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

struct arr
{
	int x0,y0,x1,y1;
} a[1010];

int T,W,H,n,dist[1010],used[1010],b[1010][1010];

int Dist(arr x,arr y)
{
	int dx,dy;
	if (x.y0>y.y1||x.y1<y.y0) dy=min(abs(x.y0-y.y1),abs(-x.y1+y.y0))-1; else dy=0;
	if (x.x0>y.x1||x.x1<y.x0) dx=min(abs(x.x0-y.x1),abs(-x.x1+y.x0))-1; else dx=0;
	return max(dx,dy);
}

int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		scanf("%d%d%d",&W,&H,&n);
		for(int i=0;i<n;i++)
			scanf("%d%d%d%d",&a[i].x0,&a[i].y0,&a[i].x1,&a[i].y1);
		a[n++]=(arr){-1,0,-1,H-1};
		a[n++]=(arr){W,0,W,H-1};
		for(int i=0;i<n;i++)
			for(int j=i+1;j<n;j++)
				b[i][j]=b[j][i]=Dist(a[i],a[j]);
		int S=n-2;
		memset(dist,63,sizeof dist);
		memset(used,0,sizeof used);
		dist[S]=0;
		while(1)
		{
			int mi=0x3f3f3f3f,t=-1;
			for(int i=0;i<n;i++) if (!used[i]&&dist[i]<mi) mi=dist[t=i];
			if (t==-1) break;
			used[t]=1;
			for(int i=0;i<n;i++) if (!used[i]&&dist[i]>dist[t]+b[t][i]) dist[i]=dist[t]+b[t][i];
		}
		printf("Case #%d: %d\n",tt,dist[n-1]);
	}
	
	return 0;
}
