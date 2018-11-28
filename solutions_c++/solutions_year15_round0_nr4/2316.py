#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:133217728")
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

typedef pair<int, int> PII;
typedef vector<int> VI;

#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
#define RFOR(i, a, b) for(int i = (a) - 1; i >= (b); --i)
#define ALL(a) (a).begin(),(a).end()
#define PB push_back
#define MP make_pair
#define pi acos(-1.0)

const int MOD = 1000000007;
const int INF = 2000000007;

const string lose = "RICHARD";
const string win = "GABRIEL";

int dx[] = { 1, 0, -1, 0 };
int dy[] = { 0, 1, 0, -1 };

int X;

class matrix
{
public:
	vector< VI > a;
	matrix(){}
	matrix(const matrix & x)
	{
		FOR(i, 0, x.n())
		{
			VI r;
			FOR(j, 0, x.m())
			{
				r.PB(x.a[i][j]);
			}
			a.push_back(r);
		}
	}
	void show() const
	{
		cerr << "matrix " << n() << "x" << m() << endl;
		FOR(i, 0, n())
		{
			FOR(j, 0, m())
				cerr << ((a[i][j] == 0) ? ('.') : ('#'));
			cerr << endl;
		}
	}
	int n() const
	{
		return a.size();
	}
	int m() const
	{
		return a[0].size();
	}
	bool operator==(const matrix & x)
	{
		if (n()*m() != x.n()*x.m()) return false;

		matrix o0(x);
		matrix o1(o0); o1.turn90();
		matrix o2(o1); o2.turn90();
		matrix o3(o2); o3.turn90();

		matrix m0(o0); m0.mirror();
		matrix m1(o1); m1.mirror();
		matrix m2(o2); m2.mirror();
		matrix m3(o3); m3.mirror();

		return (equals(o0) ||
			equals(o1) ||
			equals(o2) ||
			equals(o3) ||

			equals(m0) ||
			equals(m1) ||
			equals(m2) ||
			equals(m3));
	}
	bool equals(const matrix & x) const
	{
		if (n() != x.n() || m() != x.m()) return false;
		FOR(i, 0, n())
			FOR(j, 0, m())
			if (a[i][j] != x.a[i][j]) return false;
		return true;
	}
	void turn90()
	{
		matrix temp(*this);
		FOR(i, 0, n())
			a[i].clear();
		a.clear();
		FOR(j, 0, temp.m())
		{
			VI r;
			RFOR(i, temp.n(), 0)
				r.PB(temp.a[i][j]);
			a.PB(r);
		}
	}
	void mirror()
	{
		FOR(j, 0, m() / 2)
			FOR(i, 0, n())
			swap(a[i][j], a[i][m() - j - 1]);
	}
	void putCell(int x, int y)
	{
		if (x < 0)
		{
			VI v(m(), 0);
			v[y] = 1;
			a.insert(a.begin(), v);
			return;
		}
		if (x >= n())
		{
			VI v(m(), 0);
			v[y] = 1;
			a.PB(v);
			return;
		}
		if (y < 0)
		{
			FOR(i, 0, n())
				a[i].insert(a[i].begin(), 0);
			a[x][0] = 1;
			return;
		}
		if (y >= m())
		{
			FOR(i, 0, n())
				a[i].push_back(0);
			a[x].back() = 1;
			return;
		}
		a[x][y] = 1;
	}
};

class Dfs
{
public:
	int C;
	int N, M;
	int a[20][20];
	bool used[20][20];
	bool ok(int x, int y)
	{
		return (x >= 0 && y >= 0 && x < N && y < M);
	}
	void clear(int n, int m){
		N = n;
		M = m;
		FOR(i, 0, n)
			FOR(j, 0, m)
			{
				a[i][j] = 0;
				used[i][j] = 0;
			}
		C = 0;
	}
	void putMatrix(const matrix & m, int x, int y)
	{
		FOR(i, 0, m.n())
			FOR(j, 0, m.m())
			a[i + x][j + y] = m.a[i][j];
	}
	void dfs(int px, int py)
	{
		++C;
		used[px][py] = 1;
		FOR(i, 0, 4)
		{
			int tx = px + dx[i];
			int ty = py + dy[i];
			if (!ok(tx, ty)) continue;
			if (used[tx][ty]) continue;
			if (a[tx][ty] == 1) continue;
			dfs(tx, ty);
		}
	}
};

Dfs DFS;
vector< matrix > S[7];

