#include <iostream>
#include <deque>
#include <algorithm>

using namespace std;

int simulateWar(deque<double> naomi, deque<double> ken)
{
    int naomiWins = 0;

    // Ken's optimal strategy doesn't depend on Naomi's strategy
    while (naomi.size() > 0)
    {
        double nWeight = naomi.front();
        naomi.pop_front();
        
        // Use smallest possible weight to beat it
        int idx = ken.size() - 1;
        while (idx >= 0 && ken[idx] > nWeight)
        {
            idx--;
        }
        
        if (idx == ken.size() - 1)
        {
            // Can't beat it, use smallest weight
            ken.pop_front();
            naomiWins++;
        }
        else 
        {
            ken.erase(ken.begin() + idx + 1);
        }
    }
    
    return naomiWins;
}

int simulateDeceitfulWar(deque<double> naomi, deque<double> ken)
{
    int naomiWins = 0;

    // If Naomi can't beat Ken's smallest, she lies so that Ken uses his largest
    // Otherwise she lies and tells a weight larger than Ken's largest, so that Ken uses his smallest
    while (naomi.size() > 0)
    {
        if (naomi.front() < ken.front())
        {
            ken.pop_back();
        }
        else 
        {
            ken.pop_front();
            naomiWins++;
        }
        naomi.pop_front();
    }
    
    return naomiWins;
}

int main(int argc, char** argv)
{
    int T, N;
    deque<double> naomi, ken;

    cin >> T;

    for (int i = 0; i < T; i++)
    {
        cin >> N;

        naomi.clear(); ken.clear();
        double weight;
        for (int j = 0; j < N; j++)
        {
            cin >> weight; naomi.push_back(weight);
        }
        for (int j = 0; j < N; j++)
        {
            cin >> weight; ken.push_back(weight);
        }
        
        sort(naomi.begin(), naomi.end());
        sort(ken.begin(), ken.end());
        
        int naomiWarWins = simulateWar(naomi, ken);
        int naomiDeceitfulWins = simulateDeceitfulWar(naomi, ken);
        
        cout << "Case #" << (i+1) << ": " << naomiDeceitfulWins << " " << naomiWarWins << endl;
    }
}