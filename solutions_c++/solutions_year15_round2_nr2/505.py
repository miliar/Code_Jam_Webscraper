#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define MEM(a,b) memset((a),(b),sizeof(a))

const int INF = 1e9 + 3;
const int N = 20 + 1;
int a[N][N];
int getans(int n)
{
	int ret = 0;
	while (n)
	{
		n -= n&-n;
		ret++;
	}
	return ret;
}

int solve(int r, int c)
{
	int ret = 0;
	for (int i = 0; i < r; i++)
	{
		for (int j = 0; j < c; j++)
		{
			if (!a[i][j]) continue;
			ret += a[i + 1][j] + a[i][j + 1];
		}
	}
	return ret;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int ncase;
	cin >> ncase;
	int ks = 1;
	while (ncase--)
	{
		MEM(a, 0);
		int r, c, n;
		cin >> r >> c >> n;
		int m = r*c;
		int ans = INF;
		for (int i = 0; i < (1 << m); i++)
		{
			if (getans(i) != n) continue;
			MEM(a, 0);
			for (int j = 0; j < m; j++) if (i&(1 << j)) a[j / c][j%c] = 1;
			ans = min(ans, solve(r, c));
		}
		printf("Case #%d: %d\n", ks++, ans);
	}
	return 0;
}