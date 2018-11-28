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

#define MR 110
int t[MR][MR], N, M, tN[MR], tM[MR];

string result()
{	
	REP(i,N)
	{
		int maxv = 0;
		REP(j,M) maxv = max(maxv, t[i][j]);
		tN[i] = maxv;
	}
	REP(i,M)
	{
		int maxv = 0;
		REP(j,N) maxv = max(maxv, t[j][i]);
		tM[i] = maxv;
	}
	REP(i,N)REP(j,M) if(t[i][j] < min(tN[i], tM[j])) return "NO";
	return "YES";
}

int main()
{
	int T;
	scanf("%d", &T);
	REP(c,T)
	{
		scanf("%d%d", &N, &M);
		REP(i,N)REP(j,M) scanf("%d", &t[i][j]);
		printf("Case #%d: %s\n", c+1, result().c_str());
	}
	return 0;
}