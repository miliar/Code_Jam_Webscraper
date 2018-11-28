#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

int main(){
    int T;
    scanf("%d", &T);
    for(int t=1;t<=T;t++){
        double C, F, X;
        scanf("%lf %lf %lf", &C, &F, &X);
        double ans=X/2.0, time=0.0, cookie=2.0;
        for(int i=1;i<=(int)X;i++){
            time+=(C/cookie), cookie+=F;
            double cnt=X/cookie;
            double now=cnt+time;
            //printf("time:%lf, cookie:%lf, %lf, %lf\n", time, cookie, cnt, now);
            if(ans>now)
                ans=now;
        }
        printf("Case #%d: %.8f\n",t, ans);
    }
    return 0;
}
