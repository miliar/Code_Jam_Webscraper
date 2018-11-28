#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <sstream>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <string>
#include <queue>
#include <bitset>		//UWAGA - w czasie kompilacji musi byc znany rozmiar wektora - nie mozna go zmienic
#include <cassert>
#include <iomanip>		//do setprecision
#include <ctime>
#include <complex>
using namespace std;

#define FOR(i,b,e) for(int i=(b);i<(e);++i)
#define FORQ(i,b,e) for(int i=(b);i<=(e);++i)
#define FORD(i,b,e) for(int i=(b)-1;i>=(e);--i)
#define REP(x, n) for(int x = 0; x < (n); ++x)

#define ST first
#define ND second
#define PB push_back
#define MP make_pair
#define LL long long
#define ULL unsigned LL
#define LD long double

const double pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342;

void go(int K, int C, int S)
{
	if (C == 1)
	{
		if (S < K)
		{
			printf("IMPOSSIBLE\n");
			return;
		}
		FORQ(i, 1, K) printf("%d ", i);
		printf("\n");
		return;
	}

	if (2 * S < K)
	{
		printf("IMPOSSIBLE\n");
		return;
	}

	LL k = 1;
	FOR(i, 1, C) k *= K;
	LL l = k;
	int sub = 0;
	while(K > 0)
	{
		printf("%lld ", l - sub);
		l += k;
		sub++;
		K -= 2;
	}
	printf("\n");
}

int main()
{
	int T;
	scanf("%d", &T);
	REP(c, T)
	{
		int K, C, S;
		scanf("%d%d%d", &K, &C, &S);
		printf("Case #%d: ", c+1);
		go(K, C, S);
	}
	return 0;
}