#include <cstdlib>
#include <cstdio>

struct pnt{int x,y;};

int T,r,c,m,n;
bool f[63][63];

bool dfs(int x,int y,int s)
{
	if (x<1 || x>r || y<1 || y>c) return false;
	int cnt=0;
	for (int i=-1;i<=1;++i) for (int j=-1;j<=1;++j) cnt+=f[x+i][y+j];
	pnt *a=(pnt*)malloc((9-cnt)*sizeof(pnt));
	cnt=0;
	for (int i=-1;i<=1;++i) for (int j=-1;j<=1;++j) if (!f[x+i][y+j])
	{
		f[x+i][y+j]=true;
		a[cnt].x=x+i;
		a[cnt].y=y+j;
		++cnt;
	}
	if (s+cnt==n) goto TRUE;
	else
	{
		if (s+cnt<n) for (int i=0;i<cnt;++i) if (dfs(a[i].x,a[i].y,s+cnt)) goto TRUE;
		for (int i=0;i<cnt;++i) f[a[i].x][a[i].y]=false;
		free(a);
		return false;
	}
	TRUE:
	{
		free(a);
		return true;
	}
}
void prt(int x,int y)
{
	for (int i=1;i<=r;++i)
	{
		for (int j=1;j<=c;++j)
		{
			if (f[i][j])
			{
				if (i==x && j==y) putchar('c');
				else putchar('.');
			}
			else putchar('*');
			f[i][j]=false;
		}
		putchar('\n');
	}
}
int main()
{
	scanf("%d",&T);
	for (int t=1;t<=T;++t)
	{
		printf("Case #%d:\n",t);
		scanf("%d%d%d",&r,&c,&m);
		n=r*c-m;
		for (int i=0;i<=r+1;++i) f[i][0]=f[i][c+1]=true;
		for (int j=0;j<=c+1;++j) f[0][j]=f[r+1][j]=true;
		for (int x=1;x<=r;++x) for (int y=1;y<=c;++y)
		{
			f[x][y]=true;
			if (n==1 || dfs(x,y,1))
			{
				prt(x,y);
				f[x][y]=false;
				goto NEXT;
			}
			f[x][y]=false;
		}
		puts("Impossible");
		NEXT:
		{
			for (int i=0;i<=r+1;++i) f[i][0]=f[i][c+1]=false;
			for (int j=0;j<=c+1;++j) f[0][j]=f[r+1][j]=false;
		}
	}
	return 0;
}