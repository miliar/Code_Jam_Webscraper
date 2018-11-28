#include <iostream>
#include <cstdio>
using namespace std;

int _;
double C,F,X;

int main(){
    //freopen("B-large.in","r",stdin);
    //freopen("bb.out","w",stdout);
    scanf("%d",&_);
    int cas=0;
    while(_--){
        scanf("%lf%lf%lf",&C,&F,&X);
        double las = 0;
        double ins=2;
        double ans = 1<<30;
        for (int i=0;i<=100000;i++){
            double now = las+X/ins;
            //if(now>ans) break;
            ans = min(ans,now);
            las += C/ins;
            ins += F;
        }
        printf("Case #%d: %.7lf\n",++cas,ans);
    }

}
