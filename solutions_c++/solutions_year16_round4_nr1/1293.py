//Vanjape Rajas Mangesh

#include<bits/stdc++.h>

using namespace std;

typedef pair<int,int>   II;
typedef vector< II >      VII;
typedef vector<int>     VI;
typedef vector< VI > 	VVI;
typedef long long int 	LL;

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
	cerr << name << " : " << arg1 << std::endl;
}
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args){
	const char* comma = strchr(names + 1, ',');cerr.write(names, comma - names) << " : " << arg1<<" | ";__f(comma+1, args...);
}
#else
#define trace(...)
#endif

//FILE *fin = freopen("in","r",stdin);
//FILE *fout = freopen("out","w",stdout);

int A[3];
int B[3];
int ans[5000];
int temp[5000];
int pwi[15];
int cpi(int st,int len)
{
	for(int i=st;i<st+len;i++)
	{
		if(ans[i]>ans[i+len])
		{
			return 1;
		}
		else if(ans[i]<ans[i+len])
		{
			return 0;
		}
	}
	return 0;
}
void comp(int val,int n)
{
	SET(A,0);
	A[val]=1;
	for(int i=1;i<=n;i++)
	{
		for(int j=0;j<3;j++)
		{
			B[(j+1)%3]=A[j]+A[(j+1)%3];
		}
		for(int j=0;j<3;j++)
			A[j]=B[j];
	}
	return;
}
void func(int val,int n)
{
	ans[0]=val;
	for(int i=1;i<=n;i++)
	{
		for(int j=0;j<pwi[i-1];j++)
		{
			temp[2*j]=ans[j];
			temp[2*j+1]=(ans[j]+1)%3;
		}
		for(int j=0;j<pwi[i];j++)
			ans[j]=temp[j];
	}
	for(int i=1;i<=n;i++)
	{
		for(int j=0;j<pwi[n];j+=pwi[i])
		{
			if(cpi(j,pwi[i-1])==1)
			{
				for(int k=j;k<j+pwi[i-1];k++)
				{
					swap(ans[k],ans[k+pwi[i-1]]);
				}
			}
		}
	}
}
int main()
{
	int T;
	cin>>T;
	pwi[0]=1;
	for(int i=1;i<15;i++)
		pwi[i]=pwi[i-1]*2;
	for(int t=1;t<=T;t++)
	{
		int fl=0;
		SET(ans,-1);
		int n,p,r,s;
		cin>>n>>r>>p>>s;
		for(int i=0;i<3;i++)
		{
			comp(i,n);
			if(p==A[0]&&r==A[1]&&s==A[2])
			{
				func(i,n);
				fl=1;
				break;
			}
		}
		if(fl==0)
		{
			cout<<"Case #"<<t<<": IMPOSSIBLE\n"; 
			continue;
		}
		string str="";
		for(int i=0;i<pwi[n];i++)
		{
			if(ans[i]==0)
				str.PB('P');
			else if(ans[i]==1)
				str.PB('R');
			else
				str.PB('S');
		}
		cout<<"Case #"<<t<<": "<<str<<"\n"; 
	}
	return 0;
}
