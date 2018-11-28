#include <iostream>
#include <cstdio>
#include <string>
#include <string.h>
#include <queue>
#include <math.h>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <bitset>
#include <ctype.h>
#include <cassert>
#include <stack>
#include <fstream>

using namespace std;

#define snd second
#define fst first
#define mp make_pair
#define ll long long
#define ull unsigned long long
#define ld long double
#define pb push_back
#define left _left

template < typename T > T abs(T x)
{
	return x > 0 ? x : -x;
}

const int inf = 1e9;
const int maxn = 1005;

pair < int, int > a[maxn], b[maxn];;
int dp[maxn][maxn];
int used[maxn];
int currUsed = 1;

int tree[maxn];

void init()
{
	for (int i = 0; i < maxn; i++)
		tree[i] = 0;
}

void add(int i)
{
	while (i < maxn)
	{
		tree[i]++;
		i = i | (i + 1);
	}
}

int get(int r)
{
	int res = 0;
	while (r >= 0)
	{
		res += tree[r];
		r = (r & (r + 1)) - 1;
	}
	return res;
}


int main(int argc, char *argv[])
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	int t;
	cin >> t;
	
	for (int tt = 1; tt <= t; tt++)
	{
		int n;
		scanf("%d", &n);
		
		for (int i = 1; i <= n; i++)
		{
			scanf("%d", &a[i].fst);
			a[i].snd = i;
			b[i] = mp(a[i].snd, a[i].fst);
		}
		
		sort(a + 1, a + 1 + n);
		
		for (int i = 0; i < maxn; i++)
			for (int j = 0; j < maxn; j++)
				dp[i][j] = inf;
				
		dp[0][0] = 0;
		
		init();
		
		for (int i = 1; i <= n; i++)
		{
			
			for (int j = 0; j <= i; j++)
			{
				if (j)
				{
					int dist = a[i].snd - get(a[i].snd) - 1;
					
					dp[i][j] = dp[i - 1][j - 1] + dist; 
				}
				
				if (i > j)
				{
					int dist = n - a[i].snd - (get(n) - get(a[i].snd));
					dp[i][j] = min(dp[i][j], dp[i - 1][j] + dist);
				}
			}
			
			add(a[i].snd);
		}
		
		
		/*int bans = 1e9;
		do {
			bool good = true;
			int j = 1; 
			while (j + 1 <= n && b[j].snd < b[j + 1].snd) j++;
			for (int i = j; i + 1 <= n; i++)
				good &= b[i].snd > b[i + 1].snd;
			if (!good)
				continue;
			int curr = 0;
			for (int i = 1; i <= n; i++)
				curr += abs(i - b[i].fst);
			if (bans > curr)
			{
				bans = curr;
				for (int i = 1; i <= n; i++)
					cerr << " " << b[i].fst;
				cerr << endl;
			}
			bans = min(bans, curr);
		}while (next_permutation(b + 1, b + 1 + n));
		
		cerr << bans / 2 << endl;*/
		
		int ans = 1e9;
		
		for (int i = 0; i <= n; i++)
		{
			ans = min(ans, dp[n][i]);
			
		}
		
		/*if (bans != ans)
		{
			cerr << tt << endl;
			cerr << ans << " " << bans << endl;
			break;
		}*/
			
			
		//assert(ans % 2 == 0);
		
		cout << "Case #" << tt << ": " << ans << endl;
	}
	return 0;
}












