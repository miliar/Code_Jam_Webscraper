#include <cstdio>
#include <algorithm>

using namespace std;

int N,M;
int A[110][110];

int main()
{
	int T;
	scanf("%d",&T);
	for(int tt = 1 ; tt <= T ; tt++)
	{
		scanf("%d %d",&N,&M);
		for(int c = 0 ; c < N ; c++)
			for(int d = 0 ; d < M ; d++)
				scanf("%d",&A[c][d]);
		printf("Case #%d: ", tt);
		for(int c = 99 ; c > 0 ; c--)
		{
			for(int d = 0 ; d < N ; d++)
			{
				for(int e = 0 ; e < M ; e++)
				{
					if(A[d][e] == c)
					{
						bool x,y;
						x = y = false;
						for(int f = 0 ; f < M ; f++)
							if(A[d][f] > c)
								x = true;
						for(int f = 0 ; f < N ; f++)
							if(A[f][e] > c)
								y = true;
						if(x and y)
						{
							printf("NO\n");
							goto xxx;
						}
					}
				}
			}
		}
		printf("YES\n");
		xxx:;
	}
}