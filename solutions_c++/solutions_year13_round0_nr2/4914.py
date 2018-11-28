// .... .... .... !

#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cassert>

#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>

#include <cstdio>
#include <cstring>

using namespace std;

#define rep(i, n) for (int i = 0, _n = (int)(n); i < _n; i++)
#define fer(i, x, n) for (int i = (int)(x), _n = (int)(n); i < _n; i++)
#define rof(i, n, x) for (int i = (int)(n), _x = (int)(x); i-- > _x; )
#define fch(i, x) for (__typeof(x.begin()) i = x.begin(); i != x.end(); i++)
#define sz(x) (int((x).size()))
#define X first
#define Y second
#define pb push_back

typedef long long ll;
typedef pair <int, int> pii;

////////////////////////////////////////////////////////////////////////////////

const int maxn = 100 + 100;

int tt, tc = 1;
int n, m;
int a[maxn][maxn];
int r[maxn], c[maxn];


int main()
{
	ios::sync_with_stdio (false);

	for (cin >> tt; tc <= tt; tc++)
	{
		rep (i, maxn) r[i] = c[i] = -1;
		
		cin >> n >> m;
		rep (i, n) rep (j, m)
		{
			cin >> a[i][j];
			r[i] = max (r[i], a[i][j]);
			c[j] = max (c[j], a[i][j]);
		}
		bool ok = true;
		rep (i, n) rep (j, m)
			if (min (r[i], c[j]) > a[i][j])
				ok = false;
		cout << "Case #" << tc << ": " << (ok ? "YES" : "NO") << endl;
	}


	{ int _; cin >> _; return 0; }
}
