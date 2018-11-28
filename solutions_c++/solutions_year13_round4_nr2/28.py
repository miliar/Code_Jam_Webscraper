#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<math.h>
#include<algorithm>
#define ll long long
using namespace std;
ll worst(ll rank,ll n){
    ll Left=rank;
    if(Left==0)return 0;
    ll ret=0;
    ll round=1;
    ll rem= (1LL<<n);

    while(round<=n){
        if(Left){
            ret+=(1LL<<(n-round));
            Left--;
            Left/=2;
        }
        else{

        }
        rem/=2;
        round++;
    }
    return ret;
}
ll best(ll rank,ll n){
    ll rem=(1LL<<n);
    ll Right= rem-rank-1;
    ll round=1;
    ll ret=0;
    while(round<=n){
        if(Right){
            Right--;
            Right/=2;
        }
        else {
            ret+=(1LL<<(n-round));
        }
        rem/=2;
        round++;
    }
    return ret;
}
void solve(){
    ll n,p;
    scanf("%lld %lld",&n,&p);
    ll ans1=0,ans2=0;
    ll N=1LL<<n;
    ll s=0,e=N-1;
    while(s<=e){
        ll m = (s+e)>>1;
        if(worst(m,n)<p){
            ans1=m;
            s=m+1;
        }
        else e=m-1;
    }
    s=0,e=N-1;
    while(s<=e){
        ll m = (s+e)>>1;
        if(best(m,n)<p){
            ans2=m;
            s=m+1;
        }
        else e=m-1;
    }
    printf("%lld %lld\n",ans1,ans2);
}
int main(){
    //printf("%lld\n",1LL<<33);
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        printf("Case #%d: ",i);
        solve();
    }
}
