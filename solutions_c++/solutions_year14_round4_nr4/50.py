#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <ctime>
#include <climits>
#include <cassert>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <utility>
#include <algorithm>

#define forn(i, n) for (int i = 0; i < int(n); i++)

using namespace std;

const long long M = 1000000007LL;

int n, m;
vector<string> s;
vector<int> g;
int best;
long long ways;

void gen(int pos, int group)
{
    if (pos == n)
    {
        if (group == m)
        {
            int sum = 0;

            forn(i, m)
            {
                set<string> ss;
                forn(j, n)
                    if (g[j] == i)
                    {
                        forn(k, s[j].length() + 1)
                            ss.insert(s[j].substr(0, k));
                    }
                sum += ss.size();
            }

            if (best < sum)
            {
                best = sum;
                ways = 0;
            }

            if (best == sum)
            {
                ways = (ways + 1) % M;
            }
        }
    }
    else
    {
        forn(i, group)
        {
            g[pos] = i;
            gen(pos + 1, group);
        }

        g[pos] = group;
        gen(pos + 1, group + 1);
    }
}

int main(int argc, char* argv[])
{
    int tt;
    cin >> tt;

    forn(tx, tt)
    {
        cin >> n >> m;
        s = vector<string>(n);
        forn(i, n)
            cin >> s[i];

        g = vector<int>(n, -1);
        best = -1;
        gen(0, 0);

        for (int i = 1; i <= m; i++)
            ways = (ways * i) % M;

        cout << "Case #" << (tx + 1) << ": " << best << " " << ways % M << endl;
    }
}
