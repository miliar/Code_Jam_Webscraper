#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>

using namespace std;

#define MAXN 300
#define eps 1e-9
#define INF 1e15

int T, n;

double A, C;

struct Node {
    double x, y;
}bx[110];

int main()
{
    freopen("pro.in","r",stdin);
    freopen("pro.out","w",stdout);

    int cas = 1;
    scanf("%d", &T);
    while(T--) {
        printf("Case #%d: ", cas++);

        scanf("%d%lf%lf", &n, &A, &C);

        for(int i = 1; i <= n; i++) {
            scanf("%lf%lf", &bx[i].x, &bx[i].y);
        }

        if(n == 1) {
            if(C != bx[1].y) {
                printf("IMPOSSIBLE\n");
            } else {
                double ans = A / bx[1].x;
                printf("%.10f\n", ans);
            }
        } else {
            if(bx[1].y < C && bx[2].y < C) {
                printf("IMPOSSIBLE\n");
                continue;
            }

            if(bx[1].y > C && bx[2].y > C) {
                printf("IMPOSSIBLE\n");
                continue;
            }

            double ans;

            if(bx[1].y == bx[2].y) {
                ans = A / (bx[1].x + bx[2].x);
            } else {
                double tmp = A - (C * A - A * bx[1].y) / (bx[2].y - bx[1].y);
                ans = tmp / bx[1].x;
                if((C * A - A * bx[1].y) / (bx[2].y - bx[1].y) / bx[2].x > ans) {
                    ans = (C * A - A * bx[1].y) / (bx[2].y - bx[1].y) / bx[2].x;
                }
            }

            printf("%.10f\n", ans);
        }
    }
    return 0;
}
