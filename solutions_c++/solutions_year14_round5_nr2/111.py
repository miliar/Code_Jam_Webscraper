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

int p[2];
int n;
vector<int> h;
vector<int> g;

void readData()
{
    cin >> p[0] >> p[1] >> n;
    h = g = vector<int>(n);
    forn(i, n)
        cin >> h[i] >> g[i];
}

int tok[400];
int result;

int z[201][201][21 * 101];

int get(int pos, int ms, int r)
{
    if (pos >= n)
    {
        z[pos][ms][r] = 0;
        return 0;
    }

    if (z[pos][ms][r] != -1)
        return z[pos][ms][r];

    assert(h[pos] > ms);
    if (r > 0)
    {
        for (int k = 1; k <= r; k++)
        {
            int left = h[pos] - ms - p[0] * k;
            if (left <= 0)
            {
                z[pos][ms][r] = max(z[pos][ms][r], g[pos] + get(pos + 1, 0, r - k));
            }
            else
            {
                z[pos][ms][r] = max(z[pos][ms][r], get(pos, ms + p[0] * k, r - k));
            }
        }
    }

    if (h[pos] - ms - p[1] <= 0)
    {
        z[pos][ms][r] = max(z[pos][ms][r], get(pos + 1, 0, r + 1));
    }
    else
    {
        z[pos][ms][r] = max(z[pos][ms][r], get(pos, ms + p[1], r + 1));
    }

    // cout << pos << " " << ms << " " << r << ": " << z[pos][ms][r] << endl;

    return z[pos][ms][r];
}

void solve()
{
    /*
    tok[0] = 0;

    for (int i = 1; i <= 200; i++)
    {
        tok[i] = INT_MAX;

        forn(d, 2)
        {
            for (int c = 1; c <= 200; c++)
            {
                if (c * p[d] >= i)
                {
                    if (d == 0)
                    {
                        tok[i] = min(tok[i], c);
                    }
                }
                else
                {
                    int cc[2] = {0, 0};
                    cc[d] += c;

                    int id = d ^ 1;
                    int r = i - c * p[d];
                    while (r > 0)
                    {
                        cc[id]++;
                        r -= p[id];
                        id ^= 1;
                    }

                    if (id == 1)
                    {
                        tok[i] = min(tok[i], cc[0]);
                    }
                }
            }
        }
    }
    */

    memset(z, -1, sizeof(z));

    result = get(0, 0, 1);
}

int main(int argc, char* argv[])
{
    int tt;
    cin >> tt;

    int fromTest = 1;
    int toTest = tt;

    if (argc == 3)
    {
        fromTest = atoi(argv[1]);
        toTest = atoi(argv[2]);
    }

    cerr << "Solving " << fromTest << " ... " << toTest << endl;

    for (int tx = 1; tx <= tt; tx++)
    {
        readData();
        if (tx >= fromTest && tx <= toTest)
        {
            solve();
            cout << "Case #" << (tx) << ": " << result << endl;
        }
    }
}
