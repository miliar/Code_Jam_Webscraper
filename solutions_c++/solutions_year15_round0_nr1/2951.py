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

#define MR 1010

char t[MR];

int go(int D)
{
	int res = 0;
	int v = t[0]-'0';
	FORQ(i,1,D)
	{
		if(v < i)
		{
			res += i-v;
			v = i;
		}
		v += t[i]-'0';
	}
	return res;
}

int main()
{
	int T;
	scanf("%d", &T);
	REP(c,T)
	{
		int D;
		scanf("%d%s", &D, t);
		int res = go(D);
		printf("Case #%d: ", c+1);
		printf("%d\n", res);
	}
	return 0;
}