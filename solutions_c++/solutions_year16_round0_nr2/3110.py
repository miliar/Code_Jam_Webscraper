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
	ll t,n,i,j,ans,p,q;
		FILE * wfile;
	cin>>t;
	j=0;
	wfile=fopen("output2.txt","w");
	char str[500];
while(t--)
{
	scanf("%s",str);
	n=strlen(str);
	
	j++;
	fprintf(wfile,"Case #%lld: ",j);
	ans=0;
	p=0;
	if(str[p]=='-')
	ans=1;
	
	while(p<n)
	{
		if(str[p]=='+')
		break;
		p++;
	}
	q=0;
	
	while(p<n)
	{
		if(q==0)
		{
		
		while(p<n && str[p]=='+')
			p++;
		
		}
		else
		{
			ans+=2;
			while(p<n && str[p]=='-')
			p++;
			
		}
		q=1-q;
	}
	fprintf(wfile,"%lld\n",ans);
//	cout<<ans<<endl;
	
}
 	fclose(wfile);
	
	return 0;
}
