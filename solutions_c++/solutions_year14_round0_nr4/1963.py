#include <iostream>
#include <list>
#include <algorithm>

void printVector(std::list<double>& v)
{
    for (auto i : v)
    {
        std::cout << i << ' ';
    }
    std::cout << std::endl;
}

int deceitful_war(std::list<double> naomi, std::list<double> ken)
{
    int score = 0;
    for (auto cn : naomi)
    {
        double ck_first = *ken.begin();
        double ck_last = *ken.rbegin();

        if (cn > ck_first)
        {
            ++score;
            ken.pop_front();
        }
        else
        {
            ken.pop_back();
        }
    }

    return score;
}

int war(std::list<double> naomi, std::list<double> ken)
{
    int score = 0;

    for (auto cn : naomi)
    {
        double f = 0;
        for (auto ck : ken)
        {
            if (cn < ck)
            {
                f = ck;
                break;
            }
        }
        if (f == 0)
        {
            ++score;
            ken.pop_front();
        }
        else
        {
            ken.remove(f);
        }
    }

    return score;
}

int main(int argc, const char *argv[])
{
    int cases = 0;
    std::cin >> cases;

    for (int i = 1; i <= cases; ++i)
    {
        int blockCount;
        std::cin >> blockCount;

        double block;
        std::list<double> naomi;
        for (int j = 0; j < blockCount; ++j)
        {
            std::cin >> block;
            naomi.push_back(block);
        }
        std::list<double> ken;
        for (int j = 0; j < blockCount; ++j)
        {
            std::cin >> block;
            ken.push_back(block);
        }

        naomi.sort();
        ken.sort();

        std::cout << "Case #" << i << ": " << deceitful_war(naomi, ken) << ' ' << war(naomi, ken) << std::endl;
    }

    return 0;
}
