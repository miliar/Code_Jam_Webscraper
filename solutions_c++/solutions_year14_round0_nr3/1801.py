#pragma comment(linker, "/STACK:500000000") 
#include <functional>
#include <algorithm> 
#include <iostream> 
#include <string.h> 
#include <stdlib.h> 
#include <sstream> 
#include <ctype.h> 
#include <stdio.h> 
#include <bitset>
#include <vector> 
#include <string> 
#include <math.h> 
#include <time.h> 
#include <queue> 
#include <stack> 
#include <list>
#include <map> 
#include <set> 
#define Int long long 
#define inf 0x3f3f3f3f
#define eps 1e-9
using namespace std;
#define N 5

int A[N][N];
bool used[N][N];
int n, m, cnt;

bool ok(int x, int y)
{
	int cnt = 0;
	for(int i = x - 1; i <= x + 1; i++)
		for(int j = y - 1; j <= y + 1; j++)
		{
			if(i == x && j == y)
				continue;
			if(i >= 0 && i < n && j >= 0 && j < m && A[i][j])
				cnt++;
		}
	return (cnt == 0);
}

queue <int> q;

void f(int x, int y)
{
	if(x >= 0 && x < n && y >= 0 && y < m && !used[x][y])
	{
		used[x][y] = true;
		q.push(x);
		q.push(y);
	}
}

int size(int mask)
{
	int res = 0;
	while(mask)
		res += (mask & 1), mask >>= 1;
	return res;
}

int main()
{
	freopen("i.in", "rt", stdin);
	freopen("o2.out", "wt", stdout);
	int t, test = 0, i, j;
	cin >> t;
	while(t--)
	{
		test++;
		scanf("%d %d %d", &n, &m, &cnt);
		int h = (1 << (n * m));
		for(int mask = 0; mask < h; mask++)
		{
			if(size(mask) == cnt)
			{
				memset(A, 0, sizeof(A));
				for(i = 0; i < n * m; i++)
					if(mask & (1 << i))
					{
						A[i / m][i % m] = 1;
					}
				for(int X = 0; X < n; X++)
					for(int Y = 0; Y < m; Y++)
					{
						if(A[X][Y] == 0)
						{
							memset(used, false, sizeof(used));
							q.push(X);
							q.push(Y);
							used[X][Y] = true;
							while(!q.empty())
							{
								int x = q.front();
								q.pop();
								int y = q.front();
								q.pop();
								if(ok(x, y))
								{
									f(x - 1, y - 1);
									f(x - 1, y);
									f(x - 1, y + 1);
									f(x, y - 1);
									f(x, y + 1);
									f(x + 1, y - 1);
									f(x + 1, y);
									f(x + 1, y + 1);
								}
							}
							bool ok = true;
							for(i = 0; i < n; i++)
								for(j = 0; j < m; j++)
									if(!A[i][j] && !used[i][j])
										ok = false;
							if(ok)
							{
								printf("Case #%d:\n", test);
								for(i = 0; i < n; i++)
								{
									for(j = 0; j < m; j++)
									{
										if(i == X && j == Y)
											printf("c");
										else
											if(A[i][j] == 0)
												printf(".");
											else
												printf("*");
									}
									puts("");
								}
								goto END;
							}
						}
					}
			}
		}
		printf("Case #%d:\n", test);
		puts("Impossible");
		END: ;
	}
}

/*
4 4 3

5 4 7
*/