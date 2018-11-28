#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

void solve()
{
    double C,F,X;
    scanf("%lf%lf%lf",&C,&F,&X);
    double ans = X / 2;
    double sum = 0;
    for(int i = 0; sum < ans; i ++) {
        ans = min(ans,X / (2 + i * F) + sum);
        sum += C / (2 + i * F);
        if(i > 100000000) break;
        //cout << sum << " : " << i << endl;
    }
    printf("%.20lf\n",ans);
}
    
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas = 1; cas <= t; cas ++) {
        printf("Case #%d: ",cas);
        solve();
    }
    return 0;
}
