#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <ctime>
#include <cmath>
#include <string>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <string.h>
using namespace std;

#define pb push_back
#define rs resize
#define mp make_pair
#define inf 1e9
#define pi 3.1415926535897932384626433832795

typedef vector <int> vi;
typedef vector <vi> vvi;
typedef vector <vvi> vvvi;
typedef vector <vvvi> vvvvi;
typedef vector <bool> vb;
typedef vector <vb> vvb;
typedef vector <vvb> vvvb;
typedef vector <vvvb> vvvvb;
typedef long long ll;
typedef vector <ll> vl;
typedef vector <vl> vvl;
typedef vector <vvl> vvvl;
typedef vector <vvvl> vvvvl;
typedef pair <int, int> ii;
typedef vector <ii> vii;
typedef vector <vii> vvii;
typedef pair <int, ll> il;
typedef vector <il> vil;
typedef vector <vil> vvil;
typedef pair <ll, int> li;
typedef vector <li> vli;
typedef vector <vli> vvli;
typedef set <int> si;
typedef set <li> sli;
typedef set <il> sil;
typedef vector <string> vs;
typedef vector <vs> vvs;
typedef vector <vvs> vvvs;
typedef map <string, int> msi;
typedef map <char, int> mci;
typedef long double ld;
typedef vector <ld> vd;
typedef vector <vd> vvd;

