#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cstring>
#include <ctime>
#include <cassert>
#include <functional>
#include <numeric>
using namespace std;
typedef long long LL;
#define FOR(k,a,b) for(int k(a); k < (b); ++k)
#define FORD(k,a,b) for(int k(b-1); k >= (a); --k)
#define REP(k,a) for(int k=0; k < (a); ++k)
#define ABS(a) ((a)>0?(a):-(a))

int main( int argc, char* argv[] ) {
#ifdef HOME
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","wb",stdout);
#endif
	int T;
	scanf("%d",&T);
	FOR(tc,1,T+1)
	{
		int N;
		scanf("%d",&N);
		char c[1200];
		scanf("%s",c);
		int res = 0, stup = 0;
		REP(i,N+1)
		{
			int act = c[i]-'0';
			if(stup>=i)
				stup += act;
			else
			{
				res += i- stup;
				stup += i-stup + act;
			}
		}
		printf("Case #%d: %d\n",tc,res);
	}
	return 0;
}
