#include <cstdio>
#include <algorithm>

using namespace std;

int n,m;

int tab[105][105];
int xx[105];
int yy[105];

int mi,ma;

bool przyp()
{
	mi=200;
	ma=0;
	scanf("%d%d",&n,&m);
	for(int x=0;x<n;x++) for(int y=0;y<m;y++)
	{
		scanf("%d",&tab[x][y]);
		mi=min(mi,tab[x][y]);
		ma=max(ma,tab[x][y]);
	}
	for(int i=mi;i<=ma;i++)
	{
		for(int x=0;x<n;x++) xx[x]=0;
		for(int y=0;y<m;y++) yy[y]=0;
		for(int x=0;x<n;x++) for(int y=0;y<m;y++) if(tab[x][y]==i)
		{
			xx[x]++;
			yy[y]++;
		}
		for(int x=0;x<n;x++) for(int y=0;y<m;y++) if(tab[x][y]==i)
		{
			if((xx[x]^m)&&(yy[y]^n)) return false;
			tab[x][y]=i+1;
		}
	}
	return true;
}

int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		printf("Case #%d: %s\n",i,przyp()?"YES":"NO");
	}
	return 0;
}
