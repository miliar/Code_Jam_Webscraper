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

const int MAXN = 200;

int n;
long double v_total, x_total;
pair <long double, long double> a[MAXN];
long double t[MAXN];

int main () {
    ios_base::sync_with_stdio(0);
    freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

    int tc;
    cin >> tc;

    for (int ti = 0; ti < tc; ++ti) {
        cin >> n >> v_total >> x_total;

        for (int i = 0; i < n; ++i) {
            cin >> a[i].sc >> a[i].fs;
        }

        sort (a, a + n);

        if (a[0].fs > x_total + eps || a[n - 1].fs < x_total - eps) {
            cout << "Case #" << ti + 1 << ": " << "IMPOSSIBLE\n";
            continue;
        }

        long double en = 0;
        long double den = 0;
        for (int i = 0; i < n; ++i) {
            en += a[i].fs * a[i].sc;
            den += a[i].sc;
        }

        int ind = n - 1;
        while (en / den > x_total + eps) {
            long double y = min(a[ind].sc, (en - den * x_total) / (a[ind].fs - x_total));
            en -= y * a[ind].fs;
            den -= y;

            if (y > a[ind].sc - eps) {
                ind--;
            } else {
                break;
            }
        }

        ind = 0;
        while (en / den < x_total - eps) {
            long double y = min(a[ind].sc, (den * x_total - en) / (x_total - a[ind].fs));
            en -= y * a[ind].fs;
            den -= y;

            if (y > a[ind].sc - eps) {
                ind++;
            } else {
                break;
            }
        }

        cout.precision(20);
        cout << "Case #" << ti + 1 << ": " << v_total / den << "\n";
    }

	return 0;
}
