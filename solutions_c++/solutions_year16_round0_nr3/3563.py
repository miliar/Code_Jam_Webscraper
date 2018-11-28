#include <bits/stdc++.h>
 
using namespace std;
 
#define INF 1000000007
#define MAX 100010
#define ROOT 100
#define BIG 1010
#define EPS 1e-6
const double pi = 2*acos(0) ;
 
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi; 
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef pair<ii,ii> pii;
 
#define set0(a) memset(a,0,sizeof(a));
#define setminus1(a) memset(a,-1,sizeof(a)); 
#define all(x) x.begin(), x.end()
#define tr(x,it) for(auto it = x.begin(); it!=x.end(); ++it)
#define rtr(x,it) for(auto it = x.rbegin(); it!=x.rend(); ++it)
#define sz(a) int((a).size()) 
#define pb push_back 
#define mp make_pair
#define F first
#define S second
#define FOR(i,a,b) for(int i = a; i<=b; ++i)
#define NFOR(i,a,b) for(int i = a; i>=b; --i)
#define fast ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0)
int A[]={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97};
ll mulmod(ll a,ll b,ll mod){
    a%=mod;b%=mod;
  long double res=a;
  res*=b;
  ll c=(ll)(res/mod);
  a*=b;
  a-=c*mod;
  a%=mod;
  if(a<0)a+=mod;
  return a;
}
ll expo(ll a, ll b,ll mod)
{
    ll result=1; 
  while(b)
  {
    if(b&1)result=mulmod(result,a,mod);
    a=mulmod(a,a,mod);
    b>>=1;
  }
  return result;
}
bool Miller(ll p){
    if(p<2){
        return false;
    }
    if(p!=2 && p%2==0){
        return false;
    }
    for(int i=0;i<25;i++){
    if(p==A[i])return true; 
    else if(p%A[i]==0)return false;
    } 
    ll s=p-1;
    ll d=0;
    while(s%2==0){
        s/=2;d++;
    }
    for(int i=0;i<3;i++)
  { 
    ll a=rand()%(p-1)+1,temp=s;
    ll mod=expo(a,temp,p);
    if(mod==1||mod==p-1) continue;
    int flag=0;
    for(int j=1;j<d;j++)
    {
      mod=mulmod(mod,mod,p);
      if(mod==1)return false;
      if(mod==p-1)
      { flag=1;
        break;
      }
    }
    if(flag)continue; 
    return false;
  }
  return true;
} 
ll func(ll k,int c){ //converts k to base c
    string s="";
    while(k!=0){
      s+=(char)('0'+k%c);
      k/=c;
    }
    ll ans=0;
    NFOR(i,sz(s)-1,0){
      ans+=(s[i]-'0');
      ans*=10;
    }
    return ans/10;
}
ll func1(ll n,int c){
  ll k=1;
  ll ans=0;
  while(n!=0){
    ans+=(k*(n%10));
    k=k*c;
    n/=10;
  }
  return ans;
}
ll fact(ll n){
  FOR(i,2,n){
    if(n%i==0)return i;
  }
}
void solve(){
    int n,j;
    cin>>n>>j;
    ll c=-1;
    ll K=1;
    FOR(i,0,n-1)K=K*2;
    ll k;
    ll maxi=0;
    while(j--){
      c++;
      k=c*2+1+K/2; 
      if(k>K-1)break;
      k = func(k,2);
      int flag=1;
      FOR(i,2,10){
        ll L=func1(k,i);
        //maxi=max(maxi,L);
        if(Miller(L)){flag=0;}
      }
      if(!flag)j++;
      if(flag){
        cout<<k<<" ";
        FOR(i,2,10){
          cout<<fact(func1(k,i))<<" ";
        }
        cout<<"\n";
      }
    }
}
int main(){
  clock_t tm=clock();
  fast;
  int t=1;
  cin>>t;
  FOR(_t,1,t){
  	cout<<"Case #"<<_t<<": \n";solve();
  }	
  tm=clock()-tm;
  cerr<<(float)(tm)/CLOCKS_PER_SEC<<"\n";
  return 0;
} 