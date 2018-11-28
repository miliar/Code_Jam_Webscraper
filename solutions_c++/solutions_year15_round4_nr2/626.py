#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <queue>

#define LL long long
#define mp(x, y) make_pair(x, y)
#define pb(x) push_back(x)

using namespace std;

const long double eps = 1e-12;
int n, m, T;
long double V, X;
pair<long double, long double> spring[110];

int main(){
//    freopen("B-small-attempt2.in", "r", stdin);
    scanf("%d", &T);
    for (int Tno = 1; Tno <= T; ++Tno) {
        double a, b;
        scanf("%d%lf%lf", &n, &a, &b);
        V = a; X = b;
        for (int i = 0; i < n; ++i) {
            scanf("%lf%lf", &a, &b);
            spring[i] = make_pair((long double)b, (long double)a);
        }
        sort(spring, spring + n);

        double r = 1e8;
        if (n == 1) {
            if (fabs(spring[0].first - X) < eps)
                r = V / spring[0].second;
        } else if (n == 2) {
            if (spring[0].first <= X && spring[1].first >= X) {
                if (spring[0].first == spring[1].first) {
                    r = V / (spring[0].second + spring[1].second);
                } else {
                    double x1 = V * (X - spring[0].first) / (spring[1].second * (spring[1].first - spring[0].first));
                    double x0 = (V - spring[1].second * x1) / spring[0].second;
                    r = max(x0, x1);
                }
            }
        }

        printf("Case #%d: ", Tno);
        if (r > 1e7) printf("IMPOSSIBLE\n");
        else printf("%.9f\n", (double)r);
    }
}
