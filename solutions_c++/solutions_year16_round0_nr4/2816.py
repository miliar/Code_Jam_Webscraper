#include<bits/stdc++.h>
#define ll long long
#define fi first
#define se second
ll mpow(ll a, ll n,ll mod)
{ll ret=1;ll b=a;while(n) {if(n&1)
    ret=(ret*b)%mod;b=(b*b)%mod;n>>=1;}
return (ll)ret;
}
ll nmpow(ll a, ll n)
{ll ret=1;ll b=a;while(n) {if(n&1)
    ret=(ret*b);b=(b*b);n>>=1;}
return (ll)ret;
}
using namespace std;
#define mem(x,a) memset(x,a,sizeof(x))
#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define all(v) v.begin(),v.end()
#define N (int)3e5+4
using namespace std;
void solve(){
    ll k,c,s,x,nx;
    vector<pair<ll,ll> > range;
    cin>>k>>c>>s;
    ll nc=c;
    ll len=nmpow(k,c);
    x=1;
    nx=1;
    while(nc>1){
        nx*=k;
        nx+=min(1ll,len-1);
        nc--;
    }
    range.pb(mp(x,nx));
    for(ll i=2;i<k;i++){
        x=(i-1)*nmpow(k,c-1)+1;
        nx=x+nmpow(k,c-1)-1;
        nx=min(nx,len);
        range.pb(mp(x,nx));
    }
    if(k>1){
        nx=len;
        nc=c;
        x=1;
        while(nc>1){
            x*=k;
            x++;
            nc--;
        }
        range.pb(mp(nx-x+1,nx));
    }
    vector<ll> ans;
    ll lie=range[0].se;
    ans.pb(x);
    for(int i=1;i<range.size();i++){
        if(lie>=range[i].fi&&lie<=range[i].se){
            continue;
        }
        else{
            ans.pb(range[i].se);
            lie=range[i].se;
        }
    }
    if(ans.size()>s){
        printf("IMPOSSIBLE\n");
        return;
    }
    for(int i=0;i<ans.size();i++){
        cout<<ans[i]<<" ";
    }
    cout<<endl;
}
int main(){
   //ios_base::sync_with_stdio(false);
    freopen("input.IN","r",stdin);
    freopen("out.txt","w",stdout);
   int t=1;
   scanf("%d",&t);
   for(int i=1;i<=t;i++){
       printf("Case #%d: ",i);
       solve();
   }
   return 0;
}
