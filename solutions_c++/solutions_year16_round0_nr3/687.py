//Snorlax//
#include<bits/stdc++.h>

using namespace std;

typedef pair<int,int> II;
typedef vector<II> VII;
typedef vector<int> VI;
typedef vector< VI > VVI;
typedef long long int LL;

#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SZ(a) (int)(a.size())
#define ALL(a) a.begin(),a.end()
#define SET(a,b) memset(a,b,sizeof(a))

#define si(n) scanf("%d",&n)
#define dout(n) printf("%d\n",n)
#define sll(n) scanf("%lld",&n)
#define lldout(n) printf("%lld\n",n)
#define fast_io ios_base::sync_with_stdio(false);cin.tie(NULL)

#define TRACE

#ifdef TRACE
#define trace(...) __f(#__VA_ARGS__, __VA_ARGS__)
template <typename Arg1>
void __f(const char* name, Arg1&& arg1){
	cerr<<name<<" : "<<arg1<<endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names,Arg1&& arg1,Args&&... args){
	const char* comma=strchr(names+1,',');
	cerr.write(names,comma-names)<<" : "<<arg1<<" | ";__f(comma+1,args...);
}
#else
#define trace(...)
#endif

//FILE *fin = freopen("in","r",stdin);
//FILE *fout = freopen("out","w",stdout);
const int N=1111113;
int p[N];
vector<int> prime;
int F[12];
inline void sieve()
{
	int i,j;
	for(i=2;i*i<=N-2;i++)
		if(!p[i])
			for(j=i*i;j<=N-2;j+=i)
				p[j]=i;
	for(i=2;i<=N-2;i++)
		if(!p[i])
			prime.PB(i);
//	trace("dne");
}
int fact(LL v)
{
	if(v<(N-2)){
		if(p[v]) return p[v];
		else return 0;
	}
	for(auto pm:prime)
		if(!(v%pm) && v!=pm)
			return pm;
	return 0;
}
int check(LL v,int b)
{
	LL ans=0,d=1;
	//trace(v,b);
	while(v!=0)
	{
		if(v&1)
			ans+=d;
		d*=b;
		v>>=1;
	}
	//trace(v,b);
	if((F[b]=fact(ans)))
		return 1;
	return 0;
}
int nn,k;
char ans[35];
void gen(int flag)
{
	int i,j,b=(1<<(nn));
	int cnt=0;
	for(i=(1<<(nn-1))+1;i<b;i+=2)
	{
		bool ok=true;
		for(j=2;j<=10;j++)
		{
			if(!check(i,j)){
				ok=false;
				break;
			}
		}
		int ii=i;
		if(ok)
		{
			cnt++;
			ans[nn]='\0';
			int j=nn-1;
			while(ii){
				ans[j--]='0'+(ii&1);
				ii>>=1;
				//trace(ii,j);
			}
				printf("%s",ans);
			if(flag)
				printf("%s",ans);
			for(int kj=2;kj<=10;kj++)
				printf(" %d",F[kj]);
			printf("\n");
		}
		if(cnt==k)
			break;
	}
}
int main()
{
	int n;
	si(n);si(n);si(k);
	nn=min(16,n);
	sieve();
	printf("Case #1: \n");
	if(n==16)
		gen(0);
	else
		gen(1);
	return 0;
}


