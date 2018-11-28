#pragma warning (disable : 4996)

#include <stdlib.h>
#include <iostream>
#include <vector>
#include <string>
#include <assert.h>
#include <stack>
#include <algorithm>
#include <ios>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <queue>
#include <set>
#include <functional>
#include <cmath>
#include <sstream>
#include <map>
#include <memory.h>
#include <stdio.h>
#include <cassert>
#include <string.h>

#define forn(i , n) for (int i = 0; i < n; ++i)
#define down(i, n) for (int i = n - 1; i >= 0; --i)


using namespace std;

typedef unsigned long long int u64;
typedef long long int i64;
typedef vector<int> vint;
typedef pair<int, int> pint;
typedef pair<i64, i64> pi64;


#define FILE_NAME "file"

#define CONTEST "bees"

const int inf = 2000000000;


struct Node
{
	int p;
	int h;
	Node()
	{
		p = -1;
		h = 1;
	}
};



int find(vector<Node> & arr, int v)
{
	if (arr[v].p == -1)
		return v;
	return arr[v].p = find(arr, arr[v].p);

}

void uni(vector<Node> & arr, int a, int b)
{
	a = find(arr, a);
	b = find(arr, b);
	if (arr[a].h < arr[b].h)
	{
		arr[a].p = b;
		arr[b].h += arr[a].h;
	}
	else
	{
		arr[b].p = a;
		arr[a].h += arr[b].h;
	}
}

struct Rebro
{
	int a, b, v;

	bool operator< (const Rebro & b) const
	{
		return v < b.v;
	}

};



bool check(vector<vint> & arr, int r, int c, int m)
{
	int fr = r * c - m;
	forn(i, r)
	{
		forn(j, c)
		{
			if (arr[i][j] == 1)
				--m;
		}
	}
	if (m != 0)
	{
		return false;
	}
	return true;

	
}




bool solve(vector<vint> & arr, int r, int c, int m)
{
	int fr = r * c - m;
	if (fr == 1)
	{
		forn(i, r)
		{
			forn(j, c)
			{
				arr[i][j] = 1;
			}
		}
		arr[0][0] = -1;
		m = 0;
		return true;
	}
	else if (r == 1 || c == 1)
	{
		m = 0;
		if (r == 1)
		{

			forn(i, fr)
			{
				arr[0][i] = 0;
			}
			for (int i = fr; i < c; ++i)
			{
				arr[0][i] = 1;
			}
			arr[0][0] = -1;
		}
		else
		{
			forn(i, fr)
			{
				arr[i][0] = 0;
			}
			for (int i = fr; i < r; ++i)
			{
				arr[i][0] = 1;
			}
			arr[0][0] = -1;
		}
		return true;
	}
	else if (c > 2 && r > 2)
	{
		arr[0][0] = -1;
		arr[1][0] = -2;
		arr[0][1] = -2;
		arr[1][1] = -2;
		bool change = false;
		int h = r;
		for (int i = r - 1; i > 1; --i)
		{
			if (m > c)
			{
				forn(j, c)
				{
					arr[i][j] = 1;
				}
				m -= c;
				--h;
				change = true;
			}
		}
		int w = c;
		for (int j = c - 1; j > 1; --j)
		{
			if (m > h)
			{
				forn(i, h)
				{
					arr[i][j] = 1;
				}
				m -= h;
				--w;
				change = true;
			}
		}
		if (change)
			return solve(arr, h, w, m);
		else
		{
			if (m <= (h + w - 1 - 4))
			{
				int i = h - 1;
				for (int j = w - 1; j > 1; --j)
				{
					if (m > 0)
					{
						--m;
						arr[i][j] = 1;
					}
				}
				int j = w - 1;
				for (int i = h - 2; i > 1; --i)
				{
					if (m > 0)
					{
						--m;
						arr[i][j] = 1;
					}
				}
				return m == 0;
			}
			else
			{
				return false;
			}
		}


	}
	else
	{
		arr[0][0] = -1;
		arr[1][0] = -2;
		arr[0][1] = -2;
		arr[1][1] = -2;
		if (m % 2 == 0)
		{
			if (r == 2)
			{
				down(j, c)
				{
					forn(i, 2)
					{
						if (m > 0 && arr[i][j] == 0)
						{
							arr[i][j] = 1;
							--m;
						}
					}
				}

			}
			else
			{
				down(i, r)
				{
					forn(j, 2)
					{
						if (m > 0 && arr[i][j] == 0)
						{
							arr[i][j] = 1;
							--m;
						}
					}
				}
			}
			return m == 0;
		}
		else
		{
			return false;
		}

	}
}







int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout << fixed << setprecision(9);
#ifdef FILE_INPUT
	freopen(FILE_NAME ".in", "r", stdin);
	freopen(FILE_NAME ".out", "w", stdout);
#else
	freopen(CONTEST ".in", "r", stdin);
	freopen(CONTEST ".out", "w", stdout);
#endif
	int T;
	cin >> T;
	forn(t, T)
	{
		int ans1 = 0, ans2 = 0;
		int n;
		cin >> n;
		vector<double> a(n), b(n);
		forn(i, n)
		{
			cin >> a[i];
		}
		forn(i, n)
		{
			cin >> b[i];
		}
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());
		{
			int a1 = 0, a2 = n - 1;
			int b1 = 0, b2 = n - 1;
			forn(i, n)
			{
				if (a[a2] > b[b2])
				{
					ans2++;
					a2--;
					b1++;
				}
				else
				{
					b2--;
					a2--;
				}
			}
		}
		{
			int a1 = 0, a2 = n - 1;
			int b1 = 0, b2 = n - 1;
			forn(i, n)
			{
				if (a[a1] > b[b1])
				{
					ans1++;
					a1++;
					b1++;
				}
				else
				{
					b2--;
					a1++;
				}
			}
		}



		cout << "Case #" << t + 1 << ": " << ans1 << " " << ans2 << "\n";
		
		
	}

	return 0;

}