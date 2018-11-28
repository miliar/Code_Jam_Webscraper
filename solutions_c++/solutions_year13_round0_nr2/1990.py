/**											Be name Khoda											**/
#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <map>
#include <vector>
#include <list>
#include <set>
#include <queue>
#include <deque>
#include <algorithm>
#include <bitset>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <memory.h>
using namespace std;

#define ll long long
#define un unsigned
#define pii pair<int, int>
#define pb push_back
#define mp make_pair
#define VAL(x) #x << " = " << x << "   "
#define SQR(a) ((a) * (a))
#define SZ(x) ((int) x.size())
#define ALL(x) x.begin(), x.end()
#define CLR(x, a) memset(x, a, sizeof x)
#define FOREACH(i, x) for(__typeof((x).begin()) i = (x).begin(); i != (x).end(); i ++)
#define X first
#define Y second
#define SAL cerr << "Salam!\n"
#define PI (3.141592654)

//#define cout fout
//#define cin fin

//ifstream fin("problem.in");
//ofstream fout("problem.out");

const int MAXN = 100 * 1 + 10, INF = 1e9 + 10;

int a[MAXN][MAXN], row[MAXN], col[MAXN];

int main ()
{
	ios::sync_with_stdio(false);
	int tc;
	cin >> tc;
	for (int t = 1; t <= tc; t ++)
	{
		int n, m;
		cin >> n >> m;
		for (int i = 0; i < n; i ++)
			for (int j = 0; j < m; j ++)
				cin >> a[i][j];
		for (int i = 0; i < n; i ++)
		{
			row[i] = a[i][0];
			for (int j = 1; j < m; j ++)
				row[i] = max(row[i], a[i][j]);
		}
		for (int i = 0; i < m; i ++)
		{
			col[i] = a[0][i];
			for (int j = 1; j < n; j ++)
				col[i] = max(col[i], a[j][i]);
		}
		bool ans = true;
		for (int i = 0; i < n; i ++)
			for (int j = 0; j < m; j ++)
				if (a[i][j] < row[i] && a[i][j] < col[j])
					ans = false;
		cout << "Case #" << t << ": ";
		if (ans) cout << "YES\n";
		else cout << "NO\n";
	}
	return 0;
}

