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
#define sd(x) scanf("%d",&x)
#define pd(x) printf("%d",x)
#define mem(x,a) memset(x,a,sizeof(x))
#define pii pair<int,int>
#define mp make_pair
#define pb push_back
#define all(v) v.begin(),v.end()
#define N (int)3e2+4
using namespace std;
void solve(){
    string s;
    string ans;
    cin>>s;
    ans+=s[0];
    for(int i=1;i<s.size();i++){
        if(s[i]>=ans[0]){
            ans=s[i]+ans;
        }
        else{
            ans+=s[i];
        }
    }
    cout<<ans<<endl;
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
