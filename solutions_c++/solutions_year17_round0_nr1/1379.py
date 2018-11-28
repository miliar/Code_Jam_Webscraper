#include<bits/stdc++.h>
#define	    ll		    long long int
#define     D               double
#define     LD              long double
#define     max(a,b)	    ((a)>(b)?(a):(b))
#define     min(a,b)	    ((a)<(b)?(a):(b))
#define     mp              make_pair
#define     vi              vector<ll>
#define     pb              push_back
#define     s               second
#define     f               first
#define     mod             1000000007
using namespace std;
inline ll getn(){
	ll n=0, c=getchar();
	while(c < '0' || c > '9')
		c = getchar();
	while(c >= '0' && c <= '9')
		n = (n<<3) + (n<<1) + c - '0', c = getchar();
	return n;
}


int main()
{
	//	std::ios_base::sync_with_stdio(0);
	ll t,n,j,i,p,k,l,ji;
	FILE *wfile;
	
	cin>>t;
//	string str,str1;
	wfile=fopen("output1.txt","w");
	ji=0;
	string str,str1;
	ll dp[1005];
	ll arr[1005];
while(t--)
{
	ji++;
	cin>>str;
	cin>>k;
	ll ans=0;
	n=str.size();
	memset(dp,0,sizeof(dp));
	memset(arr,0,sizeof(arr));
	for(i=0;i<n;i++)
	{
		if(str[i]=='-')
			dp[i+1]=1;
	}
	for(i=1;i<=n;i++)
	{
		arr[i]+=arr[i-1];
		dp[i]+=arr[i];
		if(dp[i]%2)
		{
			if(i>n-k+1)
				break;
			arr[i]++;
			arr[i+k]--;
			ans++;
		}
	}




	fprintf(wfile,"Case #%lld: ",ji);
if(i==n+1)
fprintf(wfile,"%lld",ans);
else
fprintf(wfile,"IMPOSSIBLE");
	fprintf(wfile,"\n");
}
	
	return 0;
}
