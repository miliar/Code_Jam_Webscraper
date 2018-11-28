#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> PII;
typedef long long LL;
typedef long double LD;
const LL INF=1ll<<60, MaxN=1<<21;
const LD eps=1e-8;

int n,m;
int a[5][5],b[5][5];

int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int t,cas=0;
    scanf("%d",&t);
    while (t--){
        LD C,F,X;
        double a,b,c;
        scanf("%lf%lf%lf",&a,&b,&c);
        C=a; F=b; X=c;
        //cin >> C >> F >> X;
        LD rate=2,ans=INF,time=0;
        for (;;){
            if (ans-(X/rate+time)<eps) break;
            ans=X/rate+time;
            time+=C/rate;
            rate+=F;
        }
        printf("Case #%d: %.7lf\n",++cas,(double)ans);
    }
    return 0;
}
