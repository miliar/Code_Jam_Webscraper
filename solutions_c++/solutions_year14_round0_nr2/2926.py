#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;
#define eps 1e-8
double C,F,X;
double speed;
double now=0;
double Time;
double dp[110000];
double GetTime(int tt){
    if (dp[tt]<0)
        dp[tt]=dp[tt-1]+C/(2+tt*F);
    return dp[tt]+(X-C)/(2+tt*F);
}
int main()
{
    int T,cas=1;
    scanf("%d",&T);
    while(T--){
        now=0;
        speed=2;
        scanf("%lf%lf%lf",&C,&F,&X);
        printf("Case #%d: ",cas++);
        if (fabs(C-X)<=eps||X<C)
            printf("%.7lf\n",X/2.0);
        else{
            int Max=int(X)+10;
            for (int i=0;i<=Max;i++) dp[i]=-1;
            dp[0]=C/2;
            for (int i=0;;i++){
                if (GetTime(i+1)>GetTime(i)){
                    printf("%.7lf\n",GetTime(i));
                    break;
                }
            }
        }
    }
    return 0;
}
