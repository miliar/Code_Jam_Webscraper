#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <sstream>
#include <iterator>
#include <functional>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cmath>
#include <cassert>
#include <bitset>
#include <ctime>

using namespace std;

typedef long long ll;
typedef double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<ld, ld> pnt;

#define fi first
#define se second
#define mp make_pair
#define pb push_back

const int INF = 1000 * 1000 * 1000 + 9;
const ll MOD = 1000 * 1000 * 1000 + 7;
const ld EPS = 1e-9;

const int S = 30;
int tn;

int main() {
#ifdef HOME
    freopen("/Users/sigma/Documents/Projects/blabla/blabla/input.txt", "r", stdin);
    freopen("/Users/sigma/Documents/Projects/blabla/blabla/output.txt", "w", stdout);
#endif
    ios_base::sync_with_stdio(false);
    cin >> tn;
    for (int ti = 0; ti < tn; ++ti) {
        int n;
        int a[S];
        int s = 0;
        cin >> n;
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
            s += a[i];
        }
        vector<pii> ans;
        while (s > 0) {
            int x = -1, y = -1;
            for (int i = 0; i < n; ++i) {
                if (x == -1 || a[i] >= a[x]) {
                    y = x;
                    x = i;
                } else if (y == -1 || a[i] >= a[y]) {
                    y = i;
                }
            }
            if (s & 1) {
                ans.pb(mp(x, -1));
                --a[x];
                --s;
            } else if (a[x] == a[y]) {
                ans.pb(mp(x, y));
                --a[x], --a[y];
                s -= 2;
            } else {
                ans.pb(mp(x, x));
                a[x] -= 2;
                s -= 2;
            }
        }
        cout << "Case #" << (ti + 1) << ": ";
        for (auto p : ans) {
            cout << char(p.fi + 'A');
            if (p.se != -1) {
                cout << char(p.se + 'A');
            }
            cout << " ";
        }
        cout << "\n";
    }
    return 0;
}