#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define F(i,a,b) for(ll i=a;i<=b;i++)
#define ITR(x,c) for(__typeof(c.begin()) x=c.begin();x!=c.end();x++)
#define ALL(a) (a.begin()),(a.end())
#define ZERO(a) memset(a,0,sizeof(a))
#define mp make_pair
#define pb push_back 
#define X first
#define Y second
#define pi 3.14159265
#define MOD 1000000007   

ll n,m;		 //(-1,-1) itself responsible for overflow, (0,0)->no overflow 
string s[110];		
ll nb[110][110][4];
int main(){
	
	cin.sync_with_stdio(0);
	
	ll t;
	
	cin>>t;
	
	F(k,1,t)
	{
		cin>>n>>m;
				
		//0-left
		//1-right
		//2-up
		//3-down
	
		F(i,0,n-1)
		{
			cin>>s[i];
		}
		
		F(i,0,n-1)
		{	
			ll prev=-1;
			
			F(j,0,m-1)
			{
				nb[i][j][0]=prev;
				if(s[i][j]!='.')
				prev=j;
			}
		}
		
		F(i,0,n-1)
		{	
			ll prev=-1;
			
			for(ll j=m-1;j>=0;j--)
			{
				nb[i][j][1]=prev;
				if(s[i][j]!='.')
				prev=j;
			}
		}
		
		F(j,0,m-1)
		{	
			ll prev=-1;
			
			F(i,0,n-1)
			{
				nb[i][j][2]=prev;
				if(s[i][j]!='.')
				prev=i;
			}
			
		}
		
		F(j,0,m-1)
		{	
			ll prev=-1;
			
			for(ll i=n-1;i>=0;i--)
			{
				nb[i][j][3]=prev;
				if(s[i][j]!='.')
				prev=i;
			}
			
		}
		
		ll ans=0;
		
		F(i,0,n-1)
		F(j,0,m-1)
		if(s[i][j]!='.')
		{
			if(s[i][j]=='<' && nb[i][j][0]==-1)
			ans++;
			
			if(s[i][j]=='>' && nb[i][j][1]==-1)
			ans++;
			
			if(s[i][j]=='^' && nb[i][j][2]==-1)
			ans++;
			
			if(s[i][j]=='v' && nb[i][j][3]==-1)
			ans++;
		}
		
		bool imp=false;
		
		F(i,0,n-1)
		F(j,0,m-1)
		if(s[i][j]!='.')
		{
			ll cn=0;
			
			F(h,0,3)
			if(nb[i][j][h]==-1)
			cn++;
			
			if(cn==4)
			{
				imp=true;
				break;
			}
			
		}
		
		if(imp==false)
		cout<<"Case #"<<k<<": "<<ans<<"\n";
		
		else cout<<"Case #"<<k<<": "<<"IMPOSSIBLE"<<"\n";
	}
	
	return 0;
}
