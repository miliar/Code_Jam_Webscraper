#include<bits/stdc++.h>
#define ll long long
#define fi first
#define se second
ll mpow(ll a, ll n,ll mod)
{ll ret=1;ll b=a;while(n) {if(n&1)
    ret=(ret*b)%mod;b=(b*b)%mod;n>>=1;}
return (ll)ret;
}
using namespace std;
#define mem(x,a) memset(x,a,sizeof(x))
#define pii pair<int,int>
#define sd(x) scanf("%d",&x)
#define pd(x) printf("%d",x)
#define mp make_pair
#define pb push_back
#define all(v) v.begin(),v.end()
#define N (int)1e6+4
using namespace std;
void solve(){
    string s;
    cin>>s;
    int i=0;
    int ans=0;
    while(i<s.size()){
        if(s[i]=='-'){
           while(i<s.size()&&s[i]!='+'){
              i++;
           }
           ans++;
        }
        else{
            while(i<s.size()&&s[i]!='-'){
                i++;
            }
            if(i!=s.size()){
                ans++;
            }
        }
    }
    cout<<ans<<endl;
}
int main(){
   //ios_base::sync_with_stdio(false);
   freopen("input.IN","r",stdin);
   freopen("out.txt","w",stdout);
   int t=1;
   sd(t);
   for(int i=1;i<=t;i++){
       printf("Case #%d: ",i);
       solve();
   }
   return 0;
}
