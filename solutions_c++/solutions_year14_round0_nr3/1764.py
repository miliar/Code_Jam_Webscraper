#include<cstdio>
using namespace std;
int b[50][50]={0},v[50][50]={0};
bool b2[50][50][2500]={false},v2[50][50];
int m,n,k,c,mx=100000;
bool found;
int max(int x,int y){ return x>=y?x:y; }
int min(int x,int y){ return x<=y?x:y; }
void toggle(int x,int y)
{
	int old=b[x][y],diff=1-old-old;
	b[x][y]+=diff;
	v[x][y]+=diff;
	if( x>=1 ){ v[x-1][y]+=diff; if( y>=1 ) v[x-1][y-1]+=diff; if( y<n-1 ) v[x-1][y+1]+=diff; }
	if( y>=1 ) v[x][y-1]+=diff; if( y<n-1 ) v[x][y+1]+=diff;
	if( x<m-1 ){ v[x+1][y]+=diff; if( y>=1 ) v[x+1][y-1]+=diff; if( y<n-1 ) v[x+1][y+1]+=diff; }
}
bool works(int x,int y)
{
	if( b[x][y]==1 ) return true;
	if( v[x][y]==0 ) return true;
	if( x>=1 ){ if( v[x-1][y]==0 ) return true; if( y>=1 ) if( v[x-1][y-1]==0 ) return true; if( y<n-1 ) if( v[x-1][y+1]==0 ) return true; }
	if( y>=1 ) if( v[x][y-1]==0 ) return true; if( y<n-1 ) if( v[x][y+1]==0 ) return true;
	if( x<m-1 ){ if( v[x+1][y]==0 ) return true; if( y>=1 ) if( v[x+1][y-1]==0 ) return true; if( y<n-1 ) if( v[x+1][y+1]==0 ) return true; }
	return false;
}
void dfs(int x,int y)
{
	if( v2[x][y] ) return;
//printf("%d %d\n",x,y);
	v2[x][y]=true;
	if( x>=1 ){ if( v[x-1][y]==0 ) dfs(x-1,y); if( y>=1 ) if( v[x-1][y-1]==0 ) dfs(x-1,y-1); if( y<n-1 ) if( v[x-1][y+1]==0 ) dfs(x-1,y+1); }
	if( y>=1 ) if( v[x][y-1]==0 ) dfs(x,y-1); if( y<n-1 ) if( v[x][y+1]==0 ) dfs(x,y+1);
	if( x<m-1 ){ if( v[x+1][y]==0 ) dfs(x+1,y); if( y>=1 ) if( v[x+1][y-1]==0 ) dfs(x+1,y-1); if( y<n-1 ) if( v[x+1][y+1]==0 ) dfs(x+1,y+1); }
}
bool works2(int x,int y)
{
	for(int x1=max(0,x-2),x2=min(m,x+2);x1<=x2;x1++)
	{
		for(int y1=max(0,y-2),y2=min(n,y+2);y1<=y2;y1++)
		{
			if( !works(x1,y1) ) return false;
		}
	}
	return true;
}
void search(int d,int p)
{
	if( found ) return;
if( true )
{
//	b2[m][n][d]=true;
	if( d==k )
	{
		for(int a=0;a<m;a++)
			for(int s=0;s<n;s++)
				if( !works(a,s) ) goto notworks;
		for(int a=0;a<m;a++) for(int s=0;s<n;s++) v2[a][s]=false;
		for(int a=0;a<m;a++) for(int s=0;s<n;s++) if( v[a][s]==0 ){ dfs(a,s); a=m; break; }
		for(int a=0;a<m;a++) for(int s=0;s<n;s++) if( v[a][s]==0 && !v2[a][s] ) goto notworks;
//for(int a=0;a<m;a++) for(int s=0;s<n;s++) printf("%d",v[a][s]);
		found=true;
		bool t=false;
		for(int a=0;a<m;a++)
		{
			for(int s=0;s<n;s++)
				if( b[a][s]==0 )
				{
					if( v[a][s]==0 && !t ){ t=true; printf("c"); }
					else printf(".");
				}
				else printf("*");
			printf("\n");
		}
		return;
	}
//	if( d>b2[m][n] ) b2[m][n]=d;
notworks:;
}
	if( d>=k ) return;
	c++;
	if( false && c>=mx ) return;
	for(;p<=n*m-k+d;p++)
	{
			int a=p/n,s=p%n;
			if( b[a][s]==0 )
			{
				toggle(a,s);
				if( true || works2(a,s) ) search(d+1,p+1);
				toggle(a,s);
			}
	}
}
int main()
{
	k=1000000;
if( false )
{
	for(m=1;m<=5;m++)
	{
		for(n=m;n<=5;n++)
		{
			c=0;
			search(0,0);
//			printf("%d ",b2[m][n]);
		}
//		printf("\n\n");
	}
}
	int x,y,z;
int N;
scanf("%d",&N);
for(int T=1;T<=N;T++)
{
	scanf("%d%d%d",&x,&y,&z);
	m=x;
	n=y;
	k=z;
	found=false;
	printf("Case #%d:\n",T);
	if( k==m*n-1 ){ printf("c"); for(int a=0;a<m;a++){ for(int s=a==0?1:0;s<n;s++) printf("*"); printf("\n"); } continue; }
	search(0,0);
	if( !found ) printf("Impossible\n");
//	printf("%d\n",b2[x][y][z]);
}
//	scanf("%d %d %d\n");
	return 0;
}
