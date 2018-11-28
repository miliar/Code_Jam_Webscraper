#include <bits/stdc++.h>
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
const int inf=0x3f3f3f3f;
const int maxn=100005,maxm=1005;
const double eps=1e-10;
const double pi=acos(-1.0);

int T;
int a[maxm],n;
vector<int> E[maxm];

int x[maxn],r,fl,y[maxn];

void dfs(int dpt,int cur)
{
	int i,j;
	if(fl) return;
	if(dpt==r)
	{
		for(i=0;i<r;i++) y[i]=x[i];
		do
		{
			for(i=0;i<r;i++)
			{
				if(a[y[i]]==y[(i+1)%r]||a[y[i]]==y[(i+r-1)%r]) continue;
				else break;
			}
			if(i>=r) {fl=1;return;}
		}while(next_permutation(y,y+r));
		return;
	}
	for(i=cur;i<n;i++)
	{
		x[dpt]=i;dfs(dpt+1,i+1);
	}
}

void solve()
{
	r=n;fl=0;
	int i,j,k;
	while(r>1)
	{
		dfs(0,0);
		if(fl) {printf("%d\n",r);return;}
		--r;
	}
	printf("1\n");
}

int main()
{
        freopen("in.txt","r",stdin);
        freopen("out.txt","w",stdout);
	scanf("%d",&T);
	int i,j;
	for(int I=1;I<=T;I++)
	{
		scanf("%d",&n);
		printf("Case #%d: ",I);
		for(i=0;i<n;i++) E[i].clear();
		for(i=0;i<n;i++) scanf("%d",a+i),--a[i],E[i].pb(a[i]),E[a[i]].pb(i);
		solve();cerr<<I<<endl;
	}
        return 0;
}
