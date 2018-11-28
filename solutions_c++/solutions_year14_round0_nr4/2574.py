#include <iostream>
#include <fstream>
#include <queue>
#include <algorithm>

using namespace std;

int deceitfulWar(deque<double> naomi, deque<double> ken)
{
    sort(naomi.begin(), naomi.end());
    sort(ken.begin(), ken.end());

    // for (double naomiBlock : naomi)
    //     cout << naomiBlock << " ";
    // cout << endl;

    // for (double kenBlock : ken)
    //     cout << kenBlock << " ";
    // cout << endl;

    int score = 0;
    int size = naomi.size();
    for (int i = 0; i < size; ++i)
    {
        double kenBlock = ken.back();
        double naomiBlock = naomi.back();
        if (naomiBlock > kenBlock)
        {
            ken.pop_back();
            naomi.pop_back();
            ++score;
        }
        else
        {
            ken.pop_back();
            naomi.pop_front();
        }
    }

    return score;
}

int war(deque<double> naomi, deque<double> ken)
{
    sort(naomi.begin(), naomi.end());
    sort(ken.begin(), ken.end());

    int score = 0;
    int size = naomi.size();
    for (int i = 0; i < size; ++i)
    {
        double naomiBlock = naomi.back();
        naomi.pop_back();
        bool res = true;
        for (auto it = ken.begin(); it != ken.end(); ++it)
        {
            if (*it > naomiBlock)
            {
                res = false;
                ken.erase(it);
                break;
            }
        }

        if (res)
        {
            ++score;
            ken.pop_front();
        }
    }

    return score;
}

int main(int argc, const char *argv[])
{
    ifstream ifs(argv[1]);
    int countTestCases;
    ifs >> countTestCases;

    for (int i = 0; i < countTestCases; i++) {
        int countBlocks;
        ifs >> countBlocks;
        deque<double> naomi(countBlocks);
        deque<double> ken(countBlocks);

        for (int j = 0; j < countBlocks; j++) {
            ifs >> naomi[j];
        }

        for (int j = 0; j < countBlocks; j++) {
            ifs >> ken[j];
        }

        cout << "Case #" << i + 1 << ": " << deceitfulWar(naomi, ken) << " " << war(naomi, ken) << endl;
    }

    return 0;
}
