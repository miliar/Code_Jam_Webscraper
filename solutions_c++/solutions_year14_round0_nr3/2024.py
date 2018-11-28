#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

struct Direct{int x,y;};
Direct w[9];
int T,r,c,n,cnt;
char a[51][51];
bool Find,bj[51][51];

bool check(int x,int y)
{
	for (int i=1;i<=8;++i)
	{
		int xx=x+w[i].x;
		int yy=y+w[i].y;
		if ((xx<=0)||(yy<=0)||(xx>r)||(yy>c))  continue;
		if (a[xx][yy]!='.') return 0;
	}
	return 1;
}

void ff(int x,int y)
{
	if (bj[x][y]) return;
	bj[x][y]=1;
	++cnt;
	if (check(x,y))
	{
		for (int i=1;i<=8;++i)
		{
			int xx=x+w[i].x;
			int yy=y+w[i].y;
			if ((xx<=0)||(yy<=0)||(xx>r)||(yy>c))  continue;
			if (a[xx][yy]=='.') ff(xx,yy);
		}
	}
}

void dfs(int x,int y,int z)
{
	if (r*c-((x-1)*c+y-1)<z) return;
	if (x>r)
	{
		for (int i=1;i<=r;++i)
		{
			for (int j=1;j<=c;++j)
			{
				if (a[i][j]=='.')
				{
					memset(bj,0,sizeof(bj));
					cnt=0;
					ff(i,j);
					if (cnt==r*c-n)
					{
						Find=1;
						a[i][j]='c';
						break;
					}
				}
			}
			if (Find) break;
		}
		return;
	}
	a[x][y]='.';
	if (y==c) dfs(x+1,1,z); else dfs(x,y+1,z);
	if (Find) return;
	a[x][y]='*';
	if (y==c) dfs(x+1,1,z-1); else dfs(x,y+1,z-1);
}

int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	w[1].x=1;w[1].y=0;
	w[2].x=1;w[2].y=1;
	w[3].x=1;w[3].y=-1;
	w[4].x=0;w[4].y=-1;
	w[5].x=0;w[5].y=1;
	w[6].x=-1;w[6].y=0;
	w[7].x=-1;w[7].y=1;
	w[8].x=-1;w[8].y=-1;
	scanf("%d",&T);
	int TT=0;
	while (TT<T)
	{
		++TT;
		scanf("%d%d%d",&r,&c,&n);
		Find=0;
		dfs(1,1,n);
		printf("Case #%d:\n",TT);
		if (!Find) printf("Impossible\n"); else
		{
			for (int i=1;i<=r;++i)
			{
				for (int j=1;j<=c;++j)
				{
					printf("%c",a[i][j]);
				}
				printf("\n");
			}
		}
	}
	return 0;
}