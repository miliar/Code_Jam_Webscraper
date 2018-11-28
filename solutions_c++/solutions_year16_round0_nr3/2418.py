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

#define N 16
#define J 50

LL convert(int mask, int base)
{
	LL v = 0, pom = 1;
	REP(i, N)
	{
		if (mask&(1 << i)) v += pom;
		pom *= base;
	}

	return v;
}

int check(LL v)
{
	for (int i = 2; i*(LL)i <= v; i++)
		if (v % i == 0) return i;
	return -1;
}

vector<int> go(int &mask)
{
	vector < int > res;
	while (true)
	{
		int nmask = mask << 1;
		nmask++;
		nmask |= (1 << (N-1));
		bool ok = 1;
		FOR(i, 2, 11)
		{
			LL v = convert(nmask, i);
			int d = check(v);
			if (d == -1)
			{
				ok = 0;
				break;
			}
			res.push_back(d);
		}
		if (ok)
		{
			res.push_back(nmask);
			return res;
		}
		mask++;
		res.clear();
	}
}

int main()
{
	int T;
	scanf("%d", &T);
	REP(c, T)
	{
		printf("Case #1:\n");
		int mask = 0;
		REP(i, J)
		{
			auto res = go(mask);
			FORD(j, N, 0) if (res.back()&(1 << j)) printf("1"); else printf("0"); printf(" ");
			REP(j, 9) printf("%d ", res[j]); printf("\n");
			mask++;
		}
	}
	return 0;
}