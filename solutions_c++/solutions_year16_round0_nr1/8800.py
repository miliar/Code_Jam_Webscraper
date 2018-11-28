#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:66777216")
#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <ctime>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <deque>
#include <cassert>
#include <cstdlib>
#include <bitset>
#include <algorithm>
#include <string>
#include <list>
#include <fstream>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;

#define forn(i, n) for (ll i = 0; i < (ll)n; i++)
#define fornn(i, q, n) for (ll i = q; i < (ll)n; i++)
#define mp make_pair
#define pk push_back
#define all(v) v.begin(), v.end()
#define times clock() * 1.0 / CLOCKS_PER_SEC

#define TASK "party"

const ld eps = 1e-9;
const double pi = acos(-1.0);

const int INF = (int)2e9 + 1;
const ll LINF = (ll)8e18;
const ll MM = (ll)1e9 + 7;
const int inf = (int)2e9 + 1;
const ll linf = (ll)8e18;

int solve();
void gen();

int main()
{
#ifdef _DEBUG
    freopen("input.txt", "r", stdin), freopen("output.txt", "w", stdout);
#else
    //freopen(TASK".in", "r", stdin), freopen(TASK".out", "w", stdout);
    freopen("input.txt", "r", stdin), freopen("output.txt", "w", stdout), freopen("test.txt", "w", stderr);
#endif
    solve();
    return 0;
}

const int dd = 1e5 + 7;

set<int> S;

void add(int x) {
    if (x == 0)
        S.insert(0);

    while (x) {
        S.insert(x % 10);
        x /= 10;
    }
}

int solve() {

    int t;
    cin >> t;
    forn(test, t) {
        int n;
        cin >> n;

        S.clear();

        add(n);

        int x = n;

        bool ok = false;
        forn(gg, 200) {
            if (S.size() == 10) {
                cout << "Case #" << test + 1 << ": " << n << "\n";
                ok = true;
                break;
            }
            n += x;
            add(n);
        }
        if (!ok) {
            cout << "Case #" << test + 1 << ": " << "INSOMNIA" << "\n";
        }
    }
    return 0;
}