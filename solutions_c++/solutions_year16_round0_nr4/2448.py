#include<bits/stdc++.h>
#define	    ll		    long long int
#define     D               double
#define     LD              long double
#define     max(a,b)	    ((a)>(b)?(a):(b))
#define     min(a,b)	    ((a)<(b)?(a):(b))
#define     mp              make_pair
#define     vi              vector<ll>
#define     pb              push_back
//#define     s               second
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
	ll t,n,i,j,p,k,c,s;
	FILE * wfile;
	cin>>t;
	j=0;
	wfile=fopen("output4.txt","w");
//	set<ll> kl;
while(t--)
{
//	cin>>n;
//	kl.clear();
	j++;
	fprintf(wfile,"Case #%lld: ",j);
	cin>>k>>c>>s;
	
	for(i=0;i<s;i++)
	{
		fprintf(wfile,"%lld ",i+1);
	}
	fprintf(wfile,"\n");
}
fclose(wfile);
	
	return 0;
}
