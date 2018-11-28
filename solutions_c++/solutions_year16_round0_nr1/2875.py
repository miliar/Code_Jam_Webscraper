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

int go(int n)
{
	set < int > S;
	int s = 0;
	while (S.size() < 10)
	{
		s += n;
		int j = s;
		while (j)
		{
			S.insert(j % 10);
			j /= 10;
		}
	}

	return s;
}

int main()
{
	int T;
	scanf("%d", &T);
	REP(c, T)
	{
		int N;
		scanf("%d", &N);
		if (N == 0) printf("Case #%d: INSOMNIA\n", c + 1);
		else printf("Case #%d: %d\n", c + 1, go(N));
	}
	return 0;
}