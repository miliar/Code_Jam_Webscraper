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
#define pp pair<ll,ll> 
int main()
{
	//	std::ios_base::sync_with_stdio(0);
	ll t,n,j,i,a,b;
	FILE *wfile;
	
	cin>>t;
//	string str,str1;
	wfile=fopen("output2.txt","w");
	j=0;
	ll sum,l,r;
while(t--)
{
	priority_queue<pp>q;
	j++;
	fprintf(wfile,"Case #%lld: ",j);
	cin>>n;
	pp pi;
	sum=0;
	for(i=0;i<n;i++)
	{
		cin>>l;
		q.push(mp(l,i));
		sum+=l;
	}
///	cout<<sum<<endl;
	char ch;
	while(!q.empty())
	{
		
		pi=q.top();
		q.pop();
		l=pi.first;
		r=pi.second;
		n=q.size();
	//	cout<<n<<endl;
		if(n==0)
		{
			for(i=0;i<l;i++)
			{
				ch=char(r+'A');
				fprintf(wfile,"%c",ch);
			//	cout<<ch;
			}
		//	cout<<" ";
			fprintf(wfile," ");
			break;
		}
		if(sum&1)
		{
			ch=char(r+'A');
			fprintf(wfile,"%c",ch);
			if(l>1)
			q.push(mp(l-1,r));
			fprintf(wfile," ");
			sum--;
			
		}
		else if(l>(sum/2))
		{
			ch=char(r+'A');
			fprintf(wfile,"%c",ch);
		//	cout<<ch;
			fprintf(wfile,"%c",ch);
		//	cout<<ch;
			fprintf(wfile," ");
			if(l>2)
			q.push(mp(l-2,r));
			sum-=2;
		}
		else
		{
			ch=char(r+'A');
			fprintf(wfile,"%c",ch);
	//	cout<<ch;
		//	fprintf(wfile," ");
			
			sum-=1;
			pi=q.top();
		q.pop();
		a=pi.first;
		b=pi.second;
			ch=char(b+'A');
			fprintf(wfile,"%c",ch);
	//	cout<<ch;
			fprintf(wfile," ");
			if(l>1)
			q.push(mp(l-1,r));
			if(a>1)
			q.push(mp(a-1,b));
			sum-=1;
		}
	//	cout<<" ";
	}
	fprintf(wfile,"\n");
//cout<<endl;
	
}
	
	return 0;
}
