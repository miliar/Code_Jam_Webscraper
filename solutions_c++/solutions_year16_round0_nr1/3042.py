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
	ll t,n,i,j,p;
	FILE * wfile;
	cin>>t;
	j=0;
	wfile=fopen("output1.txt","w");
	set<ll> kl;
while(t--)
{
	cin>>n;
	kl.clear();
	j++;
	fprintf(wfile,"Case #%lld: ",j);
	if(n==0)
	{
		fprintf(wfile,"INSOMNIA\n");
	}
	else
	{
		i=1;
		
		while(1)
		{
			p=i*n;
		//	cout<<p<<endl;
			while(p)
			{
			kl.insert(p%10);
			p/=10;	
			}
			if(kl.size()==10)
				break;
				i++;
		}
		i=i*n;
		fprintf(wfile,"%lld\n",i);
		
	}

	
}
fclose(wfile);
	
	return 0;
}
