#include <bits/stdc++.h>

#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
#define sz(a) int(a.size())
#define reset(a, x) memset(a, x, sizeof(a))

#define FOR(i, a, b)   for(int i = a; i <= b; ++i)
#define FORD(i, a, b)  for(int i = a; i >= b; --i)
#define REP(i, n)      for(int i = 0, _n = n; i < _n; ++i)
#define REPD(i, n)     for(int i = n - 1; i >= 0; --i)
#define FORSZ(i, x)    for(int i = 0; i < sz(x); ++i)

using namespace std;

typedef long long ll;
typedef pair <int, int> pii;
typedef vector <int> vi;
typedef vector <pii> vii;

#define oo 1000000007
#define eps 1E-9

int n, T;

vector <int> a;

int main() {
    #ifdef LOCAL_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    ios_base::sync_with_stdio(0);
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> n;
        a.resize(n);
        for (int i = 0; i < n; ++i) {
            int x;
            cin >> x;
            a[i] = x;
        }

        int res = oo;
        for (int i = 1; i <= 1000; ++i) {
            int tmp = 0;
            for (int j = 0; j < n; ++j)
                tmp += a[j] / i + (a[j] % i > 0) - 1;
            res = min(res, tmp + i);
        }


        cout << "Case #" << t << ": " << res << endl;
    }
}
