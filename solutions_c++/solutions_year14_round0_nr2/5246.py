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

#define MR 1000000010
double t[2];

double result(double C, double F, double X)
{
	double res = X/2.0;
	t[0] = 0;
	bool sel = 1;
	FOR(i,1,MR)	//ile fabryk
	{
		t[sel] = t[!sel] + C/((i-1)*F+2);
		if(t[sel] > res) break;
		res = min(res, t[sel]+X/(i*F+2));
		sel = !sel;
	}
	return res;
}

int main()
{
	int T;
	scanf("%d", &T);
	REP(c,T)
	{
		double C, F, X;
		scanf("%lf%lf%lf", &C, &F, &X);
		printf("Case #%d: %.7lf\n", c+1, result(C,F,X));
	}
	return 0;
}