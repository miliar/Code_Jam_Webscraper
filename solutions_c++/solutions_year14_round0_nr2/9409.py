/*
 *       Filename:  B.cpp
 *    Description: 
 *         Author:  Wenzheng Jiang , jwzh.hi@gmail.com
 */
#include <stdio.h>
#include <string.h>

const int maxn = 100000 + 5;
const double eps = 1e-8;

int dp[maxn];

int main(int argc, const char *argv[])
{
    int t;     
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    scanf("%d",&t);
    for(int nc = 1; nc <= t; nc++) {
        double C,F,X;
        scanf("%lf%lf%lf",&C,&F,&X);
        double sec = 0, cur = 0, inc = 2.0;
        while(1){
            if(C > X+eps) {
                sec = X / inc; 
                break;
            }

            sec += C / inc;
            cur = C;

            double t1 = X / (inc+F);
            double t2 = (X - cur) / inc;
            if(t1+eps > t2) {
                // break
                sec = sec + t2;
                cur = X;
                break;
            }else {
                inc += F; 
                cur = 0;
            }
        }
        printf("Case #%d: %.7lf\n", nc, sec);
    }
    return 0;
}

