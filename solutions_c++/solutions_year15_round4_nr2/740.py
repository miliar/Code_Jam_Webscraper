#include "bits/stdc++.h"
#define puba push_back
#define mapa make_pair
#define ff first
#define ss second
#define bend(_x) (_x).begin(), (_x).end()
#define szof(_x) ((int) (_x).size())

using namespace std;
typedef long long LL;
typedef pair <int, int> pii;
const long double eps = 1e-9;

int t;

int main() {    
    //freopen(".in", "r", stdin);
    //freopen(".out", "w", stdout);

    cin >> t;

    for (int i = 0; i < t; ++i) {
        int n;
        long double v, x;
        //cerr << i + 1 << endl;
        cin >> n >> v >> x;
        //cerr << n << " " << v << " " << x << endl;
        vector <pair <long double, long double> > arr;
        long double sv = 0;
        long double tmp = 0;
        for (int j = 0; j < n; ++j) {
            long double r, c;
            cin >> r >> c;
            //cerr << r << " " << c << endl;
            arr.puba(mapa(c, r));
            sv += r;
            tmp += r * c;
        }
        long double t = tmp / sv;
        sort(bend(arr));
        if (fabs(t - x) < eps) {
            //cerr << "@" << endl;
            printf("Case #%d: %.9lf\n", i + 1, (double) (v / sv));
            continue;
        }
        bool flag = false;
        if (t > x) {
            for (int j = n - 1; j > 0; --j) {
                tmp -= arr[j].ff * arr[j].ss;
                sv -= arr[j].ss;
                if (tmp / sv <= x + eps) {
                    //cerr << j << " " << arr[j].ff << endl;
                    flag = true;
                    if (fabs(arr[j].ff - x) < eps) {
                        //cerr << "@" << endl;
                        sv += arr[j].ss;
                        break;
                    }
                    long double unx = (x * sv - tmp) / (arr[j].ff - x);
                    sv += unx;
                    break;
                }
            }
        } else {
            for (int j = 0; j < n - 1; ++j) {
                tmp -= arr[j].ff * arr[j].ss;
                sv -= arr[j].ss;
                if (tmp / sv >= x - eps) {
                    flag = true;
                    if (fabs(arr[j].ff - x) < eps) {
                        sv += arr[j].ss;
                        break;
                    }
                    long double unx = (x * sv - tmp) / (arr[j].ff - x);
                    sv += unx;
                    break;
                }
            }
        }
        //cerr << sv << endl;
        if (!flag) {
            printf("Case #%d: IMPOSSIBLE\n", i + 1);
            continue;
        }
        //cerr << v << " " << sv << endl;
        printf("Case #%d: %.9lf\n", i + 1, (double) (v / sv));
    }

    return 0;
}