void init()
{
	VI one(1,1);
	matrix m;
	m.a.PB(one);
	S[1].PB(m);
	m.show();

	FOR(i, 2, 7)
	{
		cerr << "    i=" << i << endl;
		for (auto it = S[i-1].begin(); it != S[i-1].end(); ++it)
		{
			matrix c = *it;
			FOR(ii,0,c.n())
				FOR(jj, 0, c.m())
				if (c.a[ii][jj]==1)
					FOR(d,0,4)
				{
					int tox = ii + dx[d];
					int toy = jj + dy[d];
					if (tox < 0 || tox >= c.n() || toy < 0 || toy >= c.m() || c.a[tox][toy] == 0)
					{
						matrix o(c);
						o.putCell(tox, toy);
						bool was = 0;
						for (auto it2 = S[i].begin(); it2 != S[i].end(); ++it2)
						{
							if ((*it2) == o) was = 1;
						}
						if (!was) S[i].PB(o);
					}					
				}
		}
		cerr << "sz=" << S[i].size() << endl;
		//for(auto it = S[i].begin(); it != S[i].end(); ++it)	(*it).show();
	}
	cerr << "done\n" << endl;
}

bool covers(const matrix & a, int n, int m)
{
	if (a.n() > n) return false;
	if (a.m() > m) return false;
	if (a.n() < n - 1 && a.m() < m - 1) return true;

	FOR(i, 0, n - a.n()+1)
		FOR(j, 0, m - a.m() + 1)
		{
			bool may = true;
			DFS.clear(n, m);
			DFS.putMatrix(a, i, j);
			FOR(ii,0,n)
				FOR(jj,0,m)
				if (DFS.a[ii][jj] == 0 && !DFS.used[ii][jj])
				{
					DFS.dfs(ii, jj);
					if (DFS.C%X != 0)
						may=false;
				}
			if (may) return true;
		}
	return !true;
}

bool can_cover(const matrix & a, int n, int m)
{
	matrix o0(a);
	matrix o1(o0); o1.turn90();
	matrix o2(o1); o2.turn90();
	matrix o3(o2); o3.turn90();

	matrix m0(o0); m0.mirror();
	matrix m1(o1); m1.mirror();
	matrix m2(o2); m2.mirror();
	matrix m3(o3); m3.mirror();

	return  (covers(o0,n,m) ||
			covers(o1,n,m) ||
			covers(o2,n,m) ||
			covers(o3,n,m) ||
					
			covers(m0,n,m) ||
			covers(m1,n,m) ||
			covers(m2,n,m) ||
			covers(m3,n,m));
}

string SOLVE(int x, int n, int m)
{
	X = x;
	if (!(x < 7)) return lose;
	if ((n*m) % x != 0) return lose;
	for (auto it = S[x].begin(); it != S[x].end(); ++it)
	{
		if (!can_cover(*it, n, m))
		{
			//it->show();
			return lose;
		}
	}
	return win;
}

string solve(int x, int n, int m)
{
	if (x == 1) return win;
	if (x == 2) return ((n*m % 2 == 0) ? (win) : (lose));
	if (x == 3){
		if (n*m % 3 != 0) return lose;
		if (n+m-3 == 1) return lose;
		else
			return win;
	}
	if (x == 4)
	{
		if (max(n, m) < 4) return lose;
		int e = n + m - 4;
		if (e < 3) return lose;
		return win;
	}
	throw "ops";
}

void performance()
{
	string x;
	FOR(i, 0, 1000)
	{
		x += SOLVE(rand() % 6 + 1, rand() % 20 + 1, rand() % 20 + 1);
		cerr << i << endl;
	}
	cerr << x << endl;
}

void test()
{
	//performance();
	freopen("input.txt", "r", stdin);

	int t;
	cin >> t;
	FOR(test, 0, t)
	{
		int x, n, m;
		cin >> x >> n >> m;
		if (solve(x, n, m) != SOLVE(x, n, m))
		{
			cerr << x << " " << n << " " << m << endl;
			cerr << "solve=" << solve(x, n, m) << endl;
			cerr << "SOLVE=" << SOLVE(x, n, m) << endl;
		}
	}

}

void grid(int n)
{
	string s;
	cerr << "x=" << n << endl;
	FOR(i, 1, 21)
	{
		FOR(j, 0, 20)
		{
			string res = SOLVE(n, i, j + 1);
			if (res == win)
				s += '1';
			else
				s += '0';
		}
		s += '\n';
	}
	cerr << s << endl << endl;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	//freopen("teams.in", "r", stdin);
	//freopen("teams.out", "w", stdout);

	init();

	//test(); return 0;

	//FOR(i, 1, 8)
	//	grid(i);

	//return 0;

	/*FOR(x, 1, 5)
		FOR(i, 1, 5)
		FOR(j, 1, 5)
		cerr << x << " " << i << " " << j << " " << SOLVE(x, i, j) << endl;
	*/

	int t;
	cin >> t;
	FOR(test,0,t)
	{
		int x, n, m;
		cin >> x >> n >> m;
		cout << "Case #" << test+1 << ": " << SOLVE(x,n,m) << endl;
		cerr << test + 1 << endl;
	}

	return 0;
}