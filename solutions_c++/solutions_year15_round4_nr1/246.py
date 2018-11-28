#include <iostream>
#include <cstdio>
using namespace std;

#define MAXN 200

int R,C,T;
char A[MAXN][MAXN];
int G[MAXN][MAXN];
int step[5][2]={{1,0},{-1,0},{0,1},{0,-1},{0,0}};

bool inside(int i,int j)
{
	return i>=0 && i<R && j>=0 && j<C;
}

int ch2int(char ch)
{
	switch (ch)
	{
	case '^':
		return 1;
	case 'v':
		return 0;
	case '<':
		return 3;
	case '>':
		return 2;
	default:
		return 4;
	}
}

bool can(int i,int j,int s)
{
	int x = i, y = j;
	do
	{
		x += step[s][0];
		y += step[s][1];
		if (!inside(x,y))
		{
			break;
		}
		if (G[x][y] != 4)
		{
			break;
		}
	}while (1);
	if (!inside(x,y))
	{
		return false;
	}
	else
	{
		return true;
	}
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	scanf("%d",&T);
	for (int cases=1;cases<=T;cases++)
	{
		scanf("%d%d",&R,&C);
		for (int i=0;i<R;++i)
		{
			scanf("%s",A[i]);
		}
		for (int i=0;i<R;++i)
			for (int j=0;j<C;++j)
			{
				G[i][j] = ch2int(A[i][j]);
			}
		int ans = 0;
		for (int i=0;i<R;++i)
			for (int j=0;j<C;++j)
				if (G[i][j] != 4)
				{
					if (can(i,j,G[i][j]))
					{
						continue;
					}
					int s;
					for (s = 0; s < 4; ++ s)
					{
						if (can(i,j,s))
						{
							ans ++;
							break;
						}
					}
					if (s == 4)
					{
						ans = -1;
						goto PRINT;
					}
				}
	PRINT:
		printf("Case #%d: ", cases);
		if (ans == -1)
		{
			printf("IMPOSSIBLE");
		}
		else
		{
			printf("%d",ans);
		}
		printf("\n");
				
	}

    return 0;
}
