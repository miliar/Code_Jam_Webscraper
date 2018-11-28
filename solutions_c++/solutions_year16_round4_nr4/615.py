//#define MYDEBUG
#define _CRT_SECURE_NO_WARNINGS
#define TASK "D-small-attempt0"
//#define TASK "B-large"
#pragma comment(linker, "/STACK:536870912")
#include <cstdio>
#include <iostream>
#include <iomanip> 
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <functional>
#include <cassert>
#include <bitset>
#include <unordered_set>
#include <unordered_map>
#include <random>

const int MOD = 1000000003;
const int INF = 1000000001;
const int MAXN = 100000;
const long double EPS = 1e-8;
const int HASH_POW = 29;
const long double PI = acos(-1.0);

using namespace std;

void my_return(int code)
{
#ifdef MYDEBUG
	cout << "\nTime = " << fixed << setprecision(3) << double(clock()) / CLOCKS_PER_SEC << endl;
#endif
	exit(code);
}

int n;
char p[5][5], q[5][5];

bool in[5], out[5];
bool perebor()
{
	for (int i = 1; i <= n; ++i)
	{
		if (!in[i])
		{
			in[i] = true;
			bool good2 = false;
			for (int j = 1; j <= n; ++j)
			{
				if (q[i][j] == '1' && !out[j])
				{
					good2 = true;
					out[j] = true;
					if (!perebor())
					{
						in[i] = false;
						out[j] = false;
						return false;
					}
					out[j] = false;
				}
			}
			in[i] = false;
			if (!good2)
				return false;
		}
	}
	return true;
}

int main()
{
	cin.sync_with_stdio(0);
	cin.tie(0);
	mt19937 mt_rand(time(0));
#ifdef MYDEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	freopen(TASK".in", "rt", stdin);
	freopen(TASK".out", "wt", stdout);
	/*freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);*/
#endif

	int CASE;
	scanf("%d", &CASE);
	for (int it = 1; it <= CASE; ++it)
	{
		scanf("%d\n", &n);
		for (int i = 1; i <= n; ++i)
		{
			for (int j = 1; j <= n; ++j)
				p[i][j] = getchar();
			getchar();
		}

		int ans = INF;
		for (int msk = 0; msk < (1 << (n*n)); ++msk)
		{
			bool good = true;
			for (int i = 0; i < n; ++i)
				for (int j = 0; j < n; ++j)
					if (p[i + 1][j + 1] == '1' && ((msk & (1 << (n*i + j))) == 0))
						good = false;
			if (!good)
				continue;
			memset(q, '0', sizeof q);
			for (int i = 0; i < n; ++i)
				for (int j = 0; j < n; ++j)
					if (msk & (1 << (n*i + j)))
						q[i + 1][j + 1] = '1';

			if (perebor())
			{
				int cost = 0;
				for (int i = 1; i <= n; ++i)
					for (int j = 1; j <= n; ++j)
						if (p[i][j] != q[i][j])
							++cost;
				ans = min(ans, cost);
			}
		}

		printf("Case #%d: %d\n", it, ans);
	}

	my_return(0);
}
