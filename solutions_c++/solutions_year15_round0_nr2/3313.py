#include <iostream>
#include <cassert>
#include <vector>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int run = 1; run <= T; ++run)
    {
        int D;
        cin >> D;
        vector<int> values(D);
        for (int i = 0; i < D; i++) cin >> values[i];

        int maxVal = 0;
        for (int i = 0; i < D; i++) if (values[i] > maxVal) maxVal = values[i];

        int optimal = maxVal;
        for (int maxpile = 1; maxpile < maxVal; maxpile++)
        {
            int moves = 0;
            for (int i = 0; i < D; i++)
            {
                if (values[i] > maxpile)
                {
                    // ceil( (val - maxpile)/maxpile )
                    moves += (values[i] - 1) / maxpile;
                }
            }
            if (moves + maxpile < optimal)
                optimal = moves + maxpile;
        }

        cout << "Case #" << run << ": " << optimal << endl;
    }
}
