#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>

#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <bitset>
#include <utility>
#include <functional>
#include <string>
#include <algorithm>

#include <cstring>
#include <cstdio>
#include <memory.h>
#include <ctime>
#include <cassert>
#include <cmath>
using namespace std;

//#pragma comment(linker, "/STACK:66777216")

#define forn(i,n) for(int i = 0; i < int(n); i++)
#define ford(i,n) for(int i = int(n) - 1; i >= 0; i--)
#define fore(i,a,b) for(int i = int(a); i <= int(b); i++)
#define foreach(it,a) for(__typeof((a).begin()) it = (a).begin(); it != (a).end(); it++)

#define mp make_pair
#define pb push_back
#define L(s) ((int)((s).size()))
#define sq(x) ((x)*(x))
#define sign(x) ( ((x) > 0) ? 1 : -1)

#define ll long long
#define INF 1000000000
#define eps e-8

ll res;
ll fres;

bool go2(string cur)
{
	int n = cur.size();
	int was[30];
	memset(was, 0, sizeof(30));
	char last = cur[0];
	was[last - 'a'] = 1;
	forn(i, n)
	{
		if (cur[i] != last)
		{
			if (was[cur[i] - 'a'] == 1)
				return false;
			was[cur[i] - 'a'] = 1;
			last = cur[i];
		}
	}
	return true;
}

bool go(string cur)
{
	int n = cur.size();
	int was[30];
	memset(was, 0, sizeof(30));
	char last = cur[0];
	was[last - 'a'] = 1;
	forn(i, n)
	{
		if (cur[i] != last)
		{
			if (was[cur[i] - 'a'] == 1)
				return false;
			was[cur[i] - 'a'] = 1;
			last = cur[i];
		}
	}
	res++;
	return true;
}
void check(vector<string> &vin, vector<bool> &used, string curs, int cur, int size, int n)
{
	if (size == n)
	{
		go(curs);
	}
	if (!go2(curs))
		return;
	forn(i, n)
	{
		if (!used[i])
		{
			used[i] = true;
			string cursn = curs;
			cursn.append(vin[i]);
			check(vin, used, cursn, i, size + 1, n);
			used[i] = false;
		}
	}
}
//dfs(group, used, vim, vs);
void dfs(vector<string> &group, vector<bool> &used, vector<string> &vim, vector<vector<bool> > &vs, int cur)
{
	used[cur] = true;
	group.push_back(vim[cur]);
	int n = used.size();
	forn(c, 30)
	{
		if (vs[cur][c])
		{
			forn(i, n)
			{
				if (!used[i] && vs[i][c])
				{
					dfs(group, used, vim, vs, i);
				}
			}
		}
	}
}

void solveB()
{
	int T;
	cin >> T;
	forn(t, T)
	{
		int n;
		cin >> n;
		vector<string> vin(n);
		forn(i, n)
			cin >> vin[i];
		res = 0;
		vector<string> vim(n);
		forn(i, n)
		{
			string s = vin[i];
			string sm;
			int m = s.size();
			sm += s[0];
			for (int j = 1; j < m; ++j)
			{
				if (s[j] != s[j - 1])
					sm += s[j];
			}
			vim[i] = sm;
		}
		bool done = false;

		forn(i, n)
		{
			if (!go(vim[i]))
			{
				fres = 0;
				done = true;
				break;
			}
		}
		if (!done)
		{
			vector<vector<bool> > vs(n);
			forn(i, n)
				vs[i].resize(30, false);
			forn(i, n)
			{
				int np = vim[i].size();
				forn(j, np)
					vs[i][vim[i][j] - 'a'] = true;
			}
			vector<bool> used(n, false);
			fres = 1;
			int g = 0;
			forn(i, n)
			{
				if (!used[i])
				{
					g++;
					vector<string> group;
					dfs(group, used, vim, vs, i);
					int nn = group.size();
					res = 0;
					forn(s, nn)
					{
						vector<bool> used2(nn, false);
						used2[s] = true;
						string curs = group[s];
						check(group, used2, curs, s, 1, nn);
					}
					fres *= res;
					if (fres == 0)
					{
						done = true;
						break;
					}
				}
			}
			for (int k = 1; k <= g; ++k)
				fres *= k;
		}
		/*forn(s, n)
		{
			vector<bool> used(n, false);
			used[s] = true;
			string curs = vin[s];
			check(vin, used, curs, s, 1, n);
		}*/
		cout << "Case #" << t + 1 << ": " << fres << endl;
	}
}

int main() {

#ifdef diametralis
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	solveB();

#ifdef diametralis
	cerr << "Time == " << clock() << endl;
#endif
}