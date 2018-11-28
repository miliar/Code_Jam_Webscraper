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

int main(int argc, char* argv[])
{
    int tt;
    cin >> tt;

    forn(tx, tt)
    {
        int n, m;
        cin >> n >> m;
        vector<int> a(n);
        forn(i, n)
            cin >> a[i];
        sort(a.begin(), a.end());

        int best = INT_MAX;

        {
            vector<bool> u(n);
            int cad = 0;

            forn(i, n)
                if (!u[i])
                {
                    u[i] = true;
                    cad++;
                    int maxp = -1;
                    forn(j, n)
                        if (!u[j] && a[j] + a[i] <= m)
                            maxp = j;
                    if (maxp != -1)
                        u[maxp] = true;
                }

            best = min(best, cad);
        }

        {
            vector<bool> u(n);
            int cad = 0;

            for (int i = n - 1; i >= 0; i--)
                if (!u[i])
                {
                    u[i] = true;
                    cad++;
                    int maxp = -1;
                    forn(j, n)
                        if (!u[j] && a[j] + a[i] <= m)
                            maxp = j;
                    if (maxp != -1)
                        u[maxp] = true;
                }

            best = min(best, cad);
        }

        cout << "Case #" << (tx + 1) << ": " << best << endl;
    }
}
