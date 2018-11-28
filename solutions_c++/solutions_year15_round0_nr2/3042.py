#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
using namespace std;

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");

    if (fin.is_open())
    {
        int T;
        fin >> T;

        for (int i = 0; i < T; ++i)
        {
            int D;
            fin >> D;

            long ans = -1;

            vector<long> remainingCounts;
            long maxRemaining = 0;
            for (int j = 0; j < D; ++j)
            {
                long initialCount;
                fin >> initialCount;
                remainingCounts.push_back(initialCount);

                if (initialCount > maxRemaining)
                {
                    maxRemaining = initialCount;
                }
            }

            if (maxRemaining > 1)
            {
                long dividingLimit = 2;
                long maxRemainingAfter = 0;
                while (dividingLimit <= maxRemaining)
                {
                    long count = 0;
                    int len = remainingCounts.size();
                    for (int j = 0; j < len; ++j)
                    {
                        if (remainingCounts[j] < dividingLimit)
                        {
                            if (remainingCounts[j] > maxRemainingAfter)
                            {
                                maxRemainingAfter = remainingCounts[j];
                            }
                        }
                        else if (remainingCounts[j] % dividingLimit == 0)
                        {
                            count += ((remainingCounts[j] / dividingLimit) - 1);
                            maxRemainingAfter = dividingLimit;
                        }
                        else
                        {
                            count += (remainingCounts[j] / dividingLimit);
                            maxRemainingAfter = dividingLimit;
                        }
                    }

                    if (ans < 0 || count + maxRemainingAfter < ans)
                    {
                        ans = count + maxRemainingAfter;
                    }

                    dividingLimit++;
                }
            }
            else
            {
                ans = 1;
            }

            cout << "Case #" << i + 1 << ": " << ans << endl;
            fout << "Case #" << i + 1 << ": " << ans << endl;
        }
    }
}