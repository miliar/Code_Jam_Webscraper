#include<bits/stdc++.h>
#define NINF INT_MIN 
#define INF INT_MAX
#define ull unsigned long long
#define ld long double
#define ll long long
#define M 1000000009
#define REM 4
#define N 100005
#define pll pair<ll,ll>
#define pb(x) push_back(x)
#define mset(a) memset(a,0,sizeof(a))
#define sc(x)  scanf("%c",&x)
#define si(a)  scanf("%d",&a)
#define sl(a) scanf("%lld",&a)
#define f(i,n) for(i=0;i<n;i++)
#define foi(i,j,k) for(i=j;i<k;i++)
#define mll map<ll,ll>
#define foe(i,j,k) for(i=j;i<=k;i++)
 
#define dbg(x) cout<<#x<<"="<<x<<endl;
using namespace std;



int main()
{
    ll t,i,k,l,j,ans;
    i=0;
    sl(t);
    string s;

    while(i<t)
    {
      cin>>s;
      ans=0;
      l=s.length();
      if(l>1)
      {
      	for(j=1;j<l;j++)
      {
      	if(s[j-1]=='+' && s[j]=='-')
      	ans++;
      	
      }
      if(s[0]=='+')ans=ans*2;
      else ans=ans*2+1;
      	
      }
      else
      {
      	if(s[0]=='-')ans++;
      }
      
      
      cout<<"Case #"<<i+1<<": "<<ans<<endl;
      i++;

    }
    return 0;
}
