//
#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;
typedef vector<double>::const_iterator citer;

void getBlocks(vector<double> *blocks, int numBlocks) {
    blocks->clear();
    blocks->resize(numBlocks);
    for (int i = 0; i < numBlocks; ++i)
    {
        cin >> (*blocks)[i];
    }
    sort(blocks->begin(), blocks->end());
}

int beatBlock(const vector<double>& kenBlocks,
              const vector<char>&   kenUsed,
              double                toBeat)
{
    citer best = upper_bound(kenBlocks.begin(), kenBlocks.end(), toBeat);
    int index = best - kenBlocks.begin();
    for (int i = index; i < kenBlocks.size(); ++i)
    {
        if (0 == kenUsed[i]) {
            return i;
        }
    }
    return -1;
}

int findLowestUnused(const vector<char>&   kenUsed)
{
    return find(kenUsed.begin(), kenUsed.end(), 0) - kenUsed.begin();
}

int playFair(const vector<double>& naomiBlocks,
             const vector<double>& kenBlocks)
{
    int numPoints = 0;
    int numBlocks = naomiBlocks.size();
    vector<char> kenUsed(numBlocks, 0);
    for (int i = 0; i < numBlocks; ++i)
    {
        double naomiWeight = naomiBlocks[i];
        int kenIndex = beatBlock(kenBlocks, kenUsed, naomiWeight);
        if (kenIndex < 0) {
            kenIndex = findLowestUnused( kenUsed);
        }
        if (kenBlocks[kenIndex] < naomiWeight) {
            ++numPoints;
        }
        kenUsed[kenIndex] = 1;
    }
    return numPoints;
}

int playDeceitful(const vector<double>& naomiBlocks,
                  const vector<double>& kenBlocks)
{
    // first, use naomis blocks less than Kens lowest to knock out kens highest
    // then use the rest to winnnnnnnn (until we only have blocks lower than
    // kens lowest
    citer naomisLowest = naomiBlocks.begin();
    citer naomisHighest = naomiBlocks.end() - 1;
    citer kensLowest = kenBlocks.begin();
    citer kensHighest = kenBlocks.end() - 1;

    int numPoints = 0;

    while (naomisLowest != naomiBlocks.end())
    {
        if (*naomisLowest < *kensLowest) {
            // can't win, take out his highest by lying
            ++naomisLowest;
            --kensHighest;
        }
        else {
            // peasant battle
            ++naomisLowest;
            ++kensLowest;
            ++numPoints;
        }

    }
    return numPoints;
}

int main()
{
    int numTests;
    cin >> numTests;
    for(int test = 1; test < numTests + 1; ++test)
    {
        int numBlocks;
        cin >> numBlocks;
        vector<double> naomiBlocks;
        vector<double> kenBlocks;
        getBlocks(&naomiBlocks, numBlocks);
        getBlocks(&kenBlocks, numBlocks);

        int fairPoints = playFair(naomiBlocks, kenBlocks);
        int deceitPoints = playDeceitful(naomiBlocks, kenBlocks);

        cout << "Case #" << test << ": "
             << deceitPoints << ' ' << fairPoints << endl;
    }
    return 0;
}
