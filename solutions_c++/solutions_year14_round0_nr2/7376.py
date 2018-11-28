#include<cstdio>
#include<cmath>
#include<algorithm>
using namespace std;


int main(){
	int Z;
	scanf("%d", &Z);
	for(int z = 1; z <= Z; ++z){
		double prod = 2.0, C, X, F;
		double time = 0.0, tmp, res;
		scanf("%lf %lf %lf", &C, &F, &X);
		res = X/2.0;
		for(int i = 1; ; ++i){
			tmp = C/prod;
			prod += F;
			time = time + tmp;
			tmp = time + X/prod;
			if(tmp > res)break;
			res = tmp;
		}
		printf("Case #%d: %lf\n", z, res);
	}
	return 0;
}
