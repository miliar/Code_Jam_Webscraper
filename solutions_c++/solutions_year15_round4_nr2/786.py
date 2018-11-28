#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <iostream>
#include <string>
#include <set>

using namespace std;
typedef long long LL;
typedef unsigned int uint;

const int MOD = 1000000007;
const double PI = acos(-1.0);

const int MAXN = 100000;

int n;
double V, X;
double r[110], c[110];

int main()
{
    int T;
    scanf("%d", &T);
    for(int cas=1; cas<=T; cas++) {
        scanf("%d%lf%lf", &n, &V, &X);
        for(int i=1; i<=n;i++) {
            scanf("%lf%lf", &r[i], &c[i]);
        }

        printf("Case #%d: ", cas);
        if(n == 1) {
            if(X != c[1]) {
                printf("IMPOSSIBLE\n");
            }
            else {
                printf("%.8lf\n", V / r[1]);
            }
        }
        else {
            if(X == c[1] && X == c[2]) {
                printf("%.8lf\n", V / (r[1] + r[2]));
            }
            else if(X == c[1])
            {
                printf("%.8lf\n", V / r[1]);

            }
            else if(X == c[2]) {
                printf("%.8lf\n", V / r[2]);

            }
            else {
                if(!(max(c[1], c[2]) > X && min(c[1], c[2]) < X))
                {
                    printf("IMPOSSIBLE\n");
                }
                else {
            double p1 = (r[2]*c[2] - r[2]*X) / (r[1]*X - r[1] * c[1]);
            double p2 = 1/p1;
            double t1 = V / (r[2] * p2 + r[1]);
            double t2 = V / (r[1] * p1 + r[2]);
            //printf("p1:%lf p2:%lf t1:%lf t2:%lf\n", p1, p2, t1, t2);
            if(t1 < 0 || t2 < 0) {
                printf("IMPOSSIBLE\n");

            }
            else {
                printf("%.8lf\n", max(t1, t2));
            }
                }
            }
            /*
            double t = V / (r[1] + r[2]);
            double aim = X * V;
            double fenzi = (r[1] * t * c[1]) + (r[2] * t * r[2]);
            printf("aim:%lf fenzi:%lf\n", aim, fenzi);
            if(fabs(aim-fenzi) < 1e-8) {
                printf("%.8lf\n", t);
            }
            else {
                printf("IMPOSSIBLE\n");
            }
            */

        }
    }

    return 0;
}
