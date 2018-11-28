#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <string>
using namespace std;
int a[5][5];
int hash[20];
int main() {
    int T,tc = 0;
    #ifndef ONLINE_JUDGE
    freopen("B-large.in", "r" , stdin);
    freopen("output.txt" , "w" , stdout);
    #endif // ONLINE_JUDGE
    scanf("%d",&T);
    while(T--) {
        double C,F,X;
        scanf("%lf%lf%lf",&C,&F,&X);
        double times = 0.0,cur = 2.0;
        while(1)
        {
            if(times + X/cur <= times + C/cur + X/(cur + F))
            {
                times += X/cur;
                break;
            }
            else
            {
                times += C/cur;
                cur += F;
            }
        }
        printf("Case #%d: %.7f\n",++tc,times);
    }
    return 0;
}
