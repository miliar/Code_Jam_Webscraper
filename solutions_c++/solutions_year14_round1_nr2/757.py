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
const int N = 4e5 + 10;
vector<int> v[1001];


int dfs(int u, int p)
{
	int ret1 = 0;
	int ret2 = 0;
	for (int i = 0; i < v[u].size(); i++)
	{
		int t = v[u][i];
		if (t == p) continue;
		int x = dfs(t, u);
		if (x >= ret2)
		{
			ret1 = ret2;
			ret2 = x;
		}
		else if (x > ret1) ret1 = x;
	}
	if (ret1 == 0 || ret2 == 0) return 1;
	return ret1 + ret2 + 1;
}
int main()
{
	//freopen("input.txt", "r", stdin);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int ncase;
	int ks = 1;
	int n;
	int x, y;
	scanf("%d", &ncase);
	while (ncase--)
	{
		scanf("%d", &n);
		for (int i = 1; i <= n; i++) v[i].clear();
		for (int i = 1; i < n; i++)
		{
			scanf("%d%d", &x, &y);
			v[x].push_back(y);
			v[y].push_back(x);
		}
		int ans = 0;
		for (int i = 1; i <= n; i++)
		{
			int t = dfs(i,-1);
			ans = max(ans, t);
		}
		printf("Case #%d: %d\n", ks++, n-ans);
	}
	return 0;
}