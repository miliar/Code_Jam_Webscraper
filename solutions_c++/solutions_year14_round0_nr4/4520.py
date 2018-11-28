#include <sstream>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <numeric>
#include <algorithm>

#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <limits.h>

using namespace std;

typedef long long ll;

#define mem(a,b) memset(a,b, sizeof a)
#define SZ(x)	(int)x.size()
#define FOREACH(it,x) for(__typeof((x).begin()) it=(x.begin());it!=(x.end());++it)
#define ERR 1e-6
#define PI (2.0*acos(0))
#define ALL(x) x.begin(),x.end()
#define pb push_back
#define rep(i,n,m) for(int i = (int)n,_m=(int)m;i<_m;++i)
#define bj(stat,b) (stat & (1<<b))
#define bc(stat,b) (stat & (~(1<<b)))
#define vi vector<int> 
#define vs vector<string>

template <class T> T Abs(T x) {return x<0?-x:x;}

int
main()
{
	int T;
	int N;
	scanf("%d\n",&T);
	for(int t=1;t<=T;t++) {
		scanf("%d",&N);
		double tmp;
		vector<double> naomi;
		vector<double> ken;
		rep(i,0,N) {
			scanf("%lf", &tmp);
			naomi.pb(tmp);
		}
		rep(i,0,N) {
			scanf("%lf", &tmp);
			ken.pb(tmp);
		}
		sort(ALL(naomi));
		sort(ALL(ken));

		//vector<double> d_naomi(ALL(naomi));
		//set<double> d_ken(ALL(ken));

		int WarKnum = 0;
		int WarNnum;
		// calculate war
		int ni = 0;
		int ki = 0;
		for(;ni<N;) {
			while(ki<N && ken[ki]<naomi[ni]) ki++;
			if(ki<N) {
				WarKnum++;
				ni++;
				ki++;
			}
			else break;
		}
		WarNnum = N-WarKnum;

		//calculate d war
		ni = 0;
		int kmaxi=N-1;
		int kmini=0;
		int dWarNnum = 0;
		for(;ni<N;ni++) {
			if(ken[kmini]<naomi[ni]) {
				dWarNnum++;
				kmini++;
			}
			else {
				kmaxi--;
			}
		}
		printf("Case #%d: %d %d\n", t, dWarNnum, WarNnum);
	}
}
