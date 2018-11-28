#include <cstdio>
#include <algorithm>
using namespace std;

int R,C;
int G[105][105],MR[105],MC[105];

int main()
{
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		scanf("%d%d",&R,&C);
		for(int r = 0; r < R; r++)
			for(int c = 0; c < C; c++)
				scanf("%d", &G[r][c]);
		
		// calc MR
		for(int r = 0; r < R; r++)
		{
			MR[r] = 0;
			for(int c = 0; c < C; c++)
				if(G[r][c] > MR[r])
					MR[r] = G[r][c];
		}
		
		// calc MC
		for(int c = 0; c < C; c++)
		{
			MC[c] = 0;
			for(int r = 0; r < R; r++)
				if(G[r][c] > MC[c])
					MC[c] = G[r][c];
		}
		
		bool possible = true;
		for(int r = 0; r < R; r++)
			for(int c = 0; c < C; c++)
				if(MR[r] > G[r][c] && MC[c] > G[r][c])
					possible = false;
		
		if(possible)
			printf("YES\n");
		else
			printf("NO\n");
	}
}

