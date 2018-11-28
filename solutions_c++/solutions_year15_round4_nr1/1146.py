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
#define mp make_pair
#define pb push_back
#define mt make_tuple
#define NAME ""

using namespace std;
	
typedef long long ll;
typedef long double ld;

const ld PI = acos(-1.0);
const int MAXN = 100001;
string s[MAXN];
int n, r, c;

bool go(int x, int y, int mx, int my)
{
	while (true)
	{
		x += mx;
		y += my;
		if ((x < 0) || (x >= r) || (y < 0) || (y >= c)) return false;
		if (s[x][y] != '.') return true;
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tst;
	cin >> tst;
	for (int tt = 0; tt < tst; tt++)
	{
		cin >> r >> c;
		cout << "Case #" << tt + 1 << ": ";
		for (int i = 0; i < r; i++) cin >> s[i];
		int ans = 0;
		for (int i = 0; i < r; i++)
		{
			for (int j = 0; j < c; j++)
			{
				if (s[i][j] == '.') continue;
				if ((s[i][j] == '^') && go(i, j, -1, 0)) continue;
				if ((s[i][j] == 'v') && go(i, j, 1, 0)) continue;
				if ((s[i][j] == '<') && go(i, j, 0, -1)) continue;
				if ((s[i][j] == '>') && go(i, j, 0, 1)) continue;
				ans++;
				if (go(i, j, -1, 0)) continue;
				if (go(i, j, 1, 0)) continue;
				if (go(i, j, 0, -1)) continue;
				if (go(i, j, 0, 1)) continue;
				ans = -MAXN;
			}
		}
		if (ans < 0) cout << "IMPOSSIBLE" << endl;
		else cout << ans << endl;
	}
	return 0;
}