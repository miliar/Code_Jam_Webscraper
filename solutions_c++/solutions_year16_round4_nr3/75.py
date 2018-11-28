#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker,"/STACK:32000000")
#include <algorithm>
#include <numeric>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <cassert>

using namespace std;

#define REP(i,n) for (int i=0,_n=(n); i < _n; i++)
#define REPD(i,n) for (int i=(n)-1; i >= 0; i--)
#define FOR(i,a,b) for (int _b=(b), i=(a); i <= _b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))

#define CLEAR(x) memset(x,0,sizeof x);
#define CLEARA(x) memset(&x,0,sizeof x);
#define FILL(x,v) memset(x,v,sizeof x);
#define FILLA(x,v) memset(&x,v,sizeof x);

#define VAR(a,b) __typeof(b) a=(b)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)

#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 0x7fffffff
#define X first
#define Y second
#define pb push_back
#define SZ(c) (int)(c).size()
#define MP make_pair
#define eps 1.0e-11
const double pi = acos(-1.0);

typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;

typedef pair<PII,bool> Coord;
#define TOP false
#define LEFT true

#define ROW first
#define COL second

#define N 128
int r,c;
PII prs[N*4];
bool a[N][N];

Coord getc(int p)
{
	if (p < c)
		return MP(MP(0,p),TOP);
	p -= c;
	if (p < r)
		return MP(MP(p,c),LEFT);
	p -= r;
	if (p < c)
		return MP(MP(r,c-1-p),TOP);
	p -= c;
	assert(p < r);
	return MP(MP(r-1-p,0),LEFT);
}

bool u[N][N][2];

bool isEdge(Coord p)
{
	if (p.second == TOP)
		return p.first.ROW == 0 || p.first.ROW == r;
	else
		return p.first.COL == 0 || p.first.COL == c;
}

vector<Coord> neigh(Coord p)
{
	vector<Coord> res;
	if (p.second == TOP)
	{
		if (p.first.ROW > 0)
		{
			res.push_back(MP(PII(p.first.ROW-1, p.first.COL + (a[p.first.ROW-1][p.first.COL] ? 0 : +1)), LEFT));
		}
		if (p.first.ROW < r)
		{
			res.push_back(MP(PII(p.first.ROW, p.first.COL + (a[p.first.ROW][p.first.COL] ? 1 : 0)), LEFT));
		}
	}
	else
	{
		if (p.first.COL > 0)
		{
			res.push_back(MP(PII(p.first.ROW + (a[p.first.ROW][p.first.COL-1] ? 0 : +1), p.first.COL-1), TOP));
		}
		if (p.first.COL < c)
		{
			res.push_back(MP(PII(p.first.ROW + (a[p.first.ROW][p.first.COL] ? 1 : 0), p.first.COL), TOP));
		}
	}
	return res;
}

bool& get(Coord c)
{
	return u[c.first.ROW][c.first.COL][c.second?1:0];
}

bool checkpath(Coord st, Coord fn)
{
	CLEAR(u);
	queue<Coord> q;
	q.push(st);
	get(st) = true;
	while (!q.empty())
	{
		Coord p = q.front();
		q.pop();
		if (isEdge(p))
			if (p!=st && p!=fn) return false;
		vector<Coord> nnn = neigh(p);
		REP(j,SZ(nnn))
		{
			Coord pp = nnn[j];
			if (get(pp)) continue;
			get(pp) = true;
			q.push(pp);
		}
	}
	return get(fn);
}

bool check()
{
	REP(i,r+c)
	{
		if (!checkpath(getc(prs[i].X), getc(prs[i].Y)))
			return false;
	}
	return true;
}

bool brute()
{
	REP(mask,1<<(r*c))
	{
		REP(i,r) REP(j,c) a[i][j] = (mask&(1<<(i*c+j))) != 0;
		if (check())
		{
			REP(i,r)
			{
				REP(j,c) printf("%c",a[i][j]?'\\':'/');
				printf("\n");
			}
			return true;
		}
	}
	return false;
}

int main(int argc, char **argv)
{
	string FN = "C-small-attempt0";
	if (argc>1) FN = string(argv[1]);
	int shift = 0;
	if (argc>2) sscanf(argv[2],"%d",&shift);
	freopen((FN+".in").c_str(),"r",stdin);
	freopen((FN+".out").c_str(),"w",stdout);

	int tests;
	scanf("%d",&tests);
	for (int test = 1; test<=tests; test++)
	{
		fprintf(stderr,"=== %s : %d\n", FN.c_str(), test+shift);
		printf("Case #%d: ",test+shift);
		////////////////////////////////////////////////////////////
		printf("\n");
		scanf("%d%d",&r,&c);
		REP(i,r+c)
		{
			scanf("%d%d",&prs[i].X,&prs[i].Y);
			--prs[i].X;
			--prs[i].Y;
		}
		if (!brute()) {
			printf("IMPOSSIBLE\n");
		}
	}
	fprintf(stderr,"=== %s DONE\n", FN.c_str());
	return 0;
}