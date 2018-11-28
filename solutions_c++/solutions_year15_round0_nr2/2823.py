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

bool ok(int s, const vector<int>& V)
{
	FORQ(i,1,V.back())
	{
		int ile = i;
		bool res = 1;
		int limit = s-ile;
		
		if(limit <= 0) return 0;

		REP(j,(int)V.size())
		{
			int d = V[j]/limit;
			if(V[j]%limit == 0) d--;
			if(ile < d)
			{
				res = 0;
				break;
			}
			ile -= d;
		}
		if(res) return 1;
	}
	return 0;
}

int go(vector<int>& V)
{
	sort(V.begin(), V.end());
	int p = 1, k = V.back();

	while(p < k)
	{
		int s = (p+k)/2;
		if(ok(s, V)) k = s;
		else p = s+1;
	}
	
	return k;
}

int pom;

int go1(vector < int > V, int add)
{
	sort(V.begin(), V.end());
	pom = min(pom, V.back()+add);
	if(V.back() <= add) return pom;
	pom = min(pom, V.back() + add);
	REP(i,(int)V.size())
	{
		FOR(j,1,V[i]/2+1)
		{
			V[i] -= j;
			V.PB(j);
			pom = min(pom, go1(V,add+1));
			V[i] += j;
			V.pop_back();
		}
	}
	return pom;
}

int main()
{
	int T;
	scanf("%d", &T);
	REP(c,T)
	{
		vector<int> V;
		int D;
		scanf("%d", &D);
		REP(i,D)
		{
			int a;
			scanf("%d", &a);
			V.PB(a);
		}
		int res = go(V);
		/*pom = 1e9;
		int res1 = go1(V, 0);
		if(res != res1)
		{
			printf("Error %d %d\n", res, res1);
		}*/
		printf("Case #%d: ", c+1);
		printf("%d\n", res);
	}
	return 0;
}