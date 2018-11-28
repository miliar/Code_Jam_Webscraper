/*input
5
0
1
2
11
1692
*/
#include <bits/stdc++.h>
using namespace std;
#define ll long long
//loops
#define f(i,s,n) for(ll i=(ll)s;i<(ll)n;i++)
#define rf(i,n,s) for(ll i=(ll)(n-1);i>=(ll)s;i--)
#define raf(i,v) for(__typeof(v.begin())i=v.begin(); i!=v.end(); i++)
#define pb push_back
//reset
#define ms0(X) memset((X), 0, sizeof((X)))
#define ms1(X) memset((X), -1, sizeof((X)))
//STL
#define pii pair<ll,ll>
#define vll vector<ll>
#define vpii vector<pii >
#define mpii map<pii,ll> 
#define msll map<string, ll> 
#define mll map<ll, ll>
#define sortv(v) sort(v.begin(),v.end())
#define F first
#define S second
//standard values
#define EPS 1e-6
const int MAXN = 100005;
const int mod=1e9+7;
//comparator
bool cmp(pii a,pii b){
  if(a.F==b.F) return a.S<b.S;
  else return a.F<b.F;
}
ll exp(ll a, ll b){ll ans=1;while(b!=0){if(b%2)ans=ans*a;a=a*a;b/=2;}return ans;}
/********************************************************************************************************/
bool has[15];
void mark(ll a)
{
  while(a!=0){
    ll num=a%10;
    a/=10;
    has[num]=1;
  }
}
int main() 
{
  ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
  freopen("A-large.in","r",stdin);
  freopen("ans.txt","w",stdout);
  ll n;
  cin>>n;
  f(i,0,n){
    ll a;
    cin>>a;
    if(a==0){
      cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
      continue;
    }
    ms0(has);
    bool fg=1;
    ll mul=1;
    ll val;
    while(fg){
      mark(a*mul);
      val=a*mul;
      mul++;
      bool fg1=0;
      f(j,0,10){
        if(has[j]==0){
          fg1=1;
          break;
        }
      }
      if(!fg1)
        fg=0;
    }
    cout<<"Case #"<<i+1<<": "<<val<<endl;
  }
  return 0;
}

