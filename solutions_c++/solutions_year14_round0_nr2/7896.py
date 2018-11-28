#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
const int N = 100+10;
double c, f, x;
const double eps = 1e-9;
inline int dcmp(double x) {
    return x < -eps ? -1 : x > eps;
}
int main() {
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    int T, cas = 0;
    cin >> T;
    while (T--) {
        cin >> c >> f >> x;
        double ans = x / 2;
        double tmp = 0, val = 2;

        while (1) {
            ans = min(ans, x / val + tmp);
            tmp += c / val;
            val += f;
            if (dcmp(tmp - ans) > 0) break;
        }
        printf("Case #%d: %.8lf\n",++cas, ans);
    }
    return 0;
}
