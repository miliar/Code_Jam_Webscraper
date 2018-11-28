#include <cstdio>
#include <iostream>

long long n;
bool visit[10];

void solve(void) {
	std::cin >> n;
	if (n == 0) {
		std::cout << "INSOMNIA" << std::endl;
		return;
	}
	long long answer = n, count = 0;
	std::fill(visit, visit + 10, 0);
	for (; count != 10; answer += n) {
		for (long long number = answer; number; number /= 10) {
			int digit = number % 10;
			if (!visit[digit]) {
				visit[digit] = true;
				count++;
			}
		}
	}
	answer -= n;
	std::cout << answer << std::endl;
}

int main(void) {
	int tests;
	std::cin >> tests;
	for (int i = 1; i <= tests; ++i) {
		std::cout << "Case #" << i << ": ";
		solve();
	}
}