#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>
#include <cstring>
#include <string>
#include <list>
#include <set>
#include <queue>

using namespace std;

typedef long long int LL;
typedef pair<int,int> pii;

#define F first
#define S second
#define pb push_back
#define mp make_pair

int g[202][202];
int need[21] , M[202];
int dp[1<<21];
int sol[22];
int n, k;

int solve(int mask, int x)
{	
	int &res = dp[mask];
	if(res != -1) return res;
	if(x == n) return 1;

	int keys[201] = {0};

	res = 0;

	for(int i = 0; i < n; ++i) keys[need[i]] = M[need[i]];

	for(int i = 0; i < n; ++i)
	{
		if(mask&1<<i) 
		{
			keys[need[i]]--;
			for(int j = 0; j < 201; ++j)
                keys[j] += g[i][j];
		}
	}

	for(int i = 0; i < n; ++i)
	{
 		if( !(mask&1<<i) && keys[need[i]])
			sol[x] = i, res = res | solve(mask|1<<i, x+1); 

		if(res) return 1;
	}

	return res;
}

int main (void)
{
	int T, x;
	cin >> T;

	for(int c = 1; c <= T; ++c)
	{
		memset(M, 0, sizeof M);
		memset(g, 0, sizeof g);

		cin >> k >> n;

		for(int i = 0; i < k; ++i)
		{
			cin >> x;
			M[x]++;
		}

		for(int i = 0; i < n; ++i)
		{
			int cnt;
			cin >> need[i] >> cnt;
			for(int j = 0; j < cnt; ++j)
			{
				cin >> x;
				g[i][x]++;
			}
		}

		memset(dp, -1, sizeof dp);
		int res = solve(0, 0);

		printf("Case #%d:", c);
		if(!res) printf(" IMPOSSIBLE");
		else for(int i = 0; i < n; ++i) printf(" %d", sol[i]+1);
		printf("\n");
	}
	return 0;
}
