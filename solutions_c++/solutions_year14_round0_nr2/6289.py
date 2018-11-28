#include <cstdio>
#include <algorithm>
using namespace std;

int main(){
	int T;
	scanf("%d",&T);
	for(int m = 1; m <= T; ++m){
		double c,f,x;
		double step = 2.0;
		double tm = 0.0;
		double ctotal = 0.0;
		scanf("%lf%lf%lf",&c,&f,&x);
		if ( c < x ){
			tm = x / 2.0;
			while ( (ctotal + c*1.0/step + x*1.0/(step + f)) < tm){
				ctotal += c*1.0/step;
				tm = ctotal + x*1.0/(step + f);
				step += f;
			}
		}
		else{
			tm = x / 2.0;
		}
		printf("Case #%d: %.7lf\n", m, tm);
	}
}