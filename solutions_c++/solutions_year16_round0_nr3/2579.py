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
#define MOD 1000000009
#define MAX 100000050
#define LMT 10004
#define LEN 5761457
using namespace std;
 ll findi(ll p,string str)
 {
 	ll n,i,val=0;
 	n=str.size();
 	
 	for(i=0;i<n;i++)
 	{
 		val=val*p+(str[i]-'0');
	}
	return val;
 }
 
  bool arr[MAX];
  ll prime[LEN];
void sieve()
{
	 ll i,j,k;
	for( i=3;i<=LMT;i+=2)
	{
	
		if(!arr[i])
		{
	
      		for( j=i*i,k=i*2; j<MAX; j+=k)
      		{
      
				arr[j]=i;
			}
		}
	}
		ll l=1;
	prime[0] = 2;
	for( i=3;i<=MAX;i=i+2)
	{
	
		if(!arr[i])
		{
	
       		prime[l++] = i;
       	//	if(i<30)
       	//	cout<<i<<"  ";
   		}
	}
 //cout<<endl;
		
}
ll pri(ll m)
{
	if(m<4)
	return 0;
	ll i,l;
	for(i=0;i<LEN;i++)
	{
		
		l=prime[i];
		l*=l;
	//	cout<<prime[i]<<"  "<<l<<endl;
		
		if(l>m)
		return 0; 
		else if(m%prime[i]==0)
		{
			
		return prime[i];
		}
	}
}
 
int main()
{
	//	std::ios_base::sync_with_stdio(0);
	sieve();
	ll t,n,i,j,ans,p,q,m,k;
		FILE * wfile;
	cin>>t;
	j=0;
	wfile=fopen("output3.txt","w");
	string str;
	char str1[100];
	ll val[11];
while(t--)
{
	
	cin>>n>>m;
	
	j++;
	fprintf(wfile,"Case #%lld: \n",j);
	p=n-2;
	
	for(i=0;i<(1<<p);i++)
	{
		str="1";
		for(k=p-1;k>=0;k--)
		{
			if(i& ( 1<<k ))
			{
				str+="1";
			}
			else
			str+="0";
		}
		str+="1";
		//cout<<str<<endl;
		q=1;
		for(k=2;k<=10;k++)
		{
			val[k]=findi(k,str);
		//	cout<<val[k]<<" ";
			val[k]=pri(val[k]);
		//	cout<<val[k]<<endl;
			if(!val[k])
			{
				q=0;
				break;
			}
		}
		//	cout<<endl;
		if(q && m)
		{
			//cout<<str<<endl;
			for(k=0;k<str.size();k++)
			str1[k]=str[k];
			str1[k]='\0';
			fprintf(wfile,"%s ",str1);
			for(k=2;k<=10;k++)
			{
				fprintf(wfile,"%lld ",val[k]);
			}
			fprintf(wfile,"\n");
			m--;
		}
	}

}
 	fclose(wfile);
	
	return 0;
}
