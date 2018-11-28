#define _USE_MATH_DEFINES 
#define _CRT_SECURE_NO_DEPRECATE 
#include <iostream> 
#include <cstdio> 
#include <cstdlib> 
#include <vector> 
#include <sstream> 
#include <string> 
#include <map> 
#include <set> 
#include <algorithm> 
#include <cmath> 
#include <cstring> 
#include <queue>
using namespace std; 
#pragma comment(linker, "/STACK:256000000") 
#define mp make_pair 
#define pb push_back 
#define all(C) (C).begin(), (C).end() 
#define sz(C) (int)(C).size() 
#define PRIME 1103 
#define PRIME1 31415 
typedef long long int64; 
typedef unsigned long long uint64; 
typedef pair<int, int> pii; 
typedef vector<int> vi; 
typedef vector<vector<int> > vvi; 
//------------------------------------------------------------ 
#define y1 asdf
#define y2 asdqwer
const int N = 110;
int n, m, q;
int h;
int r, c;
int was[N][N];
char mas[N][N];
int des[4][N][N];
char pat[] = {'^', '>', 'v', '<'};
int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};
int ok(int x, int y)
{
	if (x < 0 || y < 0 || x >= r || y >= c)
		return 0;
	return 1;
}

void solve()
{
	int ans = 0;
	cin >> r >> c;
	for(int i = 0; i < r; ++i)
		for(int j = 0; j < c; ++j)
			cin >> mas[i][j];

	memset(des, 0, sizeof des);
	for(int i = 0; i < r; ++i)
	{
		int q = 0;
		for(int j = 0; j < c; ++j)
		{
			if (mas[i][j] != '.')
			{
				des[3][i][j] = q;
				q = 1;
			}
		}
	}
	for(int i = 0; i < r; ++i)
	{
		int q = 0;
		for(int j = c - 1; j >= 0; --j)
		{
			if (mas[i][j] != '.')
			{
				des[1][i][j] = q;
				q = 1;
			}
		}
	}
	for(int j = 0; j < c; ++j)
	{
		int q = 0;
		for(int i = 0; i < r; ++i)
		{
			if (mas[i][j] != '.')
			{	
				des[0][i][j] = q;
				q = 1;
			}
		}
	}
	for(int j = 0; j < c; ++j)
	{
		int q = 0;
		for(int i = r - 1; i >= 0; --i)
		{
			if (mas[i][j] != '.')
			{
				des[2][i][j] = q;
				q = 1;
			}
		}
	}

	for(int i = 0; i < r; ++i)
	{
		for(int j = 0; j < c; ++j)
		{
			if (mas[i][j] == '.')
				continue;
			for(int k = 0; k < 4; ++k)
			{
				if (pat[k] != mas[i][j])
					continue;
				int q = 0;
				for(int t = 0; t < 4; ++t)
					q += des[t][i][j];
				
				if (!q)
				{
					cout << "IMPOSSIBLE" << endl;
					return;
				}
				if (!des[k][i][j])
					ans++;
			}
		}
	}
	cout << ans << endl;
}

int main()
{
 
#ifdef WIN32
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	for(int i = 0; i < t; ++i)
	{
		cout << "Case #" << i + 1 << ": ";
		solve();
	}
}