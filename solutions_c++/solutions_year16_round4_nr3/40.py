#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <string>
#include <cstring>
#include <ctime>
#include <cassert>
#include <queue>
#include <stack>
#include <bitset>
#define y1 y11
#define fs first
#define sc second
#define mp make_pair
#define pb push_back
#define mt make_tuple
#define NAME ""

using namespace std;
	
typedef long long ll;
typedef long double ld;

const ld PI = acos(-1.0);

const int MAXN = 302;

int n, m;
int mx[4] = {-1, 0, 1, 0};
int my[4] = {0, -1, 0, 1};
int a[MAXN][MAXN];
int x1[MAXN], y1[MAXN], d1[MAXN];
int x2[MAXN], y2[MAXN], d2[MAXN];
int cnt[MAXN][MAXN];
int f[MAXN];
int fn;

vector <int> pos;

void er(int x)
{
	pos.erase(pos.begin() + x);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	cin >> tests;
	cout.setf(ios::fixed);
	cout.precision(20);
	for (int test = 1; test <= tests; test++)
	{
		pos.clear();
		memset(a, 0, sizeof(a));
		cout << "Case #" << test << ":" << endl;
		int n, m;
		cin >> n >> m;
		for (int i = 1; i <= m; i++)
		{
			x1[i] = i, y1[i] = 1, d1[i] = 1;
			x2[i] = i, y2[i] = 0;
			int i2 = n + m + m - i + 1;
			x1[i2] = i, y1[i2] = n, d1[i2] = 3;
			x2[i2] = i, y2[i2] = n + 1;
		}
		for (int i = 1; i <= n; i++)
		{
			x1[m + i] = m, y1[m + i] = i, d1[m + i] = 2;
			x2[m + i] = m + 1, y2[m + i] = i;
			int i2 = 2 * (n + m) - i + 1;
			x1[i2] = 1, y1[i2] = i, d1[i2] = 0;
			x2[i2] = 0, y2[i2] = i;
		}
		for (int i = 1; i <= 2 * (n + m); i++) pos.push_back(i);
		for (int i = 1; i <= n + m; i++)
		{
			int a, b;
			cin >> a >> b;
			f[a] = b, f[b] = a;	
		}
		bool ok = true;
		for (int iter = 1; iter <= n + m; iter++)
		{
			int ps = pos.size();
			int di = -1;
			for (int i = 0; i < ps; i++)
			{
				if (f[pos[i]] == pos[(i + 1) % ps])
				{
					di = i;
					break;
				}
			}
			if (di == -1)
			{
				ok = false;
				break;
			}
			int vi = pos[di];
			er(max(di, (di + 1) % ps));
			er(min(di, (di + 1) % ps));
			di = vi;
			int cx = x1[di], cy = y1[di], cd = d1[di];
			//memset(cnt, 0, sizeof(cnt));
			while ((cx > 0) && (cx <= m) && (cy > 0) && (cy <= n))
			{
				//cnt[cx][cy]++;
				/*if (cnt[cx][cy] > 4)
				{
					cnt[cx][cy]++;
				}*/
				if (a[cy][cx] == 0)
				{
					if (cd % 2) a[cy][cx] = 3;
					else a[cy][cx] = 1;
				}
				cd = (a[cy][cx] + 4 - cd) % 4;
				cx += mx[cd], cy += my[cd];
				cd = (cd + 2) % 4;
			}
			di = f[di];
			if ((cx != x2[di]) || (cy != y2[di]))
			{
				ok = false;
				break;
			}
		}
		if (!ok)
		{
			cout << "IMPOSSIBLE" << endl;
		}
		else
		{
			for (int i = 1; i <= n; i++)
			{
				for (int j = 1; j <= m; j++)
				{
					if (a[i][j] == 1) cout << "/";
					else cout << "\\";
				}
				cout << endl;
			}
		}
	}
	return 0;
}