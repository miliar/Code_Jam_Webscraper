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

using namespace std;

typedef long long ll;
typedef long double ld;
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


int main() {
#ifdef HOME
    freopen("/Users/sigma/Documents/Projects/blabla/blabla/input.txt", "r", stdin);
    freopen("/Users/sigma/Documents/output.txt", "w", stdout);
#endif
    int tn;
    cin >> tn;
    for (int ti = 0; ti < tn; ++ti) {
        ll n;
        cin >> n;
        int c[10], cnt = 10;
        memset(c, 0, sizeof c);
        int i = 1;
        for (; i <= 2000000 && cnt; ++i) {
            ll x = n * i;
            while (x > 0) {
                if ((c[x % 10]++) == 0) {
                    --cnt;
                }
                x /= 10;
            }
        }
        cout << "Case #" << (ti + 1) << ": ";
        if (!cnt) {
            cout << ((i - 1) * n) << '\n';
        } else {
            cout << "INSOMNIA\n";
        }
    }
    return 0;
}