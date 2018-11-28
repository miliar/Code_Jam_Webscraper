#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <cmath>
#define INF (1<<30)
#define N 5
using namespace std;
bool can(double C,double F,double X,double rate){
    double cur=X*(rate+F);
    double cc=C*(rate+F)+X*rate;
    return cur>cc;
}
void solve(){
    double C,F,X;
    double rate=2;
    scanf("%lf%lf%lf",&C,&F,&X);
    double ans=0;
    while(can(C,F,X,rate)){
        ans+=C/rate;
        rate+=F;
    }
    ans+=X/rate;
    printf("%.7f\n",ans);
}
int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("out.txt","w",stdout);
    //freopen("out.txt","r",stdin);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        printf("Case #%d: ",i);
        solve();
    }
    return 0;
}
