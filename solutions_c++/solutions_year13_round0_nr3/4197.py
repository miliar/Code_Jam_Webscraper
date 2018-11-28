#include <fstream>
#include <iostream>
#include <vector>

int compare(const std::string& s1, const std::string& s2)
{
    std::string::size_type length = s1.size();
    if (length < s2.size()) return -1;
    if (length > s2.size()) return 1;

    for (std::string::size_type i = 0; i < length; ++i)
        if (s1[i] < s2[i]) return -1;
        else if (s1[i] > s2[i]) return 1;

    return 0;
}

int solveProblemC(const std::string& a, const std::string& b, std::vector<std::string>& data)
{
    int result = 0;
    std::vector<std::string>::size_type i = 0;

    while (i < data.size())
    {
        if (compare(a, data[i]) <= 0)
            break;

        ++i;
    }

    while (i < data.size())
    {
        if (compare(data[i], b) <= 0)
            ++result;
        else
            break;

        ++i;
    }

    return result;
}

void readData(std::vector<std::string>& data)
{
    std::ifstream fin("problemC.dat");
    char buffer[1000];

    while (!fin.getline(buffer, 1000).eof())
    {
        data.push_back(std::string(buffer));
    }

    fin.close();
}

void problemC(std::ifstream& fin)
{
    std::vector<std::string> data;
    readData(data);

    std::ofstream fout("C:\\CodeJam\\problemC.out");
    char buffer[1000];

    fin.getline(buffer, 1000);
    int t = atoi(buffer);

    for (int i = 1; i <= t; ++i)
    {
        fin.getline(buffer, 1000);
        char* pos = strchr(buffer, ' ');
        *pos = '\0';

        fout << "Case #" << i << ": "
             << solveProblemC(std::string(buffer), std::string(pos + 1), data) << std::endl;
    }

    fout.close();
}

int main(int argc, char* argv[])
{
    std::ifstream fin("C:\\CodeJam\\C-large-1.in");
    if (fin.is_open())
    {
        problemC(fin);
        fin.close();
    }

    return 0;
}
