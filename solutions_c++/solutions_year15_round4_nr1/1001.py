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
const LL INF = 1000000007;
const int N = 1e2+10;
const double eps = 1e-6;

char c[N][N];
int dx[] = { 0, 0, -1, 1 };
int dy[] = { -1, 1, 0, 0 };
map<char, int> mm;
int flag[N][N];
int n,m;
int ans;
int fff = 0;
string str = "<>^v";
bool check(int x, int y, int v)
{
	if (x < 0 || x >= n) return false;
	if (y < 0 || y >= m) return false;
	if (flag[x][y]) return true;	
	if (c[x][y] != '.')
	{
		flag[x][y] = 1;
		v = mm[c[x][y]];
		if (check(x + dx[v], y + dy[v], v)) return true;
		for (int i = 0; i < 4; i++)
		{
			if (i == v) continue;
			if (check(x + dx[i], y + dy[i], i))
			{
				c[x][y] = str[i];
				ans++;
				return true;
			}
			
		}
		fff = 1;
		return false;
	}
	else return check(x + dx[v], y + dy[v], v);
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int ncase;
	cin >> ncase;
	int ks = 1;
//^>v< 
	mm['^'] = 2;
	mm['v'] = 3;
	mm['<'] = 0;
	mm['>'] = 1;
	while (ncase--)
	{
		cin >> n >> m;
		fff = 0;
		ans = 0;
		MEM(flag, 0);
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				cin >> c[i][j];
			}
		}
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				if (c[i][j] != '.')
				{
					check(i, j, mm[c[i][j]]);
				}
			}
		}
		if (fff) printf("Case #%d: IMPOSSIBLE\n", ks++);
		else printf("Case #%d: %d\n", ks++, ans);
	}
	return 0;

}