#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <utility>
#include <numeric>
#include <fstream>

using namespace std;

#define		ALL(c)	(c).begin(),(c).end()
#define		SZ(c)	int((c).size())
#define		LEN(s)	int((s).length())
#define		FOR(i,n)	for(int i=0;i<(n);++i)
#define		FORD(i,a,b)	for(int i=(a);i<=(b);++i)
#define		FORR(i,a,b)	for(int i=(b);i>=(a);--i)

typedef istringstream iss;
typedef ostringstream oss;
typedef long double ld;
typedef long long i64;
typedef pair<int,int> pii;

typedef vector<i64> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;

typedef vector<ld> vd;
typedef vector<vd> vvd;

typedef vector<string> vs;

const i64 d18 = 1000000000000000000LL;
const ld eps = 1e-9;
const ld pi = atan2(0.0, -1.0);
template<class T> T sqr(T a) { return a * a; }
i64 abs(i64 a) { return (a >= 0) ? a : -a; }

ofstream LOG("log.txt");

ifstream fin;
ofstream fout;

const i64 MOD = 1000002013;

struct evnt
{
	i64 pos;
	int idx, act;
	evnt() {}
	evnt(i64 _p, int _idx, int _a) : pos(_p), idx(_idx), act(_a) {}
	bool operator<(const evnt & r) const
	{
		return pos < r.pos || pos == r.pos && act < r.act;
	}
};

struct costs
{
	i64 N, p;
	int idx;
	costs() {};
	costs(i64 _N, i64 _p, int _i) : N(_N), p(_p), idx(_i) {}
	bool operator<(const costs & r) const
	{
		return N > r.N;
	}
};

i64 cost(i64 d, i64 N)
{
	i64 r = (N * N + N - 2) / 2;
	N -= d;
	r -= (N * N + N - 2) / 2;
	return r % MOD;
}

void solve_case(int TN)
{
	i64 N;
	int M;
	fin >> N >> M;
	vi a(M), b(M), p(M);
	i64 tot = 0;
	FOR(i, M) 
	{
		fin >> a[i] >> b[i] >> p[i];
		tot += p[i] * cost(b[i]-a[i], N);
		tot %= MOD;
	}

	deque<i64> cards;
	vector<evnt> ev;
	FOR(i, M)
	{
		ev.push_back(evnt(a[i], i, 0));
		ev.push_back(evnt(b[i], i, 1));
	}
	sort(ALL(ev));

	deque<costs> c;
	i64 ans = 0, prev = -1;
	FOR(i, SZ(ev))
	{
		evnt & cev = ev[i];
		if (cev.act == 0)
		{
			FOR(j, SZ(c))
			{
				costs & cst = c[j];
				ans += cst.p * cost(cev.pos - prev, cst.N);
				ans %= MOD;
				cst.N -= cev.pos - prev;
			}
			c.push_front(costs(N, p[cev.idx], cev.idx));
			prev = cev.pos;
		}
		else
		{
			FOR(j, SZ(c))
			{
				costs & cst = c[j];
				ans += cst.p * cost(cev.pos - prev, cst.N);
				ans %= MOD;
				cst.N -= cev.pos - prev;
			}
			int i1 = 0, i2 = SZ(c)-1;
			deque<costs> c1;
			while (i1 < i2)
			{
				if (c[i1].idx == cev.idx)
				{
					++i1; 
					continue;
				}
				if (c[i2].idx != cev.idx)
				{
					--i2;
					continue;
				}
				if (c[i1].p <= c[i2].p)
				{
					c[i1].N = c[i2].N;
					c[i2].p -= c[i1].p;
					++i1;
					if (c[i2].p == 0) --i2;
					continue;
				}
				c1.push_front(costs(c[i2].N, c[i2].p, c[i1].idx));
				c[i1].p -= c[i2].p;
				c[i2].p = 0;
				--i2;
				if (c[i1].p == 0) ++i1;
			}
			FOR(j, SZ(c))
			{
				if (c[j].idx != cev.idx)
					c1.push_front(c[j]);
			}
			sort(ALL(c1));
			c = c1;
			prev = cev.pos;
		}
	}

	ans = (tot - ans + MOD) % MOD;

	fout << "Case #" << TN << ": " << ans << endl;
	cout << "Case #" << TN << ": " << ans << endl;
}

int main()
{
	fin.open("A.in"); 
	fout.open("A.out");

	int T; 
	fin >> T;
	FOR(tt, T)
	{
		solve_case(tt+1);
	}

	return 0;	
}
