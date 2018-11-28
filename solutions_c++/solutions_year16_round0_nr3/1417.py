#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <queue>
#include <vector>
#include <map>
#include <cmath>
#include <string>
#include <cstring>
#include <utility>
#include <stack>
#include <set>
#include <algorithm>
#include <bitset>
#include <functional>
#include <ctime>
#include <cassert>
#include <valarray>
#include <unordered_map>
#pragma comment(linker, "/STACK:167772160")

using namespace std;
#pragma region TypeDefs

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef pair<int, int> pii;
typedef vector< vector<int> > vvint;

#pragma endregion

const int INF = 1e9 + 10;
const ll LINF = (ll) 2e18 + 10;
const ld PI = acos(-1);
const ld eps = 1e-8;
const ld EPS = 1e-12;

int cnt;
string res = "";
vector<int> pos1, pos2;

void dfs(int lost, int p1, int p2)
{
	if (!cnt)
		return;
	if (lost == 0)
	{
		--cnt;
		cout << res << ' ';
		for (int i = 2; i < 11; ++i)
			if (i % 2 == 1)
				cout << "2 ";
			else if (i % 3 != 0)
				cout << "3 ";
			else
				cout << "7 ";
		cout << '\n';
		return;
	}
	if (lost & 1)
	{
		for (int i = p1; i < pos1.size(); ++i)
		{
			res[pos1[i]] = '1';
			dfs(lost - 1, i + 1, p2);
			res[pos1[i]] = '0';
		}
	}
	else
	{
		for (int i = p2; i < pos2.size(); ++i)
		{
			res[pos2[i]] = '1';
			dfs(lost - 1, p1, i + 1);
			res[pos2[i]] = '0';
		}
	}
}

void solve()
{
	int n;
	cin >> n >> cnt;
	for (int i = 0; i < n; ++i)
		res += '0';
	res[0] = res[1] = res[n - 1] = res[n - 2] = '1';
	for (int i = 2; i < n - 2; i += 2)
		pos1.push_back(i);
	for (int i = 3; i < n - 2; i += 2)
		pos2.push_back(i);
	dfs(8, 0, 0);
}

int main()
{
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
#endif
	ios_base::sync_with_stdio(0), cin.tie(0);

	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ":\n";
		solve();
	}

#ifdef LOCAL
	//fprintf(stderr, "\n\nTime: %.3f", (double) clock() / CLOCKS_PER_SEC);
#endif
	return 0;
}