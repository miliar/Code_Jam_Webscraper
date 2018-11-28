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
const int maxn=100005,maxm=55;
const double eps=1e-10;
const double pi=acos(-1.0);

int T,n;
struct pa
{
	int a[maxm];
	pa(){memset(a,0,sizeof(a));}
	void print(){int i;for(i=0;i<n;i++) cerr<<a[i]<<" ";cerr<<endl;}
} a[maxm*10],b[maxm];

int r[maxm];
int x[maxm],y[maxm];
bool v[maxm*10];
int rt[maxm][maxm];
int re=-1;

bool operator <(pa a,pa b)
{
	int i;
	for(i=0;i<n;i++) if(a.a[i]!=b.a[i]) return a.a[i]<b.a[i];
	return 0;
}
bool cmp(pa a,pa b)
{
	int i;
	for(i=0;i<n;i++) if(a.a[i]>=b.a[i]) return 0;
	return 1;
}
bool eq(pa a,pa b)
{
	int i;
	for(i=0;i<n;i++) if(a.a[i]!=b.a[i]) return 0;
	return 1;
}

void dfs(int dpt,int cur)
{
	if(re>=0) return;
	int i,j;
	if(dpt==n)
	{
		for(i=0;i<n;i++) for(j=0;j<n;j++) rt[i][j]=a[x[i]].a[j];
		for(i=0;i<n;i++) for(j=0;j<n;j++) b[i].a[j]=rt[j][i];
		for(i=0;i<n-1;i++) if(!cmp(b[i],b[i+1])) return;
		memset(v,0,sizeof(v));for(i=0;i<n;i++) v[x[i]]=1;
		int yn=0;
		for(i=0;i<2*n-1;i++) if(!v[i]) y[yn++]=i;
		for(i=0;i<n;i++)
		{
			for(j=0;j<n-1;j++)
			{
				if(!eq(a[y[j]],b[j+(j>=i)])) break;
			}
			if(j>=n-1)
			{
				re=i;
				for(j=0;j<n;j++) printf("%d%c",b[i].a[j],j==n-1?'\n':' ');
				return;
			}
		}
		return;
	}
	for(i=cur;i<2*n-1;i++)
	{
		x[dpt]=i;
		if(dpt==0&&i>=2) return;
		if(dpt==0||cmp(a[x[dpt-1]],a[i])) dfs(dpt+1,i+1);
	}
}

int main()
{
        freopen("in.txt","r",stdin);
        freopen("out.txt","w",stdout);
	int I,i,j,k;
	scanf("%d",&T);
	for(I=1;I<=T;I++)
	{
		re=-1;
		printf("Case #%d: ",I);
		scanf("%d",&n);
		for(i=0;i<2*n-1;i++) for(j=0;j<n;j++) scanf("%d",&a[i].a[j]);
		sort(a,a+2*n-1);dfs(0,0);
	}
        return 0;
}
