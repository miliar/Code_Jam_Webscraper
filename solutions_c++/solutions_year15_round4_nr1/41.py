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

int T,n,m,ans[110][110][4],tra[128];
char s[110][110];

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	scanf("%d",&T);
	tra['>']=0;
	tra['v']=1;
	tra['<']=2;
	tra['^']=3;
	for(int tt=1;tt<=T;tt++)
	{
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++) scanf("%s",s[i]);
		bool flag=1;
		int cnt=0;
		memset(ans,0,sizeof ans);
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++) if (s[i][j]!='.')
			{
				int tmp=0;
				for(int dir=0;dir<4;dir++)
				{
					int tx=i,ty=j;
					while(1)
					{
						tx+=dx[dir];
						ty+=dy[dir];
						if (tx<0||tx>=n||ty<0||ty>=m)
							break;
						else if (s[tx][ty]!='.')
						{
							ans[i][j][dir]=1;
							//printf("%d %d %d\n",i,j,dir);
							tmp=1;
							break;
						}
					}
				}
				if (ans[i][j][tra[s[i][j]]]==1)
					continue;
				else if (tmp)
					cnt++;
				else
					flag=0;
			}
		printf("Case #%d: ",tt);
		if (!flag)
			puts("IMPOSSIBLE");
		else
			printf("%d\n",cnt);
	}
	
	return 0;
}
