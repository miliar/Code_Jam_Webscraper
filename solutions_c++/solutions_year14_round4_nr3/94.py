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

bool used[MAXN];
int x_0[MAXN], y_0[MAXN], x_1[MAXN], y_1[MAXN];
int a[MAXN][MAXN];
int d[MAXN];

int main ()
{
    ios_base::sync_with_stdio(0);
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

    int tc;
    cin >> tc;

    for (int ti = 0; ti < tc; ++ti) {
        cerr << ti << endl;

        int w, h;
        cin >> w >> h;

        int k;
        cin >> k;
        for (int i = 0; i < k; ++i) {
            cin >> x_0[i] >> y_0[i] >> x_1[i] >> y_1[i];
        }

        int lb = k;
        int rb = k + 1;

        int dx, dy;
        for (int i = 0; i < k; ++i) {
            a[i][i] = 0;
            for (int j = i + 1; j < k; ++j) {
                if (max(x_0[i], x_0[j]) <= min(x_1[i], x_1[j])) {
                    dx = 0;
                } else {
                    dx = min(abs(x_0[i] - x_1[j]), abs(x_1[i] - x_0[j]));
                }

                if (max(y_0[i], y_0[j]) <= min(y_1[i], y_1[j])) {
                    dy = 0;
                } else {
                    dy = min(abs(y_0[i] - y_1[j]), abs(y_1[i] - y_0[j]));
                }

                a[i][j] = max(max(dx, dy) - 1, 0);
                a[j][i] = a[i][j];
            }
        }

        for (int i = 0; i < k; ++i) {
            a[lb][i] = x_0[i];
            a[rb][i] = w - 1 - x_1[i];
            a[i][lb] = a[lb][i];
            a[i][rb] = a[rb][i];
        }

        a[lb][lb] = 0;
        a[rb][rb] = 0;
        a[lb][rb] = w;
        a[rb][lb] = w;

        for (int i = 0; i < k + 2; ++i) {
            used[i] = false;
            d[i] = inf;
        }

        d[lb] = 0;

        for (int i = 0; i < k + 2; ++i) {
            int min_d = inf;
            int ind;
            for (int j = 0; j < k + 2; ++j) {
                if (!used[j] && d[j] < min_d) {
                    min_d = d[j];
                    ind = j;
                }
            }

            used[ind] = true;
            for (int j = 0; j < k + 2; ++j) {
                d[j] = min(d[j], d[ind] + a[ind][j]);
            }
        }

        cout << "Case #" << ti + 1 << ": " << d[rb] << endl;
    }

	return 0;
}
