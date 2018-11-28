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

void solve(int k,int c,int s)
{
	int i,j;
	for(i=0;i<k;i++) printf(" %d",i+1);
	printf("\n");
}

int k,c,s;

int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	int T,I,i,j;
	scanf("%d",&T);
	for(I=1;I<=T;I++)
	{
		int k,c,s;
		scanf("%d %d %d",&k,&c,&s);
		printf("Case #%d:",I);
		solve(k,c,s);
		cerr<<"Case #"<<I<<" done\n";
	}
	return 0;
}
