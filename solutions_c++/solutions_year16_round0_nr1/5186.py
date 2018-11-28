//#define MYDEBUG
#define _CRT_SECURE_NO_WARNINGS
#define TASK "A-large"
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

const int MOD = 1000000007;
const int INF = 1000000001;
const int MAXN = 100010;
const long double EPS = 1e-6;
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
	for (int id = 1; id <= CASE; ++id)
	{
		printf("Case #%d: ", id);
		int n;
		scanf("%d", &n);
		if (n == 0)
			printf("INSOMNIA\n");
		else
		{
			bool u[10];
			memset(u, false, sizeof u);
			for (int j = 1; j <= 100; ++j)
			{
				int s = n*j;
				while (s)
				{
					u[s % 10] = true;
					s /= 10;
				}
				bool good = true;
				for (int x = 0; x < 10; ++x)
					if (!u[x])
						good = false;
				if (good)
				{
					printf("%d\n", n*j);
					break;
				}
			}
		}
	}

	my_return(0);
}
