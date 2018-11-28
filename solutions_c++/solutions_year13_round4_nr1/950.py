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
#define MOD 1000002013

int N, M;

struct
{
	int o, e, p;
}t[MR];

int cost(int A, int B)
{
	return ((2*N-B+A+1)*(LL)(B-A)/2)%MOD;
}

int result()
{
	int m = M;
	int sum = 0;	//ile powinni zaplacic
	REP(i,m) sum = (sum + cost(t[i].o, t[i].e)*(LL)t[i].p) % MOD;
	int res = 0;	//ile zaplaca oszukujac
	map < int, int > M;	//kartki z poczatkowymi stacjami
	vector < pair < pair < int, bool >, int > > V;	//(nr stacji, wychodza - 1, wchodza - 0), ile
	REP(i,m)
	{
		V.PB(MP(MP(t[i].o,0),t[i].p));
		V.PB(MP(MP(t[i].e,1),t[i].p));
	}
	sort(V.begin(), V.end());
	REP(i,2*m)
	{
		if(!V[i].ST.ND) M[V[i].ST.ST] += V[i].ND;
		else
		{
			map < int, int > :: iterator it = M.end();it--;			
			while(V[i].ND)
			{
				if(V[i].ND > it->ND)
				{
					res = (res + cost(it->ST,V[i].ST.ST)*(LL)it->ND) % MOD;
					V[i].ND -= it->ND;
					it->ND = 0;
					it--;
				}
				else
				{
					res = (res + cost(it->ST,V[i].ST.ST)*(LL)V[i].ND) % MOD;					
					it->ND -= V[i].ND;
					V[i].ND = 0;
				}
			}
			it = M.begin();
			while(it != M.end())
			{
				map < int, int > :: iterator it1 = it;
				it++;
				if(!it1->ND) M.erase(it1);
			}
		}
	}
	return (sum + MOD - res) % MOD;
}

int main()
{
	int T;
	scanf("%d", &T);
	REP(c,T)
	{		
		scanf("%d%d", &N, &M);
		REP(i,M) scanf("%d%d%d", &t[i].o, &t[i].e, &t[i].p);
		printf("Case #%d: %d\n", c+1, result());
	}
	return 0;
}