
#include <iostream>

using namespace std;

void fill_digit(bool* par, long long number);
bool check_digit(bool* par);

int main() {
	int t = 0;
	int num_initial = 0;
	long long num = 0;

	scanf("%d", &t);

	for(int i = 1; i <= t; i++) {
		scanf("%d", &num_initial);
		num = num_initial;
		if(num == 0) {
			printf("Case #%d: INSOMNIA\n", i);
			continue;
		}
		bool digit[10] = {0};

		while(1) {
			fill_digit(digit, num);
			if(check_digit(digit)) {
				printf("Case #%d: %lld\n", i, num);
				break;
			}
			num += num_initial;
		}
	}

	return 0;
}

void fill_digit(bool* par, long long number) {
	for(;number > 0; number /= 10)
		par[number % 10] = true;
}
bool check_digit(bool* par) {
	for(int i = 0; i < 10; i++)
		if(par[i] == 0) return 0;
	return 1;
}
