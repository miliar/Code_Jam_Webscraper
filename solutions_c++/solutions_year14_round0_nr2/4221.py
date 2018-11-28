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

int magic = 5;

int main ()
{
//  ios_base::sync_with_stdio(0);
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

    int t;
    cin >> t;

    for (int tc = 0; tc < t; ++tc) {
        printf ("Case #%d: ", tc + 1);

        double c, f, x;
        cin >> c >> f >> x;
        double a0 = 2.0;

        cout.precision(20);
        if (c * (f + a0) > x * f - eps) {
            cout << x / a0 << endl;
            continue;
        }

        int mk = (int) (round((x * f - c * a0) / c / f) - 1.0 + eps);
        double min_time = x / a0;
        for (int k = max(mk - magic, 0); k <= mk + magic; ++k) {
            double time = 0;
            for (int i = 0; i < k; ++i) {
                time += c / (a0 + i * f);
            }
            time += x / (a0 + k * f);
            min_time = min(min_time, time);
        }

        cout << min_time << endl;
    }


	return 0;
}
