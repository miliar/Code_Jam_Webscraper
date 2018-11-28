#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <utility>
#include <stack>
#include <queue>
#include <set>
#include <map>

#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define pi 2*acos(0.0)
#define eps 1e-9
#define PII pair<int,int> 
#define PDD pair<double,double>
#define LL long long
#define INF 1000000000

using namespace std;

int R, C, T;
int target[111][111], height[111][111];
bool used[111];

bool checkOK(int r, int c, int next, int code) // code 0 -> horizontal, 1 -> vertical
{
	if(code == 0) 
	{
		for(int i = 0; i < C; i++)
			if(height[r][i] == target[r][i] && height[r][i] > next) return false;
	} else 
	{
		for(int i = 0; i < R; i++)
			if(height[i][c] == target[i][c] && height[i][c] > next) return false;
	}
	
	return true;
}

int main()
{
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		scanf("%d %d", &R, &C);
		
		memset(used, false, sizeof(used));
		for(int i = 0; i < R; i++)
			for(int j = 0; j < C; j++)
			{
				scanf("%d", &target[i][j]);
				used[target[i][j]] = true;
				height[i][j] = 100;
			}
			
		bool bisa = true;
		for(int next = 100; next > 0 && bisa; next--) if(used[next])
			for(int i = 0; i < R && bisa; i++)
				for(int j = 0; j < C && bisa; j++)
					if(target[i][j] == next && height[i][j] != next)
					{
						if(checkOK(i, j, next, 0)) for(int k = 0; k < C; k++) height[i][k] = min(height[i][k], next); else
							if(checkOK(i, j, next, 1)) for(int k = 0; k < R; k++) height[k][j] = min(height[k][j], next); else
								bisa = false;
					}
					
		printf("Case #%d: %s\n", t, bisa?"YES":"NO");
	}
	return 0;
}

