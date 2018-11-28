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

const int MOD=1000002013,dx[]={0,1,0,-1},dy[]={1,0,-1,0};
const double eps=1e-8;

void read(int &k)
{
	k=0; char x=getchar();
	while(x<'0'||x>'9') x=getchar();
	while(x>='0'&&x<='9') { k=k*10-48+x; x=getchar(); }
}

struct arr
{
	int L,R,t;
} a[1010];

int N,m,tmp[2010],len,ans;
llint cnt[2010];

llint solve(llint x)
{
	return (2*N-x+1)*(x)/2%MOD;
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	int T,tt; scanf("%d",&T);
	for(tt=1;tt<=T;tt++)
	{
		ans=0;
		scanf("%d%d",&N,&m);
		len=0;
		for(int i=1;i<=m;i++)
		{
			scanf("%d%d%d",&a[i].L,&a[i].R,&a[i].t);
			tmp[++len]=a[i].L;
			tmp[++len]=a[i].R;
			ans=(ans+solve(a[i].R-a[i].L)*a[i].t)%MOD;
		}
		sort(tmp+1,tmp+len+1);
		len=unique(tmp+1,tmp+len+1)-tmp-1;
		memset(cnt,0,sizeof cnt);
		for(int i=1;i<=m;i++)
		{
			a[i].L=lower_bound(tmp+1,tmp+len+1,a[i].L)-tmp;
			a[i].R=lower_bound(tmp+1,tmp+len+1,a[i].R)-tmp;
			for(int j=a[i].L;j<a[i].R;j++) cnt[j]+=a[i].t;
		}
		for(int i=1,j;i<len;i++) 
			while(cnt[i])
			{
				llint cost=cnt[i];
				for(j=i+1;j<len;j++)
				{
					if (!cnt[j]) break;
					cost=min(cost,cnt[j]);
				}
				ans=((ans-solve(tmp[j]-tmp[i])*cost)%MOD+MOD)%MOD;
				for(int k=i;k<j;k++) cnt[k]-=cost;
			}
		printf("Case #%d: %d\n",tt,ans);
	}
	
	return 0;
}
