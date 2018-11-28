#include <cstdio>

int main(){
	int T;
	double cost, farm, total, curSpeed, curSum;
	double ret;
	scanf("%d", &T);
	for(int i = 1; i <= T; i++){
		ret = 0;
		curSpeed = 2.0;
		curSum = 0.0;
		scanf("%lf %lf %lf", &cost, &farm, &total);
		if(total <=cost){
			ret = total/curSpeed;
		}
		else {
			while((total - cost)/curSpeed > total/(curSpeed+ farm)){
				ret += cost/curSpeed;
				curSpeed += farm;
			}
			ret += total/curSpeed;
		}
		printf("Case #%d: %.7lf\n", i, ret);
	}
	return 0;
}

