#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<ll>vll;
typedef pair<ll,ll> pll;
#define xx first
#define yy second
#define rep(n) for(i=0;i<n;i++)
#define pb push_back
#define mp make_pair
#define clr(a) memset(a, 0, sizeof a)
#define reset(a) memset(a, -1, sizeof a)
#define Clr(a) fill(a.begin(),a.end(),0)
#define Reset(a) fill(a.begin(),a.end(),-1)  
#define tr(c, it) \
  for(typeof(c.begin()) it=c.begin(); it!=c.end(); it++)  
  void debug(vector<ll> v)
{
    for(int i=0;i<v.size();i++)
        cout<<v[i]<<" ";
    cout<<"\n";
    // call debug({i,j,k})
}
int main()
{
    ll t,z,i,j,k,n,m,p,q,r,s,ans;
    scanf("%lld",&t);
    for(z=1;z<=t;z++)
    {
        char str[110];
        char prev=0;
        ans=0;
        cin>>str;
        for(i=0;str[i];i++)
        {
        	if(str[i]=='-'&&prev=='+')
        	{
        		ans+=2;
        	}
        	else if(str[i]=='-'&&prev==0) ans++;
        	prev=str[i];
        }
        printf("Case #%lld: %lld\n",z,ans);          
    }	
    return 0;
} 