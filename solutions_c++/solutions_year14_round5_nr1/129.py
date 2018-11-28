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

const int MAXN = 1000 * 1000 + 100;

int a[MAXN];

int main () {
    ios_base::sync_with_stdio(0);
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

    int tc;
    cin >> tc;

    for (int it = 0; it < tc; ++it) {
        long long n, p, q, r, s;
        cin >> n >> p >> q >> r >> s;

        long long sum = 0;
        for (int i = 0; i < n; ++i) {
            a[i] = ((i * p + q) % r) + s;
            sum += a[i];
        }
        long long total_sum = sum;

        long long sum1 = 0;
        long long sum2 = 0;
        int ind = 0;

        long long ans = sum;
        for (int i = 0; i < n; ++i) {
            sum -= a[i];
            sum2 += a[i];

            while (sum1 + a[ind] <= sum2 - a[ind]) {
                sum1 += a[ind];
                sum2 -= a[ind];
                ind++;
            }

            //cerr << sum1 << " " << sum2 << " " << sum << endl;
            ans = min(ans, max(sum, min(max(sum1, sum2), max(sum1 + a[ind], sum2 - a[ind]))));
        }

        ans = total_sum - ans;
        long double pr = ((long double)ans) / total_sum;

        cout.precision(20);
        cout << "Case #" << it + 1 << ": " << pr << endl;
    }

	return 0;
}
