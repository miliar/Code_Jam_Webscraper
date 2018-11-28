#include <cstdio>

using namespace std;

double get_elapsed(double rate, double farm_rate, double farm_cost, double target){
	double naive_time = target / rate;
	double farm_time = farm_cost / rate + target / (rate + farm_rate);
	if(naive_time < farm_time){
		return naive_time;
	}else{
		return (farm_cost / rate) + get_elapsed(rate + farm_rate, farm_rate, farm_cost, target);
	}
}

int main(){
	unsigned int T = 0;
	scanf("%u", &T);
	for(unsigned int case_no = 1; case_no <= T; case_no++){
		double C = 0.0;
		double F = 0.0;
		double X = 0.0;
		scanf("%lf", &C);
		scanf("%lf", &F);
		scanf("%lf", &X);
		double target_time = get_elapsed(2.0, F, C, X);
		printf("Case #%u: %.7lf\n", case_no, target_time);
	}
	return 0;
}