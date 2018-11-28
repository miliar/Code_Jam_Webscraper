#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef complex<double> cplx;

#define sqr(x) ((x)*(x))
#define pb push_back
#define X first
#define Y second
#define sit(a) set<a>::iterator
#define mit(a,b) map<a,b>::iterator

const ll mod=1000000007LL;
const int maxn=100005,maxm=605;
const double eps=1e-16;
const double pi=acos(-1.0);

typedef pair<ll,ll> pa;

ll pv(ll n)
{
	ll i;
	for(i=2;i*i<=n;i++)
	{
		if(n%i==0) return i;
	}
	if(i*i>n) return -1;
}

ll vt[15];

ll cf[15][25]={0};

void solve(int n,int m)
{
	ll i;
	int mt=0,j,k;
	for(i=0;i<(1LL<<(n-2));i++)
	{
		ll it=i*2+1+(1LL<<(n-1));
		for(j=2;j<=10;j++)
		{
			ll ct=0;
			for(k=0;k<n;k++)
			{
				if(it>>k&1) ct+=cf[j][k];
			}
			vt[j]=pv(ct);
			if(vt[j]==-1) break;
		}
		if(j<=10) continue;
		++mt;
		for(j=n-1;j>=0;j--) printf("%d",int(it>>j&1));
		for(j=2;j<=10;j++) printf(" %lld",vt[j]);
		printf("\n");
		if(m==mt) break;
	}
}

int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	int T,I,i,j;
	for(i=1;i<15;i++) for(cf[i][0]=1,j=1;j<25;j++) cf[i][j]=cf[i][j-1]*i;
	scanf("%d",&T);
	for(I=1;I<=T;I++)
	{
		int n,m;
		scanf("%d %d",&n,&m);
		printf("Case #%d:\n",I);
		solve(n,m);
		cerr<<"Case #"<<I<<" done\n";
	}
	return 0;
}
