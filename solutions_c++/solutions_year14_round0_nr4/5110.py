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

#define MR 20
double t[2][MR];
bool done[MR];

pair < int, int > go2(int N, bool sel)
{
	sort(t[sel], t[sel]+N);
	int m1 = -1, m2 = -1;
	do
	{
		memset(done, 0, sizeof(done));
		sort(t[!sel], t[!sel]+N);
		int r = 0;
		REP(i,N)
		{
			bool found = 0;
			REP(j,N)
				if(t[sel][i] < t[!sel][j] && !done[j])
				{
					found = 1;
					done[j] = 1;
					break;
				}	
			if(!found) REP(j,N) if(!done[j]) { done[j] = 1; break; }
			r += found;
		}
		m1 = max(m1, N-r);
		m2 = max(m2, r);
	}while(next_permutation(t[sel], t[sel]+N));
	return MP(m1, m2);
}

pair < int, int > go1(int N, bool sel)
{
	sort(t[sel], t[sel]+N);
	int m1 = -1, m2 = -1;
	do
	{
		memset(done, 0, sizeof(done));
		sort(t[!sel], t[!sel]+N);
		int r = 0;
		REP(i,N)
		{
			bool found = 0;
			REP(j,N)
				if(!done[j] && t[sel][i] > t[!sel][j])
				{
					found = 1;
					done[j] = 1;
					break;
				}
			if(!found)
			{
				FORD(j,N,0)
					if(!done[j])
					{
						done[j] = 1;
						break;
					}
			}
			r += found;
		}
		m1 = max(m1, r);
		m2 = max(m2, N-r);
	}while(next_permutation(t[sel], t[sel]+N));
	return MP(m1, m2);
}


int main()
{
	int T;
	scanf("%d", &T);
	REP(c,T)
	{
		int N;
		scanf("%d", &N);
		REP(i,N) scanf("%lf", &t[0][i]);
		REP(i,N) scanf("%lf", &t[1][i]);
		printf("Case #%d: ", c+1);
		int r2 = go2(N,0).ST;
		int r1 = go1(N,0).ST;
		printf("%d %d\n", r1, r2);
	}
	return 0;
}