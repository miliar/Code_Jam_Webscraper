#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <string.h>
#include <string>
#include <math.h>
#include <time.h>
#include <vector>
#include <queue>
#define INF (1<<30)
using namespace std;
int T;
double C,F,X,minn;
inline void solve(){
	scanf("%d",&T);
	for(int ii=1;ii<=T;ii++) {
		scanf("%lf%lf%lf",&C,&F,&X);
		double nowX=0.0,nowF=2.0,total=0.0;
		minn=INF;
		if(C>=X) {
		   printf("Case #%d: %.7lf\n",ii,X/nowF);
		   continue;
		}
		while(total<=minn) { //
			double tmp=X/nowF;
			minn=min(minn,total+tmp);
			total+=C/nowF;
			nowF+=F;
		}
		printf("Case #%d: %.7lf\n",ii,minn);
	}
}
int main(){
	freopen("gcj14B.in","r",stdin);freopen("gcj14B.out","w",stdout);
	solve();
    return 0;
}

