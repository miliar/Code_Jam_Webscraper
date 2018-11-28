#include <cstdlib>
#include <cstdio>
using namespace std;

int main(){
	int cases;
	scanf("%d", &cases);
	for(int z=1; z<=cases; z++){
		double C, F, X;
		scanf("%lf %lf %lf", &C, &F, &X);
		
		double curtime = 0;
		double prodrate = 2;
		double best = X/2;
		while(true){
			curtime += C/prodrate;
			prodrate += F;
			double temp = curtime + X/prodrate;
			if(temp < best){
				best = temp;
			}else{
				break;
			}
		}
		printf("Case #%d: %.7f\n", z, best);
	}

	return 0;
}