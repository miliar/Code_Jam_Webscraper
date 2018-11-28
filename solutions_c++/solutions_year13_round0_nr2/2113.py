#if 1
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <functional>
#include <cstring>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <ctime>
#include <cassert>
#include <sstream>
#include <iostream>
#include <bitset>

using namespace std;

typedef long long LL;
typedef long double LD;
typedef pair<int , int> pii;
typedef vector <int> veci;
typedef vector <veci> graph;
const LD eps = 1e-9;
const LD pi = acos(-1.0);
const int inf = 1000 * 1000 * 1000;
const LL inf64 = LL(inf) * inf;

#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define iss istringstream
#define oss ostringstream
#define dbg(x) {cerr << #x << " = " << x << endl;}
#define dbgv(x) {cerr << #x << " ={"; for (int _i = 0; _i < x.size(); _i++) {if (_i) cerr << ", "; cerr << x[_i];} cerr << "}" << endl;}
#define NAME "problem"

string T(int test) { ostringstream os; os << "Case #" << test << ":"; return os.str(); }

void solve(int test)
{
	int n, m;
	scanf("%d%d", &n, &m);
	vector< vector<int> > a(n, vector<int>(m));
	for(int i = 0; i < n; ++i)
		for(int j = 0; j < m; ++j)
			scanf("%d", &a[i][j]);
	vector< int > row(n), col(m);
	for(int i = 0; i < n; ++i)
		for(int j = 0; j < m; ++j)
		{
			row[i] = max(row[i], a[i][j]);
			col[j] = max(col[j], a[i][j]);
		}

	bool ok = true;
	for(int i = 0; i < n; ++i)
		for(int j = 0; j < m; ++j)
			if(a[i][j] >= row[i] || a[i][j] >= col[j])
				;
			else
				ok = false;

	cout << T(test) << " " << (ok ? "YES" : "NO") << endl;
}

int main()
{
	//freopen("input.txt", "r", stdin); //freopen("output.txt", "w", stdout);
	//freopen(NAME ".in","r",stdin);freopen(NAME ".out","w",stdout);

	int tests;
	scanf("%d", &tests);
	for(int test = 1; test <= tests; ++test)
		solve(test);

	return 0;
}
/*************************
*************************/
#endif
