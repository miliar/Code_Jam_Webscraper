#pragma comment(linker, "/STACK:167177216")

#include <stdio.h>
#include <stack>
#include <deque>
#include <math.h>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <string>
#include <memory.h>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <time.h>
#include <bitset>
using namespace std;

#define mp make_pair
#define pb push_back
#define pii pair<int, int>
#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define x first
#define y second

typedef long long li;
typedef long double ld;
typedef unsigned long long uli;

const int INF = 1e9;
const ld eps = 1e-12;
const li mod = INF + 7;
const li INF64 = (li)(INF) * (li)(INF);

const int ddx[] = {-1, 1, 1, -1};
const int ddy[] = {1, 1, -1, -1};
const int dx[] = {-1, -1, 0, 1, 1, 1, 0, -1};
const int dy[] = {0, 1, 1, 1, 0, -1, -1, -1};
const int dx4[] = {-1, 0, 1, 0};
const int dy4[] = {0, 1, 0, -1};
const int dxh[] = {-2, -2, -1, 1, 2, 2, 1, -1};
const int dyh[] = {1, -1, -2, -2, -1, 1, 2, 2};
const string dirs[] = {"RIGHT", "UP", "LEFT", "DOWN"};

bool a[7][7];
bool good[7][7];
int n, m, cnt;

bool in(int i, int j, int n, int m)
{
	return i >= 1 && i <= n && j >= 1 && j <= m;
}

void solve()
{
	cin >> n >> m >> cnt;
	//n = 5, m = 5, cnt = 20;
	int must = n * m - cnt;
	if(must == 1)
	{
		for(int i = 1; i < n; i++)
		{
			for(int j = 1; j <= m; j++)
				cout << '*';
			cout << endl;
		}
		//cout << endl;
		for(int j = 1; j < m; j++)
			cout << '*';
		cout << 'c' << endl;
		return;
	}

	for(int mask = 0; mask < (1 << n * m); mask++)
	{
		int curcnt = 0;
		for(int i = 0; i < n * m; i++)
			if(mask & (1 << i))
				curcnt++;
		if(curcnt != cnt)
			continue;
		
		for(int i = 1; i <= 6; i++)
			for(int j = 1; j <= 6; j++)
				a[i][j] = good[i][j] = false;

		for(int i = 0; i < n * m; i++)
			if(mask & (1 << i))
			{
				int val = i + 1;
				int x = val / m + 1;
				if(val % m == 0)
					x--;
				int y = val - (x - 1) * m;
				a[x][y] = true;
			}

			/*cout << "mask == " << mask << endl;
			for(int i = 1; i <= n; i++)
			{
				for(int j = 1; j <= m; j++)
				{
					if(a[i][j])
						cout << '*';
					else
						cout << '.';
				}
				cout << endl;
			}*/

		for(int sx = 1; sx <= n; sx++)
			for(int sy = 1; sy <= m; sy++)
				if(!a[sx][sy])
				{
					for(int i = 1; i <= 6; i++)
						for(int j = 1; j <= 6; j++)
							good[i][j] = false;
					int kol = 0;
					forn(k, 8)
					{
						int ni = sx + dx[k];
						int nj = sy + dy[k];
						if(!a[ni][nj])
							kol++;
						else
							break;
					}
					//if(mask == 4)
						//cout << "kol == " << kol << endl;
					if(kol == 8)
					{
						int curkol = 0;
						queue<pair<int, int>> q;
						good[sx][sy] = true;
						q.push(mp(sx, sy));
						bool ok = true;
						while(!q.empty())
						{
							if(!ok)
								break;
							pair<int, int> v = q.front();
							q.pop();
							curkol++;
							bool can = true;
							forn(k, 8)
							{
								int ni = v.x + dx[k];
								int nj = v.y + dy[k];
								if(in(ni, nj, n, m) && a[ni][nj] == true)
									can = false;
							}
							forn(k, 8)
							{
								int ni = v.x + dx[k];
								int nj = v.y + dy[k];
								if(!in(ni, nj, n, m))
									continue;
								//if(a[ni][nj])
								//{
									//ok = false;
									//break;
								//}

								//bool can = true;

								if(!good[ni][nj] && !a[ni][nj] && can)
								{
									good[ni][nj] = true;
									q.push(mp(ni, nj));
								}
							}
						}

						if(ok && curkol == must)
						{
							for(int i = 1; i <= n; i++)
							{
								for(int j = 1; j <= m; j++)
								{
									if(sx == i && sy == j)
										cout << 'c';
									else
										if(a[i][j])
											cout << '*';
										else
											cout << '.';
								}
								cout << endl;
							}
							return;
						}
					}
				}
	}
	cout << "Impossible" << endl;
	return;
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ios_base::sync_with_stdio(false);
	int tests;
	cin >> tests;
	//tests = 230;
	forn(test, tests)
	{
		cout << "Case #" << test + 1 << ": " << endl;
		solve();
	}
	return 0;
}
