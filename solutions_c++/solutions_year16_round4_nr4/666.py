#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <stack>
#include <cstdlib>
#include <algorithm>
#include <list>
#include <cassert>
#include <ctime>
#include <sstream>
#include <cmath>
#include <unordered_map>
#include <unordered_set>
#include <iomanip>
using namespace std;

#define sc(x) scanf("%d", &x)
#define sc2(x, y) scanf("%d%d", &x, &y)
#define sc_str(s) scanf("%s", s)
#define pr(x) printf("%d ", x)
#define nl() printf("\n")
#define mp(x, y) make_pair(x, y)
#define forn(i, a, b) for(int i=a; i<b; ++i)
#define ford(i, a, b) for(int i=b-1; i>=a; --i)
#define pb(x) push_back(x)
#define sz(x) (int)x.size()
#define X first
#define Y second

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<bool> vb;
typedef vector<vector<bool> > vvb;

double ans = 0;

bool check(int i, vector<int> &ar, vector<string> &v, vector<bool> &used)
{
	if (i == v.size()) return true;
	bool any = false;
	forn(j, 0, v.size())
		if(v[ar[i]][j]=='1' && !used[j])
		{
			any = true;
			used[j] = true;
			if (!check(i + 1, ar, v, used)) return false;
			used[j] = false;
		}
	return any;
}

void solve()
{
	int t;
	sc(t);
	forn(tt, 0, t)
	{
		int n;
		sc(n);
		vector<string> v(n);
		forn(i, 0, n)
			cin >> v[i];
		int nn = n*n;
		int ans = 1e9;
		forn(mask, 0, 1<<nn)
		{
			int cur = 0;
			vector<string> cv = v;
			forn(i, 0, n)
				forn(j, 0, n)
				if(v[i][j]=='0' && (mask & (1<<(i*n+j))))
				{
					cv[i][j] = '1';
					cur++;
				}
			vector<int> ar(n);
			forn(i, 0, n)
				ar[i] = i;
			bool flag = true;
			do
			{
				vector<bool> used(n, false);
				if (!check(0, ar, cv, used))
					flag = false;
			} while (next_permutation(ar.begin(), ar.end()));

			if(flag)
				ans = min(cur, ans);
		}


		
		printf("Case #%d: %d\n", tt + 1, ans);
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	solve();
	fprintf(stderr, "Time: %.2lf\n", (double)clock() / CLOCKS_PER_SEC);

	return 0;
}