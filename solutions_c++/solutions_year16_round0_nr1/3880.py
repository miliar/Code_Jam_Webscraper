#include<iostream>
#include<climits>
#include<vector>
#include<algorithm>

void solve(int c) {
	long long n;
	std::cin >> n;

	if (n == 0) {
		std::cout << "Case #" << c << ": INSOMNIA" << std::endl;
		return;
	}

	std::vector<int> v(10);
	{
		int t = n;
		while (t != 0) {
			v[t % 10]++;
			t /= 10;
		}
	}


	for (int i = 2; i < LLONG_MAX / n; i++) {
		long long t = n * i;
		while (t != 0) {
			v[t % 10]++;
			t /= 10;
		}
		if (std::find(v.begin(), v.end(), 0) == v.end()) {
			std::cout << "Case #" << c << ": " << n * i << std::endl;
			return;
		}
	}
}

int main() {
	int t;

	std::cin >> t;

	for (int i = 0; i < t; i++) {
		solve(i + 1);
	}
}