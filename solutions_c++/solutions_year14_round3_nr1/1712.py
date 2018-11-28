#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
int n,m;

int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,cas=0;
    scanf("%d",&t);
    while (t--){
        printf("Case #%d: ",++cas);
        LL a,b;
        scanf("%lld/%lld",&a,&b);
        int cnt=0;
        while (b && b%2==0){
            b/=2; cnt++;
        }
        int ca=0;
        while (a && a%2==0){
            a/=2; ca++;
        }
        if (b>1 && b!=a){
            puts("impossible");
            continue;
        }
        if (b>1) b=1, a=1;
        cnt-=ca;
        if (a==1){
            printf("%d\n",cnt);
            continue;
        }
        LL e=1,te=0;
        while(e*2<a){
            e*=2; te++;
        }
        cnt-=te;
        printf("%d\n",cnt);
    }
    return 0;
}
