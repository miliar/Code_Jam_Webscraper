#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");

    if (fin.is_open())
    {
        int T;
        fin >> T;

        for (int i = 0; i < T; ++i)
        {
            int n;
            fin >> n;

            string distribution;
            fin >> distribution;

            long ans = 0;
            int len = distribution.size();
            if (len == 0)
            {
                // do nothing
            }
            else
            {
                long clappedCount = distribution[0] - '0';
                for (int i = 1; i < len; ++i)
                {
                    int num = distribution[i] - '0';
                    if (num > 0 && clappedCount < i)
                    {
                        ans += (i - clappedCount);
                        clappedCount += (i - clappedCount + num);
                    }
                    else
                    {
                        clappedCount += num;
                    }
                }
            }

            cout << "Case #" << i + 1 << ": " << ans << endl;
            fout << "Case #" << i + 1 << ": " << ans << endl;
        }
    }
}