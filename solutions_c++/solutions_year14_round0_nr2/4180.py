#include <cstdio>
#include <cfloat>
#include <iostream>
using namespace std;
#define E .000001

int TC;
double C, F, X, best, need;


double dfs( double time, int f, double cur ){

	//cout << time << " - " << cur << " - " << f << endl;

	if( cur+E >= X ){
		best = min(best,time);
		return 0;
	}

	//save until end
	need = ( X - cur );
	dfs( time + need/( 2 + f*F ), f, cur + need );

	//save until next fact
	need = ( C - cur );
	if( time + need/( 2 + f*F ) - E < best ) dfs( time + need/( 2 + f*F ), f+1, cur + need - C );

	return 0;

}


int main(){
	scanf("%d",&TC);
	for(int tc=1; tc<=TC; ++tc){

		scanf("%lf %lf %lf",&C,&F,&X);

		best = 100000;
		dfs(0,0,0);
		printf("Case #%d: %.7lf\n", tc, best );

	}
	return 0;
}
