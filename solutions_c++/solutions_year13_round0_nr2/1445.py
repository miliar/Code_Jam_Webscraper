#include<stdio.h>
#include<string.h>
#include<queue>
#include<string>
#include<set>
#include<map>
#include<algorithm>
#include<math.h>
#include<stack>
#include<sstream>
using namespace std;

#define MAXN 105

int grid[MAXN][MAXN];
int row_max[MAXN];
int col_max[MAXN];
int n, m, t;

bool check()
{
	for(int i=0 ; i<n ; i++)
	{
		row_max[i]=grid[i][0];
		for(int j=0 ; j<m ; j++)
			row_max[i] = max ( row_max[i] , grid[i][j] ) ;
	}
	for(int i=0 ; i<m ; i++)
	{
		col_max[i]=grid[0][i];
		for(int j=0 ; j<n ; j++)
			col_max[i] = max ( col_max[i] , grid[j][i] ) ;
	}
	for(int i=0 ; i<n ; i++)
		for(int j=0 ; j<m ; j++)
			if ( grid[i][j]!=row_max[i] && grid[i][j]!=col_max[j] )
				return 0;
	return 1;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	for(int tc=1 ; tc<=t ; tc++)
	{
		printf("Case #%d: ",tc);
		scanf("%d%d",&n,&m);
		for(int i=0 ; i<n ; i++)
			for(int j=0 ; j<m ; j++)
				scanf("%d",&grid[i][j]);
		if(check()) printf("YES\n");
		else printf("NO\n");
	}
	//while(1);
}