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

int T,P,Q,n,h[110],g[110],f[110][2010];

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		scanf("%d%d%d",&P,&Q,&n);
		for(int i=0;i<n;i++)
			scanf("%d%d",&h[i],&g[i]);
		memset(f,-1,sizeof f);
		f[0][1]=0;
		for(int i=0;i<n;i++)
		{
			int tower=(h[i]-1)/Q;
			int me=h[i]-Q*tower;
			if (me%P==0) me=me/P; else me=me/P+1;
			int tn;
			if (h[i]%Q==0) tn=h[i]/Q; else tn=h[i]/Q+1;
			for(int j=0;j<=2001;j++) if (f[i][j]>=0)
			{
				int nj=j-me+tower;
				if (nj>=0)
					f[i+1][nj]=max(f[i+1][nj],f[i][j]+g[i]);
				f[i+1][j+tn]=max(f[i+1][j+tn],f[i][j]);
			}
		}
		int ans=0;
		for(int i=0;i<=2001;i++) if (f[n][i]>ans) ans=f[n][i];
		printf("Case #%d: %d\n",tt,ans);
	}
	
	return 0;
}
