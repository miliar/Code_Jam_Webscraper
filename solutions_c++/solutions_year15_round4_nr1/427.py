#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<string>
#include<map>
#include<cmath>
#include<iostream>
#include<vector>
#include<ctime>
#include<algorithm>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> per;
#define mp(x,y) make_pair(x,y)
inline int readT(){
    int ret = 0; char c;
    while(c = getchar(), c < '0' || c > '9') ; ret = c - 48;
    while(c = getchar(), c >= '0' && c <= '9') ret = ret * 10 + c - 48;
    return ret;
}
const int MOD = 1000000007;
const int INF = 1000000007;
const int M = 100005;
const int N = 105;
char s[N][N];
int c[4][2]={1,0,0,1,-1,0,0,-1};
int h[200];
bool u[4];
int main()
{
	//ios_base::sync_with_stdio(0);
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,ca=1;
	scanf("%d",&T);
	h['v']=0;
	h['>']=1;
	h['^']=2;
	h['<']=3;
	while(T--)
	{
		printf("Case #%d: ",ca++);
		int n,m,ret=0;
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++)scanf("%s",s[i]);
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)if(s[i][j]!='.')
			{
				int t=h[s[i][j]],g=0;
				for(int k=0;k<4;k++)
				{
					int x=i+c[k][0],y=j+c[k][1],f=0;
					while(x>=0&&y>=0&&x<n&&y<m)
					{
						if(s[x][y]!='.'){f=1;break;}
						x+=c[k][0];
						y+=c[k][1];
					}
					u[k]=f;
					if(f)g=1;
				}
			//	printf("t:%d u:%d \n",t,u[t]);
				if(!u[t])ret++;
				if(!g)ret=-INF;
			}
		}
		if(ret<0)puts("IMPOSSIBLE");
		else printf("%d\n",ret);
	}
    return 0;
}




















