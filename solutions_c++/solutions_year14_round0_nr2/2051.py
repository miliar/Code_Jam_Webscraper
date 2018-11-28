#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <complex>
#include <cstring>
#include <cstdio>

using namespace std;

int T, n;

double c, f, x;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin>>T;
    int cs = 0;
    while (T--) {
        cin>>c>>f>>x;
        int mx = x / c;
        double tm = 0, cl = 2, rs = x;
        double ans = 1e10;
        for (int i = 0; i <= mx; i++) {
            double cur = tm + rs / cl;
            ans = min(ans, cur);
            tm = c / cl + tm;
            cl += f;
        }
        printf("Case #%d: %.8lf\n", ++cs, ans);
    }
    return 0;
}
