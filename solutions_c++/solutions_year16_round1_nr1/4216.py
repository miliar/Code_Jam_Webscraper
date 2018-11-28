#include <bits/stdc++.h>
#define ll long long int
#define pi 3.1415926535897
#define ff first
#define ss second
#define loop(a,b) for(a=0;a<b;a++)
#define test() while(t--)
 
using namespace std;
 

 
const ll N=1000005;
const ll MOD = 1000000007LL;
int phi[N];
ll sum[N],ans[N];
 
ll fact[1000006];
ll ifact[1000006];
ll power2[1000006];
 
inline ll powr (ll a, ll  b)
{
    if (b == 0)
        return 1;
    long long int x = powr(a, b/2);
    if (b % 2 == 0)
        return (x*x)%MOD;
    else
        return (((x*x)%MOD)*a)%MOD;
}
 
inline ll inv(ll x) {
  return powr(x, MOD - 2);
}
 
inline ll mulMod(ll a, ll b) {
  return (a%MOD * b%MOD) % MOD;
}
 
inline void process() {
  fact[0] = 1;
  power2[0] = 1;
  for(int i = 1; i < 100003; i++) {
    fact[i] = mulMod(fact[i - 1], i);
    power2[i] = mulMod(power2[i - 1], 2);
  }
  ifact[100002] = inv(fact[100002]);
  for(int i = 100002 - 1; i >= 0; i--) {
    ifact[i] = mulMod(ifact[i + 1], i + 1);
  }
}
 
inline ll ncr(ll n, ll r) {
  if(n < r) return 0;
  return mulMod(fact[n], mulMod(ifact[r], ifact[(n - r)]));
}
 
inline void calc()
{
    ll i,j;
    for(i=1;i<N;i++) phi[i]=i;
    for(i=2;i<N;i++){
        if(phi[i]==i){
            for(j=i;j<N;j+=i){
                phi[j]/=i;
                phi[j]*=i-1;
            }
        }
    }
     
    for(i=1;i<N;i++){
        for(j=i;j<N;j+=i){
            sum[j]=sum[j]+1LL*i*phi[j/i];
        }
    }
    for(i=1;i<N;i++) sum[i]-=i;
    ans[0]=0;
    for(i=1;i<N;i++){
        ans[i]=ans[i-1]+sum[i];
    }
}
 
inline long double power(ll a, ll b)
{
    if (b == 0)
        return 1;
    ll x = powr(a, b/2);
    if (b % 2 == 0)
        return (x*x);
    else
        return (((x*x))*a);
}
 
using namespace std;
 
int main() {
	// your code goes here
	//ios_base::sync_with_stdio(false);
	//cin.tie(0),cout.tie(0);
	register ll t,i,n,ans,test;
	test=1;
	cin>>t;
	string st,p;
    while(t--)
    {
     cin>>st;   
        p=st[0];
        for(i=1;i<st.length();i++)
        {
            if(st[i]>=p[0])
            p=st[i]+p;
            else
            p=p+st[i];
        }
        cout<<"Case #"<<test<<": "<<p<<"\n";
        test++;
    }
	return 0;
} 