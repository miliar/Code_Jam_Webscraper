#include <assert.h>
#include <ctype.h>
#include <float.h>
#include <math.h>
#include <stdio.h>
#include <string>
#include <stdlib.h>
#include <time.h>
#include <algorithm>
#include <numeric>
#include <functional>
#include <utility>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <memory.h>

using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,k,n) for (int i=(k); i<=(int)(n); ++i)
#define OPENFILE
#define FILENAME "A-small-attempt0"
#define PI 3.14159265359

typedef long long ll;

int main() {
#ifdef OPENFILE
		char INPUTF[30]=FILENAME;
		char INPUTF2[30]=FILENAME;
		freopen(strcat(INPUTF,".in"),"r",stdin);//redirects standard input
		freopen(strcat(INPUTF2,".out"),"w",stdout);//redirects standard output
#endif
	int T;
	cin>>T;
	REP(tt,T){
		ll r,t;
		cin>>r>>t;
		ll n=(1-r+t)/4+1;
		if(n>1e9)n=min(1000000000LL,1000000000000000000L/r);
		while(t<2*n*r+(2*n-1)*n)n--;
		printf("Case #%d: %lld\n",tt+1,n);
		//fprintf (stderr, "Case #%d: %f\n",t+1,res);

	}

}
