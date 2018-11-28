#include <iostream>
#include <cstdio>
#include <set>
using namespace std;

int a[60][60];

void solve(int r, int c, int m)
{
	bool reversed = r > c;
	if(reversed) r^=c, c^=r, r^=c;
	if(r == 1)
	{
		for(int i = 0; i < c; ++i)
		{
			if(m)
			{
				a[0][i] = 1;
				--m;
			}
			else
			{
				a[0][i] = 0;
			}
		}
		a[0][c - 1] = 2;
	}
	else
	{
		int p = max(0, m - (r - 2) * (c - 2));
		int l = r * c - m;
		if((r == 2 && p % 2 && l != 1) || (l == 5) || (l == 7) || (l == 2) || (l == 3))
		{
			cout << "Impossible\n";
			return;
		}
		int rr = r - 2, cc = c - 2;
		for(int i = 0; i < rr; ++i)
			for(int j = 0; j < cc; ++j)
			{
				if(m)
				{
					a[i][j] = 1;
					--m;
				}
				else
				{
					a[i][j] = 0;
				}
			}
		if (m % 2 && l != 1)
		{
			++m;
			a[rr - 1][cc - 1] = 0;
		}
		
		for(int i = 0; i < rr - 1; ++i)
		{
			if(m)
			{
				a[i][cc] = 1;
				--m;
				a[i][cc + 1] = 1;
				--m;
			}
			else
			{
				a[i][cc] = 0;
				a[i][cc + 1] = 0;
			}
		}
		for(int j = 0; j < cc - 1; ++j)
		{
			if(m)
			{
				a[rr][j] = 1;
				--m;
				a[rr + 1][j] = 1;
				--m;
			}
			else
			{
				a[rr][j] = 0;
				a[rr + 1][j] = 0;
			}
		}
		
		if(m && rr)
		{
			a[rr - 1][cc] = 1;
			--m;
			a[rr - 1][cc + 1] = 1;
			--m;
		}
		else
		{
			a[rr - 1][cc] = 0;
			a[rr - 1][cc + 1] = 0;
		}
		if(m && cc)
		{
			a[rr][cc - 1] = 1;
			--m;
			a[rr + 1][cc - 1] = 1;
			--m;
		}
		else
		{
			a[rr][cc - 1] = 0;
			a[rr + 1][cc - 1] = 0;
		}
		
		
		
		a[rr][cc] = 0;
		a[rr][cc + 1] = 0;
		a[rr + 1][cc] = 0;
		a[rr + 1][cc + 1] = 2;
		if (l == 1)
		{
			a[rr][cc] = 1;
			a[rr][cc + 1] = 1;
			a[rr + 1][cc] = 1;
		}
	}
	if(reversed)
	{
		for(int j = 0; j < c; ++j)
		{
			for(int i = 0; i < r; ++i)
			{
				if (a[i][j] == 0)
				{
					cout << ".";
				}
				else if (a[i][j] == 1)
				{
					cout << "*";
				}
				else
				{
					cout << "c";
				}
			}
			cout << endl;
		}
	}
	else
	{	
		for(int i = 0; i < r; ++i)
		{
			for(int j = 0; j < c; ++j)
			{
				if (a[i][j] == 0)
				{
					cout << ".";
				}
				else if (a[i][j] == 1)
				{
					cout << "*";
				}
				else
				{
					cout << "c";
				}
			}
			cout << endl;
		}
	}
}

int main()
{
	freopen("C.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int T;
	cin >> T;
	for(int t = 0; t < T; ++t)
	{
		int r, c, m;
		cin >> r >> c >> m;
		cout << "Case #" << t + 1 << ":\n";
		solve(r, c, m);
	}
	return 0;
}

