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
				cerr << ((a[i][j]==0)?('.'):('#'));
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
		if (n() != x.n() || m()!=x.m()) return false;
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
	void mirrorH()
	{
		FOR(i, 0, n()/2)
			FOR(j, 0, m())
				swap(a[i][j], a[n() - i - 1][j]);
	}
	void mirrorV()
	{
		FOR(j, 0, m() / 2)
			FOR(i, 0, n())
				swap(a[i][j], a[i][m() - j - 1]);
	}
};

vector< matrix > S[7];

void init()
{
	VI one(2,1);
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
				{
					// TODO
				}
		}
		cerr << "sz=" << S[i].size() << endl;
		for(auto it = S[i].begin(); it != S[i].end(); ++it)
			(*it).show();
	}
}

string solve(int x, int n, int m)
{
	if (!(x < 7)) return lose;

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

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	//freopen("teams.in", "r", stdin);
	//freopen("teams.out", "w", stdout);

	//init();

	/*FOR(x, 1, 5)
		FOR(i, 1, 5)
		FOR(j, 1, 5)
		cerr << x << " " << i << " " << j << " " << solve(x, i, j) << endl;
	*/
	int t;
	cin >> t;
	FOR(test,0,t)
	{
		int x, n, m;
		cin >> x >> n >> m;
		cout << "Case #" << test+1 << ": " << solve(x,n,m) << endl;
		cerr << test + 1 << endl;
	}

	return 0;
}