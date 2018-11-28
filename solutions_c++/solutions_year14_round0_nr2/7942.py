#include <cstdio>
#include <cstring>
#include <cmath>

const double eps = 1e-6;
const int MAX_NUMBER = 100007;
double c, f, x;
double cnt_rate;
double rate_time[MAX_NUMBER];

int main() {
	int test_case, case_number;
	scanf("%d", &test_case);
	case_number = 1;
	while (test_case--) {
		scanf("%lf%lf%lf", &c, &f, &x);
		double max_total_time = x / 2.0;
		memset(rate_time, 0, sizeof(rate_time));
		cnt_rate = 2.0;
		for (int i = 1; i <= x; i++) {
			double cnt_time = c / cnt_rate;
			rate_time[i] = cnt_time + rate_time[i - 1];
			cnt_rate += f;
		}
		int k = 1;
		cnt_rate = 2.0;
		while (1) {
			cnt_rate += f;
			double temp_time = rate_time[k] + x * 1.0 / cnt_rate;
			if (temp_time > max_total_time) {
				break;
			}
			else {
				max_total_time = temp_time;
			}
			k++;
		}
		printf("Case #%d: %.6lf\n", case_number, max_total_time);
		case_number++;
	}
	return 0;
}