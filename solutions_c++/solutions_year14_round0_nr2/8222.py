#include <iostream>
#include <cstdio>

using namespace std;

#define PROBLEM_NAME "B-large"
#define INPUT_FILE_NAME "/home/moustafa/" PROBLEM_NAME ".in"
#define OUTPUT_FILE_NAME "/home/moustafa/" PROBLEM_NAME ".out"


int main() {



	int tc;
	scanf("%d", &tc);
	int it = 0;

	while (++it <= tc) {
		printf("Case #%d: ", it);

		double c,f, x;

		scanf("%lf %lf %lf", &c, &f, &x);
		double cur_val = 0.0f;
		double cur_rate = 2.0;
		double cur_t = 0.0;
		while (cur_val < x) {
			if (cur_val < c) {
				// cannot buy : no need to decide
				double dt =  min(c-cur_val, x-cur_val) / cur_rate;
				cur_val += dt * cur_rate;

				cur_val += min(c-cur_val, x-cur_val) ;
				cur_t  += dt;
			} else {
				// can buy now
				// decide wither or not I should buy
				bool buy = ((x-cur_val+c) / (cur_rate+f)) < ((x-cur_val) / cur_rate);
				if (buy) {
					cur_rate = cur_rate + f;
					double dt = min(c-cur_val+c, x-cur_val+c) / cur_rate;
					cur_val = cur_val - c + dt * cur_rate;
					cur_t += dt;
				} else {
					double dt = (x-cur_val) / cur_rate;
					cur_val = cur_val + dt * cur_rate;
					cur_t += dt;
				}
			}
		}
		printf("%0.7f", cur_t);
		puts("");
	}

	return 0;
}
