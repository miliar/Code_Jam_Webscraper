#include<stdio.h>
#include<stdlib.h>
#include<vector>

#include<math.h>
#include<algorithm>
#define mod 1000002013LL
#define ll long long
using namespace std;
ll n,m;
typedef pair<ll,ll> pl;
ll comCost(ll s,ll e){
    ll dif = e-s;

    return (n*dif - (dif*(dif-1LL)/2))%mod;
}
pl stack[1010];
int top=0;
void solve(){
    scanf("%lld %lld",&n,&m);
    vector<pl> b,e;
    ll old=0;
    for(int i=0;i<m;i++){
        ll q,w,p;
        scanf("%lld %lld %lld",&q,&w,&p);
        b.push_back(make_pair(q,p));
        e.push_back(make_pair(w,p));
        old+= (p* comCost(q,w))%mod;
        old%=mod;
    }
    sort(b.begin(),b.end());
    sort(e.begin(),e.end());
    top =0;
    int idx=0;

    ll ans=0;
    for(int i=0;i<m;i++){
       // printf("i=%d\n",i);
        while(idx<m&&b[idx].first<=e[i].first){
            stack[top++]=b[idx++];
        }
        ll rem=e[i].second;
        while(rem){
            if(stack[top-1].second<rem){
                rem-=stack[top-1].second;
                ans+= (comCost(stack[top-1].first,e[i].first)*stack[top-1].second)%mod;
                top--;
            }
            else{
                ans+= (comCost(stack[top-1].first,e[i].first)*rem)%mod;
                stack[top-1].second-=rem;
                rem=0;

                if(stack[top-1].second==0)top--;
            }
            ans%=mod;
        }
    }
    //printf("%lld %lld\n",old,ans);
    old-=ans;
    old%=mod;
    old+=mod;
    old%=mod;
    printf("%lld\n",old);
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        printf("Case #%d: ",i);
        solve();
    }
}
