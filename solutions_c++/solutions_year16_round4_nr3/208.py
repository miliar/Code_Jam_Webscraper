#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <cstdio>
#include <cmath>
#include <iomanip>
#include <deque>
#include <ctime>
#include <cstring>
#include <unordered_map>
#include <unordered_set>

//#include <bits/stdc++.h>

using namespace std;

#define endl '\n'

#define forr(i, n) for(ll (i) = 0LL; (i) < (n); (i)++)

typedef long long ll;
typedef pair<ll, ll> pll;
typedef pair<ll, pll> plll;
typedef vector < vector < double > > vvd;
typedef vector < double > vd;
typedef vector < pair < double, double> > vdd;
typedef vector < vector < long long > > vvl;
typedef vector < long long > vl;
typedef vector < pll > vll;

int INT_MAX_VAL = (int)  0x3F3F3F3F;
int INT_MIN_VAL = (int) -0x3F3F3F3F;
ll LONG_MAX_VAL = (ll)   0x3F3F3F3F3F3F3F3F;
ll LONG_MIN_VAL = (ll)  -0x3F3F3F3F3F3F3F3F;

#define MAXN 500
#define MOD 1000000007
int n, m;

char ans[100][100];
map<pll, vll> G;
set<pll> used;

bool dfs(pll p1, pll p2)
{
    if (p1 == p2) {
        return true;
    }

    if (used.count(p1)) return false;
    used.insert(p1);

    for (auto &p3 : G[p1]) {
        if(dfs(p3, p2)) {
            return true;
        }
    }
    return false;
}

void connect_graph(int a1, int b1, int a2, int b2)
{
    G[make_pair(a1, b1)].push_back(make_pair(a2, b2));
    G[make_pair(a2, b2)].push_back(make_pair(a1, b1));
}

void fill_graph(int mask)
{
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            int a = 2 * i + 1;
            int b = 2 * j + 1;

            if (mask & 1) {
                ans[i][j] = '/';

                connect_graph(a - 1, b, a, b - 1);
                connect_graph(a + 1, b, a, b + 1);
            } else {
                ans[i][j] = '\\';
                connect_graph(a - 1, b, a, b + 1);
                connect_graph(a + 1, b, a, b - 1);
            }
            mask /= 2;
        }
    }

}

pll int_to_pair(int i)
{
    if (i < m) {
        return {0, 2 * i + 1};
    }

    i -= m;

    if (i < n) {
        return {2 * i + 1, 2 * m};
    }

    i -= n;

    if (i < m) {
        return {2 * n, 2 * (m - i - 1) + 1};
    }

    i -= m;

    return {2 * (n - i - 1) + 1 , 0};
}

void solve(int test)
{
    cin >> n >> m;
    vll vs;
    //cerr << n << " " << m << "     ";
    for (int i = 0; i < n + m; ++i) {
        int a, b; cin >> a >> b;
      //  cerr << a << " " << b << " ";
        --a; --b;
        vs.emplace_back(a, b);
    }
//    cerr << endl;

    int gn = 2 * n + 1;
    int gm = 2 * m + 1;


    for (int mask = 0; mask <= (1 << (n * m)); ++mask) {
        G.clear();
        fill_graph(mask);

        bool is_good = true;
        for (auto &p : vs) {
            auto p1 = int_to_pair(p.first);
            auto p2 = int_to_pair(p.second);

            used.clear();

            if (!dfs(p1, p2)) {
        //        cout << p.first << " " << p.second << endl;
                is_good = false;
                break;
            }
        }

        if (is_good) {
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < m; ++j) {
                    cout << ans[i][j];
                }
                cout << endl;
            }

            return;
        }
    }

    cout << "IMPOSSIBLE" << endl;
}

int main()
{
    cin.tie(0);
    ios::sync_with_stdio(false);
/*
    n = 3, m = 2;
    for (int i = 0; i < 2 * (n + m); ++i) {
        auto p = int_to_pair(i);

        cout << i << "  " << p.first << " " << p.second << endl;
    }

    return 0;
*/

    int t; cin >> t;
    for(int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": " << endl;
        solve(t);
//        cout << endl;
    }

    return 0;
}
