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

int t1[4][4], t2[4][4];

string result(int r1, int r2)
{	
	set < int > S;
	REP(i,4) S.insert(t1[r1][i]);
	int ile = 0, res;
	REP(i,4)
		if(S.find(t2[r2][i]) != S.end())
		{
			ile++;
			res = t2[r2][i];
		}
	if(!ile) return "Volunteer cheated!";
	if(ile == 1)
	{
		string s = "";
		while(res)
		{
			s += (char)(res%10+'0');
			res /= 10;
		}
		reverse(s.begin(), s.end());
		return s;
	}
	return "Bad magician!";
}

int main()
{
	int T;
	scanf("%d", &T);
	REP(c,T)
	{
		int r1;
		scanf("%d", &r1);
		REP(i,4)REP(j,4) scanf("%d", &t1[i][j]);
		int r2;
		scanf("%d", &r2);
		REP(i,4)REP(j,4) scanf("%d", &t2[i][j]);
		printf("Case #%d: %s\n", c+1, result(r1-1, r2-1).c_str());
	}
	return 0;
}