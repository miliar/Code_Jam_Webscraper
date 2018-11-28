#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <stdio.h>
//#include <math.h>

using namespace std;

typedef pair<int, int>  pii;

#define LS <
#define Size(x) (int(x.size()))

#define FOR(k,a,b) for(int k=(a); k LS (b); ++k)

int N, M;
int table[100][100];
int row[100];
int col[100];

void solveCase()
{
	scanf("%d%d",&N,&M);
	FOR(i,0,N) row[i] = 0;
	FOR(i,0,M) col[i] = 0;
	FOR(i,0,N)
	{
		FOR(j,0,M)
		{
			scanf("%d",&table[i][j]);
			if (table[i][j] > row[i])
				row[i] = table[i][j];
			if (table[i][j] > col[j])
				col[j] = table[i][j];
		}
	}

	FOR(i,0,N)
	{
		FOR(j,0,M)
		{
			if (row[i] > table[i][j] && col[j] > table[i][j])
			{
				printf("NO\n");
				return;
			}
		}
	}

	printf("YES\n");
}

int main() 
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int T;
	scanf("%d",&T);
	FOR(_t, 0, T)
	{
		printf("Case #%d: ",_t+1);
		solveCase();
	}
	return 0;
}