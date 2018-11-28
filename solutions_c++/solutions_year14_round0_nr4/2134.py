#include <iostream>
#include <deque>
#include <algorithm>

using namespace std;

typedef std::deque<double> Blocks;

// If she is winning, he'll choose smallest block.
int warPoints(Blocks naomi, Blocks ken)
{
    std::sort(naomi.begin(), naomi.end());
    std::sort(ken.begin(), ken.end());
    int points = 0;
    while (naomi.size())
    {
        double n = naomi.back();
        naomi.pop_back();
        if (n > ken.back())
        {
            ken.pop_front();
            ++points;
        }
        else
        {
            ken.pop_back();
        }
    }
    return points;
}

// play lowest blocks while saying they're the highest
int deceitfulWarPoints(Blocks naomi, Blocks ken)
{
    std::sort(naomi.begin(), naomi.end());
    std::sort(ken.begin(), ken.end());
    int points = 0;
    while (naomi.size())
    {
        double n = naomi.front();
        naomi.pop_front();
        for (Blocks::iterator it = ken.begin(); ken.end() != it; ++it)
        {
            if (n > *it)
            {
                ++points;
                ken.erase(it);
                break;
            }
        }
    }
    return points;
}

int main()
{
    int T;
    cin >> T;

    for (int t = 0; t < T; ++t)
    {
        Blocks naomi, ken;
        int N;
        cin >> N;
        for (int i = 0; i < N; ++i)
        {
            double W;
            cin >> W;
            naomi.push_back(W);
        }
        for (int i = 0; i < N; ++i)
        {
            double W;
            cin >> W;
            ken.push_back(W);
        }
        int dw = deceitfulWarPoints(naomi, ken);
        int w = warPoints(naomi, ken);
        cout << "Case #" << t << ": " << dw << " " << w << endl;
    }

    return 0;
}
