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

const int MAXN = 2000;

double a[MAXN], b[MAXN];
set <double> b_set;

int main ()
{
//  ios_base::sync_with_stdio(0);
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

    int t;
    cin >> t;

    for (int tc = 0; tc < t; ++tc) {
        printf ("Case #%d: ", tc + 1);

        int n;
        cin >> n;
        b_set.clear();
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }
        for (int i = 0; i < n; ++i) {
            cin >> b[i];
            b_set.insert(b[i]);
        }

        sort (a, a + n);
        sort (b, b + n);

        int ans2 = n;
        for (int i = 0; i < n; ++i) {
            set <double> :: iterator it = upper_bound(b_set.begin(), b_set.end(), a[i]);
            if (it != b_set.end()) {
                ans2--;
                b_set.erase(it);
            }
        }

        int ans1 = 0;
        bool key = true;
        while (ans1 < n && key) {
            ans1++;
            for (int j = 0; j < ans1; ++j) {
                key &= (a[n - ans1 + j] > b[j]);
            }

            if (!key) ans1--;
        }

        cout << ans1 << " " << ans2 << endl;
    }


	return 0;
}
