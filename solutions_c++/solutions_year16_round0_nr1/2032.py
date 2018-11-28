#include <bits/stdc++.h>
using namespace std;

bool seen[10];
int remaining;

typedef long long Num;

void reset(void) {
	remaining = 10;
	for (int i = 0; i < 10; i++)
		seen[i] = false;
}

void see(Num num) {
	assert(num >= 0);
	while (num > 0) {
		int rem = num % 10;
		if (!seen[rem]) {
			seen[rem] = true;
			remaining--;
		}

		num /= 10;
	}
}

bool all(void) {
	return remaining == 0;
}

void handle_case(int case_num) {
	Num num;
	scanf(" %lld", &num);

	if (num <= 0) {
		printf("INSOMNIA");
	} else {
		reset();

		Num curr = num;
		for (int i = 0; i < 1000000; i++) { // Should be log_2(num) * 10?
			see(curr);
			if (all()) {
				printf("%lld", curr);
				return;
			}

			if (curr >= LLONG_MAX / 2) {
				break;
			}

			curr += num;
		}

		printf("INSOMNIA");
	}
}

int main(void) {
	int n_cases;
	scanf(" %d", &n_cases);
	for (int case_num = 1; case_num <= n_cases; case_num++) {
		printf("Case #%d: ", case_num);
		handle_case(case_num);
		printf("\n");
	}

	return 0;
}
