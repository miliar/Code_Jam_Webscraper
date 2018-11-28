#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <cassert>
#include <numeric>
#include <string>
#include <cstring>
#include <cmath>
using namespace std;

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) 42
#endif

typedef long long int int64;


//const int mod = (int) 1e9 + 7;

const int maxn = 20;
bool solvedH[maxn];
int ans[maxn][maxn];


struct State
{
	int n, w;
	vector <int> cL, cR, remL, remR;
	State() : n(), w(), cL(), cR(), remL(), remR() {}
	State(int _n, int _w, const vector <int> &_cL, const vector <int> &_cR, const vector <int> &_remL, const vector <int> &_remR) 
		: n(_n), w(_w), cL(_cL), cR(_cR), remL(_remL), remR(_remR) {}
	State(const vector <int> &v) : n( (int) v.size() ), w(1), cL(v), cR(v), remL(v), remR(v) 
	{
		for (int i = 1; i < n; i++)
		{
			if (v[i] == v[i - 1] )
			{
				remL[i]--;
				remL[i - 1]--;
				remR[i]--;
				remR[i - 1]--;
			}
		}
	}

	State operator + (vector <int> &v) const
	{
		vector <int> lr = remR, rr = v;
		for (int i = 1; i < n; i++)
		{
			if (v[i] == v[i - 1] )
			{
				rr[i]--;
				rr[i - 1]--;
			}
		}
		for (int i = 0; i < n; i++)
		{
			if (cR[i] == v[i] )
			{
				rr[i]--;
				lr[i]--;
			}
		}
		State anss = State(n, w + 1, cL, v, remL, rr);
		if (w == 1)
			anss.remL = lr;
		else
		{
			for (int i = 0; i < n; i++)
				if (lr[i] != 0)
				{
					anss.n = -1;
					break;
				}
		}
		return anss;
	}

	bool good()
	{
		bool st = (w == 1);
		for (int i = 0; i < n; i++)
		{
			if (remR[i] < 0 || remL[i] < 0)
				return false;
			if (st && (remR[i] > 2 || remL[i] > 2) )
				return false;
			if (!st && (remR[i] > 1 || remL[i] > 1) )
				return false;
		}
		return true;
	}

	bool isFin()
	{
		for (int i = 0; i < n; i++)
			if (cL[i] == cR[i] )
			{
				if (remL[i] != 1 || remR[i] != 1)
					return false;
			}
			else
			{
				if (remL[i] != 0 || remR[i] != 0)
					return false;
			}
		return true;
	}

	void print()
	{
		return;
		eprintf("----- w = %d --------\n", w);
		for (int i = 0; i < n; i++)
			eprintf("%d ", cL[i] );
		eprintf("\n");
		for (int i = 0; i < n; i++)
			eprintf("%d ", remL[i] );
		eprintf("\n\n");
		for (int i = 0; i < n; i++)
			eprintf("%d ", cR[i] );
		eprintf("\n");
		for (int i = 0; i < n; i++)
			eprintf("%d ", remR[i] );
		eprintf("\n");
		eprintf("-------------\n");
		eprintf("\n\n\n");
	}

	bool operator < (const State &A) const
	{
		if (cL != A.cL)
			return cL < A.cL;
		if (cR != A.cR)
			return cR < A.cR;
		if (remL != A.remL)
			return remL < A.remL;
		if (remL != A.remL)
			return remL < A.remL;
		return false;
	}
};

map <State, int> dp[maxn];

vector <vector <int> > turns;

void genAll(int n, vector <int> &v)
{
	if (n == 0)
	{
		State s = State(v);
		if (s.good() )
		{
			dp[0][s] = 1;
			turns.push_back(v);
		}
		return;
	}
	for (int i = 1; i <= 3; i++)
	{
		v.push_back(i);
		genAll(n - 1, v);
		v.pop_back();
	}
}

void solveH(int n)
{
	if (solvedH[n] )
		return;
	for (int i = 0; i < maxn; i++)
		dp[i].clear();
	turns.clear();

	solvedH[n] = true;

	vector <int> xxv;
	genAll(n, xxv);

	for (int i = 0; i < maxn - 1; i++)
	{
		for (auto it : dp[i] )
		{
			State cur = it.first;
			int cnt = it.second;
			//eprintf("i = %d, cnt = %d\n", i, cnt);
			cur.print();
			if (cur.isFin() )
			{
				ans[n][i + 1] += cnt;
			}

			for (auto v : turns)
			{
				State nx = cur + v;
				if (nx.n == -1 || !nx.good() )
					continue;
				dp[i + 1][nx] += cnt;
			}
		}
	}
}

const int MX = 6; //TODO

void test()
{
	for (int h = 2; h <= MX; h++)
	{
		solveH(h);
		for (int l = 1; l < maxn; l++)
		{
			for (int i = 1; i < l; i++)
			{
				if (l % i != 0)
					continue;
				ans[h][l] -= ans[h][i] * i;
			}
			if (ans[h][l] % l != 0)
				throw 42;
			ans[h][l] /= l;	
			eprintf("%5d", ans[h][l] );
		}
		eprintf("\n");
	}
}

void solve()
{
	int r, c;
	scanf("%d%d", &r, &c);
	solveH(r);
	int answ = 0;
	for (int i = 1; i <= c; i++)
		if (c % i == 0)
			answ += ans[r][i];
	printf("%d\n", answ);
}

void multitest()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++)
	{
		printf("Case #%d: ", i);
		eprintf("Case #%d .. %d\n", i, n);
		solve();
	}


}

int main(int argc, char **)
{
	test();
//	return 0;

	if (argc == 1)
		multitest();
	else
		solve();

	return 0;
}


