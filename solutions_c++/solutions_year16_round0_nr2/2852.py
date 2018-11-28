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

char c[maxn];
int n;

ll dp(int m,int sgn)
{
	while(m>0&&c[m-1]==(sgn==0?'+':'-')) --m;
	if(m<=0) return 0;
	return 1+dp(m,1-sgn);
}

void solve()
{
	printf("%lld\n",dp(n,0));
}

int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	int T,I,i,j;
	scanf("%d",&T);
	for(I=1;I<=T;I++)
	{
		scanf("%s",c);n=strlen(c);
		printf("Case #%d: ",I);
		solve();
		cerr<<"Case #"<<I<<" done\n";
	}
	return 0;
}
