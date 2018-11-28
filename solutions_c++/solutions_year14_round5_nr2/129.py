#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <bitset>
#include <sstream>
#include <queue>

#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz(a) ((int) (a).size())
#define eprintf(...) fprintf(stderr, __VA_ARGS__)

using namespace std;

typedef long long int64;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const long long inf64 = ((long long)1 << 62) - 1;
const long double pi = acos(-1);

template <class T> T sqr (T x) {return x * x;}
template <class T> T abs (T x) {return x < 0 ? -x : x;}

const int MAXN = 1200;
const int MAXM = 12000;

int h[MAXN], g[MAXN];
int d[MAXN][MAXM];

int main () {
    ios_base::sync_with_stdio(0);
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

    int tc;
    cin >> tc;

    for (int it = 0; it < tc; ++it) {
        int p, q, n;
        cin >> p >> q >> n;

        int mps = 10;
        for (int i = 0; i < n; ++i) {
            cin >> h[i] >> g[i];
            mps += (h[i] + p - 1) / p;
        }

        for (int i = 0; i <= mps; ++i) {
            d[n][i] = 0;
        }

        for (int i = n - 1; i >= 0; --i) {
            for (int j = 0; j <= mps; ++j) {
                d[i][j] = d[i + 1][min(mps, (h[i] + q - 1) / q + j)];
                for (int k = 0; k < (h[i] + q - 1) / q; ++k) {
                    int steps = (h[i] - k * q + p - 1) / p;
                    if (j + k >= steps) {
                        d[i][j] = max(d[i][j], d[i + 1][min(j + k - steps, mps)] + g[i]);
                    }
                }
            }
        }

        cout << "Case #" << it + 1 << ": " << d[0][1] << endl;
    }

	return 0;
}
