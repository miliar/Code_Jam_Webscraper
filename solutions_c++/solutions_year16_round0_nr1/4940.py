#include<bits/stdc++.h>
using namespace std;
#define P1 37
#define P2 47
#define mod 1000000007
#define ll long long 
#define F first
#define S second
#define maxs 100009
#define INF INT_MIN
#define dbg(x) cout<<#x<<"="<<x<<endl
#define sc scanf
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define f(i,n) for(i=0;i<n;i++)
#define FOR(i,j,n) for(i=j;i<n;i++)
 
map<ll,bool>m;
int main()
{
	ll t,n,k,y,r,i,con,j;
	cin>>t;
	f(j,t)
	{
		y=0;

		cin>>n;
		if(n==0)
		{
			cout<<"case #"<<j+1<<": "<<"INSOMNIA\n";
		}
		else
		{
			i=1;
			while(1)
			{
				con=k=(i++)*n;
				while(k!=0)
				{
				 r=k%10;
				 m[r]=1;
				 //dbg(m.size());
				 k/=10;
				 if(m.size()==10)
				 {
				 	y=1;break;
				 }
				}
				if(y)break;
			}
			cout<<"case #"<<j+1<<": "<<con<<endl;
		}
		m.clear();
	}
} 

 