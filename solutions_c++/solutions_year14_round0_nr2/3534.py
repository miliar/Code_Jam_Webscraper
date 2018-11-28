#include <cstdio>
#include <cstdlib>

const double MAX_TIME = 100000.0/2 + 100;

int main() {
	int T;
	scanf("%d", &T);
	for (int cs=1; cs<=T; cs++){
		double C;
		double F;
		double goal;
		scanf("%lf%lf%lf", &C, &F, &goal);
		double min_win_time = MAX_TIME;
		double current_time = 0.0;
		double product_rate = 2.0;
		double next_buy_time = 0.0;
		do {
			double not_buy_win = current_time + goal/product_rate;
			if (not_buy_win < min_win_time) {
				min_win_time = not_buy_win;
			}
			// make money and buy
			current_time += C/product_rate;
			product_rate += F;
			//printf("nbw = %lf, crt_time = %lf pr = %lf\n", 
			//	not_buy_win, current_time, product_rate);
		} while (current_time <= min_win_time);
		printf("Case #%d: %.7lf\n", cs, min_win_time);
	}
	return 0;
}