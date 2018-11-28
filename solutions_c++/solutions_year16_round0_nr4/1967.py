#include <functional>
#include <algorithm>
#include <iostream>
#include <bitset>
#include <numeric>
#include <cassert>
#include <cstdlib>
#include <string>
#include <cstdio>
#include <vector>
#include <ctime>
#include <queue>
#include <set>
#include <map>
using namespace std;
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define fore(i, b, e) for (int i = (int)(b); i <= (int)(e); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define all(x) (x).begin(), (x).end()
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long i64;
typedef unsigned long long u64;

typedef bitset<1000> B;

string print(const B& b, int n) {
    string res;
    forn(i, n) res += '0' + b[i];
    return res;
}

void solve(int k, int c) {
    cout << "sdf" << endl;
    forn(mask, 1<<k) if (mask && !(mask&(mask-1))) {
        B x;
        forn(i, k) if (mask&(1<<i)) x[i] = 1;
        B orig = x;

        int sz = k;
        B t;
        forn(iter, c-1) {
            forn(i, sz) {
                if (x[i]) {
                    forn(j, k) t[i*k+j] = 1;
                } else {
                    t |= orig << (i*k);
                }
            }

            x = t;
            sz *= k;
        }

        cout << print(x, sz) << endl;
//         cout << print(orig, k) << "\n" << print(x, sz) << endl;
    }
}

int main() {
#ifdef LOCAL
//     freopen("d.in", "r", stdin);
#endif

    int t;
    cin >> t;
    fore(tn, 1, t) {
        int n, k, s;
        cin >> n >> k >> s;
        if (k * s < n) {
            cout << "Case #" << tn << ": " << "IMPOSSIBLE" << endl;
            continue;
        }
        cout << "Case #" << tn << ":";
        int q = 0;
        forn(iter, (n + k - 1) / k) {
            i64 x = 0;
            forn(i, k) {
                x = x * n + q;
                q = (q + 1) % n;
            }
            cout << " " << x+1;
        }
        cout << endl;
    }

#ifdef LOCAL
    cerr << "Time elapsed: " << clock() / 1000 << " ms" << endl;
#endif
    return 0;
}
