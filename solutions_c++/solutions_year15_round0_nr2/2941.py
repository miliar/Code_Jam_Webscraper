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
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","wb",stdout);
#endif
	int T,D,MX;
	scanf("%d",&T);
	
	FOR(tc,1,T+1)
	{
		scanf("%d",&D);
		vector<int> v(D);
		REP(i,D)
			scanf("%d",&v[i]);
		int fres = 10000;
		FOR(i,1,10000)
		{
			int act = i;
			REP(j,D)
			{
				if(v[j]>i)
				{
					act += (v[j]-1)/i;
				}
			}
			fres=min(fres,act);
		}
		
		printf("Case #%d: %d\n",tc,fres);
	}
	return 0;
}
