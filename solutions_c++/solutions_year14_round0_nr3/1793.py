#include<cstdio>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<string>
#include<cstdlib>
#include<functional>
#include<iostream>
#define fo(i,a,b) for(i=a;i<=b;i++)
#define fd(i,a,b) for(i=a;i>=b;i--)
#define MP(a,b) make_pair(a,b)
#define clr(x,y) memset(x,y,sizeof x)
#define fi first
#define se second
#define sqr(z) ((z)*(z))
using namespace std;
typedef pair<int,int> PII;
const int oo=1047483647,maxn=110000;
int n,i,j,k,m,q,T,rt,R,C,ge;
PII D[100];
bool flag,a[7][7],sure[7][7];
bool ret(int i,int j)
{
	return (!a[i][j])&&(!a[i][j+1])&&(!a[i][j-1])&&(!a[i-1][j])&&(!a[i+1][j])&&(!a[i+1][j+1])&&(!a[i-1][j-1])&&(!a[i+1][j-1])&&(!a[i-1][j+1]);
}
int fx[8][2]={{0,1},{0,-1},{1,0},{-1,0},{-1,-1},{1,1},{-1,1},{1,-1}};
bool check()
{
	int i,j,k,head=1,tail=1;
	clr(sure,0);
	fo(i,1,R)
	fo(j,1,C)
	if (ret(i,j))
	{
		sure[i][j]=1;
		D[1]=MP(i,j);
		int ans=1;
		while (head<=tail)
		{
			int x=D[head].fi;
			int y=D[head].se;
			fo(k,0,7)
			{
				int x2=x+fx[k][0];
				int y2=y+fx[k][1];
				if ((x2>=1)&&(y2>=1)&&(x2<=R)&&(y2<=C) && !sure[x2][y2])
				{
					sure[x2][y2]=1;
					ans++;
					if (ret(x2,y2))
					{
						tail++;
						D[tail]=MP(x2,y2);
					}
				}
			}
			head++;
		}
		if (ans+ge==R*C) 
		{
			flag=1;
			int xx=i,yy=j;
			fo(i,1,R)
			{
				fo(j,1,C)
				{
					if (i==xx && j==yy)
					putchar('c');
					else
				if (a[i][j]) putchar('*');
				else putchar('.');
				}
				printf("\n");
			}
			return 1;
		}
		else return 0;
	}
}
void dfs(int x,int y,int z)
{
	if (flag) return;
	if (y>C)
	{
		x++;y=1;
	}
	if (x>R)
	{
		if (ge==z) 
		check();
		return;
	}
	if (z<ge)
	{
		a[x][y]=1;
		dfs(x,y+1,z+1);
	}
	a[x][y]=0;
	dfs(x,y+1,z);
}
int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	for (;T;T--)
	{
		scanf("%d%d%d",&R,&C,&ge);
		flag=0;
		printf("Case #%d:\n",++rt);
		if (ge+1==R*C)
		{
			putchar('c');
			fo(i,2,C) putchar('*');
			printf("\n");
			fo(i,2,R)
			{
			fo(j,1,C)
			{
				putchar('*');
			}
			printf("\n");
			}
		}
		else
		{
		dfs(1,1,0);
		if (!flag) printf("Impossible\n");
		}
	}
	return 0;
}
