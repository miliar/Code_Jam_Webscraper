#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;
int main() {
    int tc;
    scanf("%d",&tc);
    for ( int _case = 1 ; _case <= tc ; _case++ ) {
        double mp[111111]={};
        double sum[111111]={};
        double C,F,X;
        scanf("%lf %lf %lf",&C,&F,&X);
        for ( int factory = 0 ; factory <= (int)X+1 ; factory++ ) 
            mp[factory] = C/(2+factory*F);
        sum[0] = mp[0];
        for ( int i = 1 ; i <= (int)X+1 ; i++ ) 
            sum[i] = sum[i-1] + mp[i];
        double ans = X/2.0;
        for ( int factory = 1 ; factory <= (int)X+1 ; factory++ ) {
            double now = sum[factory-1] + X/(2+factory*F);
            ans = ans > now ? now : ans;
        }
        printf("Case #%d: %.7lf\n",_case,ans);
    }
    return 0;
}
