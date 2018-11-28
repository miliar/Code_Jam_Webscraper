#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <iostream>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <vector>
#include <algorithm>
#include <iterator>
#include <cassert>

using namespace std;

typedef long long llong;
typedef long double ldouble;
typedef pair<int, int> pint;
typedef pair<double, double> pdouble;
typedef vector<int> vint;
typedef vector<double> vdouble;
typedef vector<llong> vllong;

#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define SIZE(x) (int)x.size()
#define ALL(c) c.begin(),c.end()

#define ST first
#define ND second
#define INF 1000000000
#define INFL 1000000000000000000LL
#define EPS 1e-5

void print(vector<char> &v, int R, int C)
{
	REP(i, R)
	{
		REP(j, C)
			printf("%c", v[i * C + j]);
		puts("");
	}
}

void check(vector<char> &v, int R, int C, int M, int F)
{
	int m = 0, f = 0, x = 0;
	REP(i, R)
		REP(j, C)
			if(v[i * C + j] == 'c')
				x++;
			else if(v[i * C + j] == '.')
				f++;
			else if(v[i * C + j] == '*')
				m++;

	assert(x == 1);
	assert(f == F - 1);
	assert(m == M);
}

bool solve(vector<char> &v, int R, int C, int F)
{
	FOR(r1, 2, R) FOR(r2, 0, R - r1) FOR(r3, 0, R - r1 - r2)
	FOR(c1, 2, C) FOR(c2, 0, C - c1) FOR(c3, 0, C - c1 - c2)
		if(c1 * (r1 + r2 + r3) + c2 * (r1 + r2) + c3 * r1 == F)
		{
			REP(i, r1 + r2 + r3)
				REP(j, c1)
					v[i * C + j] = '.';
			REP(i, r1 + r2)
				REP(j, c1 + c2)
					v[i * C + j] = '.';
			REP(i, r1)
				REP(j, c1 + c2 + c3)
					v[i * C + j] = '.';
			v[0] = 'c';
			return true;
		}
	return false;
}

int main()
{
	int N;
	
	cin >> N;
	REP(t, N)
	{
		int R, C, M, F;
		cin >> R >> C >> M, F = R * C - M;
		vector<char> data(R * C, '*');

		printf("Case #%d:\n", t + 1);
		if(F == 1)
		{
			data[0] = 'c';
			print(data, R, C);
		}
		else if(R == 1 || C == 1)
		{
			REP(i, F)
				data[i] = '.';
			data[0] = 'c';
			print(data, R, C);
		}
		else
		{
			if(solve(data, R, C, F))
				print(data, R, C);
			else
			{
				puts("Impossible");
				continue;
			}
		}
		check(data, R, C, M, F);
		// check2(data, R, C, M, F);
	}
	
	return 0;
}