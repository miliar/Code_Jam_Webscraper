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
 
int main()
{
	ll start,count,i,j,len,t;
	string str;
	cin>>t;
	f(j,t)
	{
		start=0;count=0;
		cin>>str;
		ll len=str.length();
		if(str[0]=='-')
			count++;
		FOR(i,1,len)
		{
			if(str[i]=='-' && str[i-1]=='+')
				 count++;
		}
		ll ans;
		if(str[0]=='+')
		 ans=(count)*2;
	    else
	    	ans=(count-1)*2+1;

		 
			 
		cout<<"case #"<<j+1<<": "<<ans<<endl;
	}
}