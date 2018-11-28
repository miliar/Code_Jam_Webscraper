#define MYDEBUG
#define _CRT_SECURE_NO_WARNINGS
#define TASK "C-small-attempt0"
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

int n, cnt;
bool check(int msk, int base, int div)
{
	int cur = 0;
	for (int i = n - 1; i >= 0; --i)
	{
		cur = cur * 1ll * base % div;
		if (msk & (1 << i))
			cur = (cur + 1) % div;
	}
	return cur == 0;
}

vector <int> jamcoin(int msk)
{
	vector <int> ans;
	for (int base = 2; base <= 10; ++base)
	{
		long long val = 0;
		for (int i = n - 1; i >= 0; --i)
		{
			val = val*base;
			if (msk & (1 << i))
				++val;
		}
		bool pr = true;
		for (int x = 2; x * 1ll * x <= val; ++x)
		{
			if (check(msk, base, x))
			{
				ans.push_back(x);
				pr = false;
				break;
			}
		}
		if (pr)
			ans.push_back(-1);
	}
	return ans;
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
		scanf("%d %d", &n, &cnt);
		printf("Case #%d:\n", id);
		for (int i = (1 << (n - 1)) + 1; i < (1 << n); i += 2)
		{
			vector <int> foo = jamcoin(i);
			bool good = true;
			for (int j = 0; j < foo.size(); ++j)
				if (foo[j] == -1)
					good = false;
			if (good)
			{
				for (int j = n - 1; j >= 0; --j)
				{
					if (i & (1 << j))
						printf("1");
					else
						printf("0");
				}
				for (int j = 0; j < foo.size(); ++j)
					printf(" %d", foo[j]);
				printf("\n");
				--cnt;
				if (cnt == 0)
					break;
			}
		}
	}

	my_return(0);
}