void solve()
{
	int r, c, m;
	cin >> r >> c >> m;
	//cout << r << ' ' << c << ' ' << m << endl;
	if (r * c == m + 1)
	{
		for (int i = 0; i < r; ++i)
		{
			for (int j = 0; j < c; ++j)
				if (i == 0 && j == 0)
					cout << 'c';
				else
					cout << '*';
			cout << endl;
		}
		return ;
	}
	if (r == 1)
	{
		cout << 'c';
		for (int i = 0; i < c - m - 1; ++i)
			cout << '.';
		for (int i = 0; i < m; ++i)
			cout << '*';
		cout << endl;
		return ;
	}
	if (c == 1)
	{
		cout << 'c' << endl;
		for (int i = 0; i < r - m - 1; ++i)
			cout << '.' << endl;
		for (int i = 0; i < m; ++i)
			cout << '*' << endl;
		return ;
	}
	if (m > r * c - 4 && m != r * c - 1)
	{
		cout << "Impossible\n";
		return ;
	}
	if (r == 2)
	{
		if (m % 2 == 0)
		{
			cout << 'c';
			for (int i = 0; i < c - m / 2 - 1; ++i)
				cout << '.';
			for (int i = 0; i < m / 2; i++)
				cout << '*';
			cout << endl;
			for (int i = 0; i < c - m / 2; ++i)
				cout << '.';
			for (int i = 0; i < m / 2; ++i)
				cout << '*';
			cout << endl;
			return ;
		}
		if (r * c - m != 1)
		{
			cout << "Impossible\n";
			return ;
		}
		cout << 'c';
		for (int i = 1; i < c; ++i)
			cout << '*';
		cout << endl;
		for (int i = 0; i < c; ++i)
			cout << '*';
		cout << endl;
		return ;
	}
	if (c == 2)
	{
		if (m % 2 == 0)
		{
			cout << "c.\n";
			for (int i = 0; i < r - m / 2 - 1; ++i)
				cout << "..\n";
			for (int i = 0; i < m / 2; i++)
				cout << "**\n";
			return ;
		}
		if (r * c - m != 1)
		{
			cout << "Impossible\n";
			return ;
		}
		cout << "c*\n";
		for (int i = 1; i < c; ++i)
			cout << "**\n";
		return ;
	}
	if ((r * c - m) % 2 == 0)
	{
		if (r * c - m == 2)
		{
			cout << "Impossible\n";
			return ;
		}
		vector <vector <char> > a(r, vector <char> (c, '*'));
		a[0][0] = 'c';
		a[0][1] = a[1][0] = a[1][1] = '.';
		int x = (r * c - 4);
		for (int i = 2; i < c && x > m; ++i)
		{
			a[0][i] = a[1][i] = '.';
			x -= 2;
		}
		for (int i = 2; i < r && x > m; ++i)
			for (int j = 0; j + 1 < c && x > m; j += 2)
			{
				a[i][j] = a[i][j + 1] = '.';
				x -= 2;
			}
		for (int i = 2; i < r && x > m; ++i)
			if (a[i][c - 1] == '*')
			{
				a[i][c - 1] = '.';
				x--;
			}
		for (int i = 0; i < r; ++i)
		{
			for (int j = 0; j < c; ++j)
				cout << a[i][j];
			cout << endl;
		}
		return ;
	}
	if (r * c - m < 9)
	{
		cout << "Impossible\n";
		return ;
	}
	vector <vector <char> > a(r, vector <char> (c, '*'));
	for (int i = 0; i < 3; ++i)
		for (int j = 0; j < 3; ++j)
			a[i][j] = '.';
	a[0][0] = 'c';
	int x = r * c - 3 * 3;
	if (c % 2 != 0)
	{
		for (int i = 3; i < c && x > m; ++i)
		{
			a[0][i] = a[1][i] = '.';
			x -= 2;
		}
		for (int i = 3; i < c && x > m; i += 2)
		{
			a[2][i] = a[2][i + 1] = '.';
			x -= 2;
		}
		if (x == m)
		{
			for (int i = 0; i < r; ++i)
			{
				for (int j = 0; j < c; ++j)
					cout << a[i][j];
				cout << endl;
			}
			return ;
		}
		if ((x - m) % c != 1)
		{
			for (int i = 3; i < r && x > m; ++i)
				for (int j = 0; j < c && x > m; ++j)
				{
					a[i][j] = '.';
					x--;
				}
			for (int i = 0; i < r; ++i)
			{
				for (int j = 0; j < c; ++j)
					cout << a[i][j];
				cout << endl;
			}
			return ;
		}
		else
		{
			for (int i = 3; i + 1 < r && x > m; i += 2)
			{
				for (int j = 0; j < c - 1 && x > m; j += 2)
				{
					a[i][j] = a[i][j + 1] = '.';
					x -= 2;
				}
				for (int j = 0; j < c - 1 && x > m; j += 2)
				{
					a[i + 1][j] = a[i + 1][j + 1] = '.';
					x -= 2;
				}
				if (x > m)
				{
					a[i][c - 1] = a[i + 1][c - 1] = '.';
					x -= 2;
				}
			}
			for (int i = 0; i < c && x > m; ++i)
				if (a[r - 1][i] == '*')
				{
					a[r - 1][i] = '.';
					x--;
				}
			for (int i = 0; i < r; ++i)
			{
				for (int j = 0; j < c; ++j)
					cout << a[i][j];
				cout << endl;
			}
			return ;
		}
		return ;
	}
	for (int i = 3; i < c && x > m; ++i)
	{
		a[0][i] = a[1][i] = '.';
		x -= 2;
	}
	for (int i = 3; i < c - 2 && x > m ; i += 2)
	{
		a[2][i] = a[2][i + 1] = '.';
		x -= 2;
	}
	for (int i = 3; i < r && x > m; ++i)
		for (int j = 0; j < c - 2 && x > m; j += 2)
		{
			a[i][j] = a[i][j + 1] = '.';
			x -= 2;
		}
	for (int i = 3; i + 1 < r && x > m; i += 2)
	{
		a[i][c - 2] = a[i + 1][c - 2] = '.';
		x -= 2;
	}
	for (int i = 2; i < r - 2 && x > m; i += 2)
	{
		a[i][c - 1] = a[i + 1][c - 1] = '.';
		x -= 2;
	}
	if (x > m)
	{
		a[r - 1][c - 2] = a[r - 2][c - 1] = '.';
		x -= 2;
	}
	for (int i = 0; i < r; ++i)
	{
		for (int j = 0; j < c; ++j)
			cout << a[i][j];
		cout << endl;
	}
	return ;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i)
	{
		cout << "Case #" << i + 1 << ":\n";
		solve();
	}
}