#include <fstream>
#include <string>

std::ifstream INPUT;
std::ofstream OUTPUT;

void RunCase();
void FindFSes();

int main(int argc, char *argv[])
{
    std::string inFileName("test.in");
    std::string outFileName("test.out");
    if (argc == 3)
    {
        inFileName = argv[1];
        outFileName = argv[2];
    }
    INPUT.open(inFileName.c_str());
    OUTPUT.open(outFileName.c_str());
    int noCases;
    INPUT >> noCases;
    FindFSes();
    for (int i = 0; i < noCases; i++)
    {
        OUTPUT << "Case #" << i + 1 << ": ";
        RunCase();
        OUTPUT << std::endl;
    }
    INPUT.close();
    OUTPUT.close();
    return 0;
}

#include <vector>

#define TONUM(x) int(x - 48)
#define FROMNUM(x) char(x + 48)

std::string Square(std::string const& number)
{
    std::string result;
    std::vector<std::string> mid;
    int s(number.size());
    result.resize(s * 2);
    mid.resize(s);

    int s_2(s / 2 + s % 2);
    int r(0);
    int j;
    for (int i = 0; i < s_2; i++)
    {
        r = 0;
        mid[i].resize(s);
        for (int d = s - 1; d >= 0; d--)
        {
            r += TONUM(number[i]) * TONUM(number[d]);
            mid[i][d] = FROMNUM(r % 10);
            r /= 10;
        }
        if (r)
            mid[i] = FROMNUM(r) + mid[i];
        j = s - i - 1;
        if (i != j)
        {
            mid[j] = mid[i] + std::string(j, '0');
            mid[j] = std::string(s * 2 - mid[j].size(), '0') + mid[j];
        }
        mid[i] += std::string(i, '0');
        mid[i] = std::string(s * 2 - mid[i].size(), '0') + mid[i];
    }

    r = 0;
    for (int d = s * 2 - 1; d >= 0; d--)
    {
        for (int i = 0; i < s; i++)
            r += TONUM(mid[i][d]);
        result[d] = FROMNUM(r % 10);
        r /= 10;
    }
    if (result[0] == '0')
        result = result.substr(1);

    if (r)
        result = FROMNUM(r) + result;
    return result;
}

std::vector<std::string> FSes;

void Check(std::string const& number)
{
    std::string square = Square(number);

    int s(square.size() - 1);
    int max(square.size() / 2);
    for (int i = 0; i < max ; i++)
        if (square[i] != square[s - i])
            return;
    FSes.push_back(square);
}

void FindFSes()
{
    int d;
    std::string poliN, poliP, it("1");
    while (it.size() <= 5)
    {
        poliN.resize(it.size() * 2 - 1);
        poliP.resize(it.size() * 2);
        poliN[it.size() - 1] =  poliP[it.size() - 1] = poliP[it.size()] = it[0];
        for (unsigned int i = 0; i < it.size() - 1; i++)
        {
            poliN[it.size() - i - 2] = poliN[it.size() + i] = poliP[it.size() - i - 2] = poliP[it.size() + i + 1] = it[i + 1];
        }

        Check(poliN);
        Check(poliP);

        d = it.size() - 1;
        while (d >= 0 && it[d] == '9')
        {
            it[d] = '0';
            d--;
        }
        if (d == -1)
            it = '1' + it;
        else
            it[d] += 1;
    }
}

void RunCase()
{
    int N(0);
    std::string a, b;
    INPUT >> a >> b;

    int k(0);
    for (unsigned int i = 0; i < FSes.size(); i++)
    {
        k = 0;
        if (FSes[i].size() < a.size())
            continue;
        if (FSes[i].size() == a.size()
            && FSes[i] != a)
        {
            while (FSes[i][k] == a[k])
                k++;
            if (FSes[i][k] < a[k])
                continue;
        }

        if (FSes[i].size() > b.size())
            continue;
        if (FSes[i].size() == b.size()
            && FSes[i] != b)
        {
            k = 0;
            while (FSes[i][k] == b[k])
                k++;
            if (FSes[i][k] > b[k])
                continue;
        }
        N++;
    }

    OUTPUT << N;
}
