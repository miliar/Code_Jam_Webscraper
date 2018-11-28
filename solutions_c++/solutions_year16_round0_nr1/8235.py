/*input
5
0
1
2
1023456789
1692
*/
#include <bits/stdc++.h>
using namespace std;
 
#define boost  ios_base::sync_with_stdio(false);
#define endl '\n'
#define mp make_pair
#define pb push_back
#define ppb pop_back
#define fi first
#define se second
#define ll long long
#define ull unsigned long long
#define pii pair<ll, ll>
#define f(i,a,b) for(ll i = (ll)(a); i <= (ll)(b); i++)
#define rf(i,a,b) for(ll i = (ll)(a); i >= (ll)(b); i--)
#define ms(a,b) memset((a),(b),sizeof(a))
#define max(a,b) ((a>b)?(a):(b))
#define min(a,b) ((a<b)?(a):(b))
 
#define abs(x) ((x<0)?(-(x)):(x))
#define MAX 100005
#define inf LLONG_MAX
#define MIN INT_MIN
 
//typedef
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;
 
int mod = 1e9 + 7 ;
ll gcd(ll a , ll b){return b==0?a:gcd(b,a%b);}
ll powmod(ll a,ll b) {ll res=1;if(a>=mod)a%=mod;for(;b;b>>=1){if(b&1)res=res*a;if(res>=mod)res%=mod;a=a*a;if(a>=mod)a%=mod;}return res;}
 
/*..................................................................................................................................*/
int main() 
{
    //ios_base::sync_with_stdio(false);cin.tie(0);
    freopen("input.in","r",stdin);
    int t;cin>>t;int x;x=t;
    ll n;ll temp,ans,temp1;
    while(t--)
    {
      set<int>s;
    cin>>n;
    temp=n;
    freopen("output.txt","a",stdout);
    if(n==0){cout<<"Case #"<<x-t<<": INSOMNIA"<<endl;}
    else
    {      ll i=2;
      while(temp>0)
      {
        s.insert(temp%10);
        temp/=10;
      }
      if(s.size()==10)ans=n;
      else
      {
       while(1)
        {
          temp=n*i;
          temp1=temp;
          while(temp>0)
          {
            s.insert(temp%10);
            temp/=10;
          }
          if(s.size()==10){ans=temp1;break;}
          i++;
        }
      }
      cout<<"Case #"<<x-t<<": "<<ans<<endl;
    }
    fclose(stdout);
}
 fclose(stdin);
    return 0;
}



