#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;
double c, f, x, best;
double check(double cp, double twait){
	while(1){
		double wtime, btime, cerotime;
		wtime=x/cp + twait;
		if (wtime>best) return best;
		best=wtime;
		cerotime=c/cp + twait;
		cp+=f;
		twait=cerotime;
	}
}
int main(){
    //freopen("B-large.in", "r", stdin);
    //freopen("out2", "w", stdout);

	int tc, cs=0;
	cin>>tc;
	while(tc--){
		cin>>c>>f>>x;
		best=50000000000.0f;
		//cout<<check(2.0,  0.0, 0)<<endl;

		printf("Case #%d: %0.7f\n", ++cs, check(2.0,  0.0));
	}
}
