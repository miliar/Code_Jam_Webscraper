#include <iostream> 
#include <fstream> 
#include <cmath> 
#include <algorithm> 
#include <cassert> 
#include <string> 
#include <cstdlib> 
#include <cstdio> 
#include <vector> 
#include <map> 
#include <set> 

#define pb push_back 
#define mp make_pair 
#define float long double 
#define ll long long 
#define abracadabra next 
#define pii pair<int, int> 

using namespace std; 

const int dx[8] = {1, 1, 1, 0, -1, -1, -1, 0};
const int dy[8] = {1, 0, -1, -1, -1, 0, 1, 1};


char d[5][5], a[5][5], ans[5][5];
bool used[5][5], uused[5][5];
int r, c, m;

bool norm(int x, int y)
{
	return (x >= 0 && x < r && y >= 0 && y < c);
}

void print(int x, int y)
{
	for(int i = 0; i < r; i++)
	{
		for(int j = 0; j < c; j++)
		if (a[i][j] == 0)
			ans[i][j] = '.';
		else
			ans[i][j] = '*';
	}
	ans[x][y] = 'c';
	for(int i = 0; i < r; i++)
	{
		for(int j = 0; j < c; j++)
			cout << ans[i][j];
		cout << endl;
	}
}

int dfs(int x, int y)
{
	uused[x][y] = true;
	used[x][y] = true;
	if (d[x][y] > 0) return 1;
	int res = 1;
	for(int k = 0; k < 8; k++)
		if (norm(x + dx[k], y + dy[k]) && a[x + dx[k]][y + dy[k]] == 0 && !used[x + dx[k]][y + dy[k]]) {
			res += dfs(x + dx[k], y + dy[k]);
		}
	return res;
}

bool solve()
{
	for(int i = 0; i < r; i++)
		for(int j = 0; j < c; j++)
		{
			d[i][j] = 0;
			uused[i][j] = 0;
			for(int k = 0; k < 8; k++)
				if (norm(i + dx[k], j + dy[k]) && a[i + dx[k]][j + dy[k]]) {
					d[i][j]++;
					break;
				}
		}
	
	for(int i = 0; i < r; i++)
		for(int j = 0; j < c; j++)
		{
			if (!uused[i][j] && a[i][j] == 0)
			{
				memset(used, 0, sizeof(used));
				int t = dfs(i, j);
				if (t == r*c-m)
				{
					print(i, j);
					return true;
				}
			}
		}
	return false;
}

bool rec(int i, int j, int cur, int rem)
{
	if (cur == m)
	{
		return solve();
	}
	if (rem < m - cur)
		return false;
	if (j == c)
	{
		j = 0, i++;
	}
	if (i == r)
		return false;
	a[i][j] = 1;
	if (rec(i, j + 1, cur + 1, rem - 1)) {
		a[i][j] = 0;
		return true;
	}
	a[i][j] = 0;
	return rec(i, j + 1, cur, rem - 1);
}

int main(){ 
	
	int T;
	cin >> T;
	for(int qwe = 1; qwe <= T; qwe++)
		{
		
		printf("Case #%d:\n", qwe);
		cin >> r >> c >> m;
		if (!rec(0, 0, 0, r*c)) {
			cout << "Impossible\n";
		}
	}
	
	
	return 0; 
} 
