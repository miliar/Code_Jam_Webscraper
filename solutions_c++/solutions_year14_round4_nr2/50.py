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

const int N = 2000;

int n;
vector<int> a;
vector<int> b;
map<int,int> l;
map<int,int> r;

map<pair<int,int>,int> z[N];

int solve(int total, int lf, int rg)
{
    if (total == n)
        return 0;

    pair<int,int> p(lf, rg);
    if (z[total].count(p) != 0)
        return z[total][p];

    int result = INT_MAX;

    int value = b[total + 1];

    if (value > b[lf])
    {
        int cad = solve(total + 1, total + 1, rg) + l[value];
        result = min(result, cad);
    }

    if (value > b[rg])
    {
        int cad = solve(total + 1, lf, total + 1) + r[value];
        result = min(result, cad);
    }

    z[total][p] = result;
    return result;
}

int main(int argc, char* argv[])
{
    int tt;
    cin >> tt;

    forn(tx, tt)
    {
        cin >> n;
        a = vector<int>(n);
        forn(i, n)
            cin >> a[i];

        b = a;
        b.push_back(0);
        sort(b.begin(), b.end());
        
        l = r = map<int,int>();
        forn(i, n)
        {
            int ll = 0;
            int rr = 0;
            for (int j = 0; j < i; j++)
                if (a[j] > a[i])
                    ll++;
            for (int j = i + 1; j < n; j++)
                if (a[j] > a[i])
                    rr++;
            l[a[i]] = ll;
            r[a[i]] = rr;
        }

        forn(i, N)
            z[i].clear();

        cout << "Case #" << (tx + 1) << ": " << solve(0, 0, 0) << endl;
    }
}
