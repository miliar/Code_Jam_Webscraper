#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <algorithm>
#include <queue>
#include <map>
#define mem(x,val) memset (x, val, sizeof (x))
#define MAXN 1000005
using namespace std;
typedef long long ll;
const double eps = 1e-8;

int main () {
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int _, cnt = 0;
    double c, f, x, v, t, now, an;
    scanf ("%d", &_);
    while (_ --) {
        scanf ("%lf %lf %lf", &c, &f, &x);
        v = 2;  t = 0;  an = x;
        while (t < x) {
            if (t + x / v > an)  break;
            an = t + x / v;
            t += c / v;//printf("%f\n", c / v);
            v += f;
        }
        printf("Case #%d: %.7f\n", ++ cnt, an);
    }
    return 0;
}

