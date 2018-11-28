#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <cstdio>
#include <map>
#include <hash_map>
#include <string>
#include <iomanip>
#include <vector>
#include <memory.h>
#include <queue>
#include <set>
#include <stack> 
#include <algorithm>
#include <math.h>
#include <sstream>
#include <functional>
#include <bitset>
#pragma comment (linker, "/STACK:167177216")
using namespace std;
#define mems(A, val) memset(A, val, sizeof(A))
#define mp(a, b) make_pair(a, b)
#define all(B) (B).begin(), (B).end()
#define forn(it, from, to) for(int it = from; it < to; ++it)
#define forit (it, coll) for(auto it = coll.begin(); it != coll.end(); ++it)
const int MAX = 2147483647;
const int MAXN = 1000000 + 10000;
typedef long long LL;
const LL MOD = 1000000000 + 7;
int n,m;
bool used[4][4];
bool dfs(vector<string> &s, vector<vector<int> > &good, int x, int y, char dir)
{
	if (x < 0 || x >= n || y < 0 || y >= m) return false;
	if (used[x][y]) return true;
	used[x][y] = true;
	if (dir == '.') return true;
	if (s[x][y] != '.') dir = s[x][y];
	if (dir == 'v')
	{
		return dfs(s, good, x + 1, y, dir);
	}
	if (dir == '>')
	{
		return dfs(s, good, x , y + 1, dir);
	}
	if (dir == '<')
	{
		return dfs(s, good, x, y - 1, dir);
	}
	if (dir == '^')
	{
		return dfs(s, good, x - 1, y, dir);
	}
}

bool check(vector<string> &s)
{
	bool bb = true;
	vector<vector<int> > good(s.size(), vector<int> (s[0].size(), 0));
	for(int i = 0; i < n; ++i)
	{
		for(int j = 0; j < m; ++j)
		{
			mems(used,false);
			bb &= dfs(s,good,i,j, s[i][j]);
		}
	}

	return bb;
}
int ans = 100;
void rec(vector<string> &s, int changed, int x, int y)
{
	if (changed > 12) return;
	if (x == n) return;
	if (check(s))
	{
		ans = min(ans, changed);
		return;
	}

	if (s[x][y] == '.') rec(s, changed, x + (y + 1) / m, (y + 1) % m);
	else
	{
		char cur = s[x][y];
		if (s[x][y] != 'v')
		{
			s[x][y] = 'v';
			rec(s, changed + 1, x + (y + 1) / m, (y + 1) % m);
			s[x][y] = cur;
		}
		if (s[x][y] != '>')
		{
			s[x][y] = '>';
			rec(s, changed + 1, x + (y + 1) / m, (y + 1) % m);
			s[x][y] = cur;
		}
		if (s[x][y] != '<')
		{
			s[x][y] = '<';
			rec(s, changed + 1, x + (y + 1) / m, (y + 1) % m);
			s[x][y] = cur;
		}
		if (s[x][y] != '^')
		{
			s[x][y] = '^';
			rec(s, changed + 1, x + (y + 1) / m, (y + 1) % m);
			s[x][y] = cur;
		}

		rec(s, changed, x + (y + 1) / m, (y + 1) % m);
	}
}

int main()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#else
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	//freopen("f.in", "r", stdin); freopen("f.out", "w", stdout);
#endif
	ios::sync_with_stdio(0);
	int T;
	cin>>T;
	forn(ttt,0,T)
	{
		ans = 0;
		cin>>n>>m;
		vector<string> s(n);
		forn(i,0,n)
		{
			cin>>s[i];
		}
		bool br = false;
		for(int i = 0; i < n; ++i)
		{
			if (br) break;
			for(int j = 0; j < m; ++j)
			{
				if (br) break;
				if (s[i][j] == '.') continue;

				int pts = 0;
				for(int k = 0; k < m; ++k)
				{
					pts += s[i][k] == '.';
				}

				for(int k = 0; k < n; ++k)
				{
					pts += s[k][j] == '.';
				}

				if (pts == n + m - 2)
				{
					br = true;
					break;
				}

				if (s[i][j] == '>')
				{
					bool good = false;
					for(int k = j + 1; k < m; ++k)
					{
						if (s[i][k] != '.') {good = true;break;}
					}

					if (!good) ans++;
				}
				if (s[i][j] == '<')
				{
					bool good = false;
					for(int k = j - 1; k >=0; --k)
					{
						if (s[i][k] != '.') {good = true;break;}
					}

					if (!good) ans++;
				}
				if (s[i][j] == '^')
				{
					bool good = false;
					for(int k = i - 1; k >=0; --k)
					{
						if (s[k][j] != '.') {good = true;break;}
					}

					if (!good) ans++;
				}
				if (s[i][j] == 'v')
				{
					bool good = false;
					for(int k = i + 1; k < n; ++k)
					{
						if (s[k][j] != '.') {good = true;break;}
					}

					if (!good) ans++;
				}
			}
		}

		//rec(s, 0, 0, 0);
		if (br)cout<<"Case #"<<ttt + 1<<": IMPOSSIBLE"<<endl;else
			cout<<"Case #"<<ttt + 1<<": "<<ans<<endl;
	}
	return 0;
}