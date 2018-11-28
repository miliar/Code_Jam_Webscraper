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

#define MR 10000010
int t[MR];

int result(LL A, LL B)
{
	int a = sqrt(1.0*A), b = sqrt(1.0*B);
	while(a*a >= A) a--;
	while(b*b <= B) b++; b--;
	return t[b]-t[a];
}

bool check(LL a)
{
	vector < int > v;
	while(a)
	{
		v.PB(a%10);
		a /= 10;
	}
	REP(i,(int)v.size()/2) if(v[i] != v[(int)v.size()-i-1]) return 0;
	return 1;
}

bool go(int a)
{
	return check(a) && check(a*(LL)a);
}

int main()
{
	FOR(i,1,MR) t[i] = t[i-1] + go(i);
	int T;
	scanf("%d", &T);
	REP(c,T)
	{
		LL A, B;
		scanf("%lld%lld", &A, &B);		
		printf("Case #%d: %d\n", c+1, result(A, B));
	}
	return 0;
}