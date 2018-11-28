#include<bits/stdc++.h>
using namespace std;
#define P1 37
#define P2 47
#define mod 1000000007
#define ll long long 
#define F first
#define S second
#define maxs 70000
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
	ll t,j,k,c,s,i;
	cin>>t;
	f(j,t)
	{
		cin>>k>>c>>s;
		cout<<"Case "<<j+1<<": ";
		FOR(i,1,k+1)
		cout<<i<<" ";
		cout<<endl;
	}
}