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

llong max_position(llong p, llong l, llong v, llong k)
{
	// cout << p << " " << l << " " << k << endl;
	if(k == 0)
		return p;
	if(k == l - 1)
		return p + l - 1;
	
	return max_position(p, l / 2, v, (k + 1) / 2);
}

llong max_binary(llong L, llong P)
{	
	llong low = 0, high = L - 1, mid;
	while(low + 1 != high)
	{
		mid = (low + high) / 2;
		if(max_position(0, L, mid, mid) < P)
			low = mid;
		else
			high = mid;
	}

	return low;
}

llong min_position(llong p, llong l, llong v, llong k)
{
	if(k == 0)
		return p;
	if(k == l - 1)
		return p + l - 1;
	
	return min_position(p + l / 2, l / 2, v, (k - 1) / 2);
}

llong min_binary(llong L, llong P)
{	
	llong low = 0, high = L - 1, mid;
	while(low + 1 != high)
	{
		mid = (low + high) / 2;
		if(min_position(0, L, mid, mid) < P)
			low = mid;
		else
			high = mid;
	}

	return low;
}

int main()
{
	int T;
	
	cin >> T;
	REP(t, T)
	{
		llong N, P, L;
		cin >> N >> P, L = 1 << N;
		
		llong a = P == L ? L - 1 : min_binary(L, P), b = P == L ? L - 1 : max_binary(L, P);
		
		printf("Case #%d: %lld %lld\n", t + 1, a, b);
	}
	
	return 0;
}