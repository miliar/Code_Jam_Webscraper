#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <queue>
#include <ctime>
using namespace std;
#define maxn 110
int h[maxn][maxn],cur[maxn][maxn];
int n,m;
void cutr(int r)
{
	int i,big;
	big = 0;
	for ( i=1 ; i<=m ; i++ ) big = max(big,h[r][i]);
	for ( i=1 ; i<=m ; i++ ) cur[r][i] = min(cur[r][i],big);
}
void cutc(int c)
{
	int i,big;
	big = 0;
	for ( i=1 ; i<=n ; i++ ) big = max(big,h[i][c]);
	for ( i=1 ; i<=n ; i++ ) cur[i][c] = min(cur[i][c],big);
}
void input()
{
	int i,j;
	scanf("%d%d",&n,&m);
	for ( i=1 ; i<=n ; i++ )
	for ( j=1 ; j<=m ; j++ ) scanf("%d",&h[i][j]);
}
int judge()
{
	int r,c;
	for ( r=1 ; r<=n ; r++ )
	for ( c=1 ; c<=m ; c++ ) cur[r][c] = 100;

	for ( r=1 ; r<=n ; r++ ) cutr(r);
	for ( c=1 ; c<=m ; c++ ) cutc(c);

	for ( r=1 ; r<=n ; r++ )
	for ( c=1 ; c<=m ; c++ )
	if (cur[r][c] != h[r][c]) return 0;

	return 1;
}
int main()
{
	int cas,tt=0;
	freopen("test.in","r",stdin);
	freopen("out.out","w",stdout);
	scanf("%d",&cas);
	while (cas--)
	{
		printf("Case #%d: ",++tt);
		input();
		if (judge()) printf("YES\n");
		else	printf("NO\n");
	}
	return 0;
}
