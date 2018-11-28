/*
	Author : ChnLich
*/
#include<cstdio>
#include<cmath>
#include<iomanip>
#include<cstring>
#include<cstdlib>
#include<ctime>
#include<iostream>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<deque>
#include<set>
#include<map>
#include<string>
#include<bitset>
#include<functional>
#include<utility>

using namespace std;

typedef long long llint;
typedef pair<int,int> ipair;
typedef unsigned int uint;
#define pb push_back
#define fi first
#define se second
#define mp make_pair

const int MOD=1000000007,dx[]={0,1,0,-1},dy[]={1,0,-1,0};
const double eps=1e-8;

void read(int &k)
{
	k=0; char x=getchar();
	while(x<'0'||x>'9') x=getchar();
	while(x>='0'&&x<='9') { k=k*10-48+x; x=getchar(); }
}

double ans;
llint m,a[40],use,las,b[40];
int n,can;

void update(llint x,llint*a,llint t)
{
	if (x<=0) return;
	int tot=0;
	llint cost=0;
	double ret=0;
	llint can=37-n;
	for(int i=1;i<=n;i++) if (a[i]<=x) can++;
	for(int i=1;i<=n;i++) if (a[i]<=x)
	{
		tot++;
		ret+=1.0/can*(x-a[i])*36;
		cost+=x-a[i];
	}
	ret+=(can-tot)/double(can)*x*36;
	ret-=cost+(can-tot)*x;
	ret-=t;
	if (ret>ans) ans=ret;
//	cerr<<x<<' '<<ret<<endl;
}

void solve(llint x)
{
	llint mo=m;
	for(int i=1;i<=n;i++) if (a[i]<=x) mo-=x-a[i];
	mo-=(37-n)*x;
	if (mo<0) return;
	memcpy(b,a,sizeof b);
	update(x,b,0);
	llint cnt=0;
	for(int i=n;i;i--) if (a[i]<=x)
	{
		if (mo>0)
		{
			mo--; b[i]=x+1; cnt+=x-a[i]+1;
			update(x,b,cnt);
		} else break;
	}
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	int T;
	cin>>T;
	for(int tt=1;tt<=T;tt++)
	{
		ans=0;
		cin>>m>>n;
		for(int i=1;i<=n;i++) cin>>a[i]; a[n+1]=1ll<<50;
		sort(a+1,a+n+1);
		can=37-n;
		use=0,las=0;
		for(int i=1;i<=n+1;i++) if (i==1||a[i]>a[i-1])
		{
			if ((a[i]-1-las)*can+use<=m)
			{
				for(int j=1;j<=40;j++)
					solve(a[i]-j);
				use+=(a[i]-las)*can;
				las=a[i];
				can++;
			} else if (use<=m)
			{
				llint hig=(m-use)/can;
				for(int j=0;j<=40;j++)
					solve(las+hig-j);
				break;
			}
			//if (use<=m) solve(a[i]);
		} else can++;
		printf("Case #%d: %.12lf\n",tt,ans);
	}
	
	return 0;
}
