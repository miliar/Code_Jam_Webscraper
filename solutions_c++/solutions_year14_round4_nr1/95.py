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

const int MAXN = 20 * 1000;
const int MAXSIZE = 1000;

int a[MAXN];
int nd[MAXN];

int main ()
{
    ios_base::sync_with_stdio(0);
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

    int tc;
    cin >> tc;

    for (int ti = 0; ti < tc; ++ti) {
        int n, x;
        cin >> n >> x;

        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }

        for (int i = 0; i <= x; ++i) {
            nd[i] = 0;
        }

        sort (a, a + n);
        int num = 0;

        for (int i = n - 1; i >= 0; --i) {
            bool key = false;
            for (int j = a[i]; j <= x; ++j) {
                if (nd[j] > 0) {
                    nd[j]--;
                    key = true;
                    break;
                }
            }

            if (!key) {
                num++;
                nd[x - a[i]]++;
            }
        }

        cout << "Case #" << ti + 1 << ": " << num << endl;
    }

	return 0;
}
