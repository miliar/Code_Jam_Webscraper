/* Pranet Verma */
/* Yeh mera template hai. Apna khud banao =_= */
#include <bits/stdc++.h>
using namespace std;
#define infinity (1000000007)
#define ll long long
#define ull unsigned long long
#define pii pair<int,int>
#define ppi pair<pii,int>
#define ppp pair<pii,pii>
#define pip pair<int,pii>
#define pb push_back
#define mp make_pair
#define s(n) scanf("%d",&n)
#define s2(n,m) scanf("%d%d",&n,&m)
#define s3(n,m,l) scanf("%d%d%d",&n,&m,&l)
#define rep(i,n) for(int i=0;i<n;++i)
ll pwr(ll a,ll b,ll mod) {a%=mod;if(a<0)a+=mod;ll ans=1; while(b) {if(b&1) ans=(ans*a)%mod; a=(a*a)%mod; b/=2; } return ans; }
ll pwr(ll a,ll b) {ll ans=1; while(b) {if(b&1) ans*=a; a*=a; b/=2; } return ans; }
ll gcd(ll a,ll b) {while(b) {ll temp=a; a=b; b=temp%b; } return a; }
ll lcm(ll a,ll b) {return (a/gcd(a,b))*b; }
ll modularInverse(ll a,ll m) {/*reminder: make sure m is prime*/ assert(false); return pwr(a,m-2,m); }
const int mod=1000000007;
vector<int> cnt(10);
map<vector<int>,int> M;
int dp(vector<int> cnt,int u)
{

  if(u==1)
    return (cnt[1]>0?1:0);
  int o1=u;
  if(M.find(cnt)!=M.end())
    return M[cnt];

  int o2=infinity;
  
  vector<int> key=cnt;
  
  if(cnt[u]>0)
  {
    --cnt[u];
    for(int i=1;i<u;++i)
    {
      ++cnt[i];
      ++cnt[u-i];
      o2=min(o2,1+dp(cnt,u));
      --cnt[i];
      --cnt[u-i];
    }
    ++cnt[u];
  }
  else
    o2=dp(cnt,u-1);
  
  return M[key]=min(o1,o2);
}
int main()
{
  std::ios::sync_with_stdio(false);


    
  int t;
  cin>>t;
  for(int tt=1;tt<=t;++tt)
  {
    cout<<"Case #"<<tt<<": ";

    int n;
    cin>>n;
    for(int i=0;i<10;++i)
      cnt[i]=0;
    for(int i=0;i<n;++i)
    {
      int x;
      cin>>x;
      ++cnt[x];
    }
    cout<<dp(cnt,9)<<endl;

  }
  
   


}