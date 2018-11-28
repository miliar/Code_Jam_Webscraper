#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<list>
#include<functional>
#include<algorithm>
#include<cassert>

using namespace std;

//#define _INFILE		"B.in"
//#define _OUTFILE	"B.out"

//#define _INFILE		"B-small-attempt0.in"
//#define _OUTFILE	"B-small.out"

#define _INFILE		"B-large.in"
#define _OUTFILE	"B-large.out"


void solve()
{
	int in[100][100];
	int n, m;
	scanf("%d%d",&n,&m);
	for(int i=0; i<n; i++)
		for(int j=0; j<m; j++)
			scanf("%d",&in[i][j]);

	int rowMax[100];
	int colMax[100];
	for(int i=0; i<100; i++)
	{
		rowMax[i] = 0;
		colMax[i] = 0;
	}
	for(int i=0; i<n; i++)
	{
		for(int j=0; j<m; j++)
		{
			rowMax[i] = max(rowMax[i], in[i][j]);
			colMax[j] = max(colMax[j], in[i][j]);
		}
	}

	for(int i=0; i<n; i++)
		for(int j=0; j<m; j++)
		{
			if (in[i][j] < rowMax[i] && in[i][j] < colMax[j])
			{
				printf("NO\n");
				return;
			}
		}


	printf("YES\n");
}

int main(void)
{
	int T;
	freopen(_INFILE, "r", stdin);
	freopen(_OUTFILE, "w", stdout);

	scanf("%d",&T);

	for(int i=0; i<T; i++)
	{
		printf("Case #%d: ", i+1);
		solve();
	}
	return 0;
}

