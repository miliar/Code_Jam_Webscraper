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

ldouble compute(int n, ldouble C, ldouble F, ldouble X)
{
	if(n < 0)
		n = 0;
	ldouble Ti = 0;
	REP(i, n)
		Ti += 1 / (2 + i * F);
	return X / (2 + n * F) + C * Ti;
}

void check(int n, ldouble C, ldouble F, ldouble X)
{
	ldouble minus = compute(n - 1, C, F, X), out = compute(n, C, F, X), plus = compute(n + 1, C, F, X);
	if(out > minus || out > plus)
	{
		cout << n - 2 << " " << compute(n - 2, C, F, X) << endl;
		cout << n - 1 << " " << compute(n - 1, C, F, X) << endl;
		cout << n << " " << compute(n, C, F, X) << endl;
		cout << n + 1 << " " << compute(n + 1, C, F, X) << endl;
		cout << n + 2 << " " << compute(n + 2, C, F, X) << endl;
	}
}

int main()
{
	int N;
	
	cin >> N;
	REP(t, N)
	{
		ldouble C, F, X;
		cin >> C >> F >> X;
		
		int n = (X * F - 2) / (F * C) - 1;

		ldouble minus = compute(n - 1, C, F, X), out = compute(n, C, F, X), plus = compute(n + 1, C, F, X);
		if(out > plus)
			n++, out = plus;
		else if(out > minus)
			n--, out = minus;
		check(n, C, F, X);
		
		printf("Case #%d: %.7Lf\n", t + 1, out);
	}
	
	return 0;
}