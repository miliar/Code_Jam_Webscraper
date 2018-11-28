#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
using namespace std;
#define MAXNUM 2000010


int map[5][5], map2[5][5];
int main()
{
    //freopen("in.txt", "r", stdin);
    //freopen("B-large.in","r", stdin);
    //freopen("B-large.out","w", stdout);
    int t;
    double c, f, x, rate;
    scanf("%d", &t);
    for(int cas = 1; cas <= t; cas++){
        scanf("%lf %lf %lf", &c, &f, &x);
        rate = 2.0;
        double ans = c/rate;
        if(c >= x) {printf("Case #%d: %.6lf\n",cas, x/rate); continue;}
        while(1){
            if(x/(rate+f) >= (x-c)/rate){
                ans += (x-c)/rate;
                printf("Case #%d: %.6lf\n",cas, ans);
                break;
            }
            else{
                rate += f;
                ans += c/rate;
            }
        }
    }
    return 0;
}

