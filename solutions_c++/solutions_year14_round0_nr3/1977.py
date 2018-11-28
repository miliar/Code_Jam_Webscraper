//Besmellah
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
#define X first
#define Y second
#define pb push_back
#define SQR(x) ((x) * (x))
#define SZ(x) ((int)((x).size()))
#define ALL(x) (x).begin(), (x).end()
#define debug(x) cerr << #x << " = " << x << endl
#define FOR(i, a, n) for(__typeof(n) i = (a); i <= (n); i++)
#define FORD(i, n, a) for(__typeof(n) i = (n); i >= (a); i--)
#define INF (1000 * 1000 * 1000)
#define MAXN 100010

struct Table
{
	int a[6][6], row, col;
} t;

int mark[6][6], vis;

void check(int x, int y, Table &t)
{
	//cout << x << " - " << y << endl;
	mark[x][y] = 1;
	vis++;
	int cnt = 0;
	FOR (x2, x - 1, x + 1)
		FOR (y2, y - 1, y + 1)
			if (x2 >= 1 && x2 <= t.col && y2 >= 1 && y2 <= t.row)
				cnt += t.a[x2][y2];
	//debug(cnt);
	if (cnt != 0)
		return;
	FOR (x2, x - 1, x + 1)
		FOR (y2, y - 1, y + 1)
			if (x2 >= 1 && x2 <= t.col && y2 >= 1 && y2 <= t.row)
				if (!mark[x2][y2] && t.a[x2][y2] == 0)
					check(x2, y2, t);
}

inline void printTable(Table &t)
{
	FOR (y, 1, t.row)
	{
		FOR (x, 1, t.col)
		{
			if (x == 1 && y == 1)
				cout << "c";
			else if (t.a[x][y] == 1)
				cout << "*";
			//else if (mark[x][y] == 1)
				//cout << "m";
			else
				cout << ".";
		}
		cout << endl;
	}
}

void build(int h, Table &t)
{
	memset(t.a, 0, sizeof t.a);
	int x = 1;
	int y = 1;
	while (h > 0)
	{
		t.a[x][y] = h % 2;
		h /= 2;
		x++;
		if (x > t.col)
		{
			x = 1;
			y++;
		}
	}
}

int tests;

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin >> tests;
	FOR (tt, 1, tests)
	{
		int r, c, m;
		cin >> r >> c >> m;
		t.row = r;
		t.col = c;
		cout << "Case #" << tt << ": " << endl;
		int tmp = (1 << (r * c)) - 1;
		bool found = false;
		FOR (mask, 0, tmp)
			if (mask % 2 == 0 && __builtin_popcount(mask) == m)
			{
				//debug(mask);
				vis = 0;
				build(mask, t);
				memset(mark, 0, sizeof mark);
				check(1, 1, t);
				if (vis == r * c - m)
				{
					printTable(t);
					found = true;
					break;
				}
			}
		//debug("next!");
		if (!found)
			cout << "Impossible" << endl;
	}
	return 0;
}