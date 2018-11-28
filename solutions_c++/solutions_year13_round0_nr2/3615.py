#pragma comment(linker, "/STACK:128777216")
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <vector>
#include <memory.h>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <cstring>
#include <string.h>
#include <math.h>
#include <queue>
#include <stack>
#include <cassert>

#define forn(i,n) for (int i = 0; i < (int)n; i++)
#define fornd(i, n) for (int i = (int)n - 1; i >= 0; i--)
#define forab(i,a,b) for (int i = (int)a; i <= (int)b; i++)
#define forba(i,b,a) for (int i = (int)b; i >= (int)a; i--)
#define zero(a) memset (a, 0, sizeof (a))
#define _(a, val) memset (a, val, sizeof (a))
#define pb push_back
#define mp make_pair
#define all(v) (v).begin(), (v).end()
typedef long long ll;
typedef unsigned long long ull;

const ll LINF= 1000000000000000000LL;
const int INF = 1000000000;
const long double eps = 1e-9;
const long double PI = 3.1415926535897932384626433832795l;

using namespace std;

void prepare (string s)
{
#ifdef _DEBUG
	freopen ("input.txt", "r", stdin);
	freopen ("output.txt", "w", stdout);
#else
	if (s.length() != 0)
	{
		freopen ((s + ".in").c_str(), "r", stdin);
		freopen ((s + ".out").c_str(), "w", stdout);
	}
#endif
}

const int NMAX = 100100;
int a[100][100], n, m,
	row[100], col[100];

int main ()
{
	prepare ("");

	int T = 0;
	cin >> T;

	forn(l, T)
	{
		zero(row);
		zero(col);

		cin >> n >> m;
		forn(i, n)
		{
			forn(j, m) 
			{
				cin >> a[i][j];
				row[i] = max(row[i], a[i][j]);
				col[j] = max(col[j], a[i][j]);
			}
		}

		bool check = true;
		forn(i, n)
		{
			forn(j, m)
			{
				if (row[i] > a[i][j] && col[j] > a[i][j])
				{
					check = false;
					break;
				}
			}
			if (!check) break;
		}

		cout << "Case #" << l+1 << ": " << (check ? "YES" : "NO") << endl;
	}

	return 0;
}