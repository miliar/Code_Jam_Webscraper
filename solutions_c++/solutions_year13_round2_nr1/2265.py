#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int getNumMoves(int currSize, vector<int> motes, int pos)
{
    int numMoves = 0;

    for(int i = pos; i < motes.size(); ++i)
    {
        if (currSize <= motes[i]) {
            // two choices, add a mote just smaller than us or remove this
            // If increasing our size gets us big enough, we can skip
            return 1 + min(getNumMoves(currSize*2-1, motes, i),
                           getNumMoves(currSize, motes, i+1));
        }
        currSize += motes[i];
    }
    return 0;
}

int main()
{
    int numTests;
    cin >> numTests;
    for(int test = 0; test < numTests; ++test)
    {
        int arminSize, numMotes;
        cin >> arminSize >> numMotes;

        vector<int> motes(numMotes);
        for(int i = 0; i < motes.size(); ++i)
        {
            cin >> motes[i];
        }

        if (arminSize == 1) {
            // can't eat anything
            cout << "Case #" << test+1 << ": " << numMotes << endl;
            continue;
        }

        sort(motes.begin(), motes.end());

        // First, can armin do it?
        int currSize = arminSize;
        for(int i = 0; i < motes.size(); ++i)
        {
            if (currSize <= motes[i]) {
                break;
            }
            currSize += motes[i];
        }
        if (currSize > motes.back()) {
            // Armin can do it already
            cout << "Case #" << test+1 << ": 0" << endl;
            continue;
        }

        int moves = getNumMoves(arminSize, motes, 0);
        cout << "Case #" << test+1 << ": " << moves << endl;
    }
}
