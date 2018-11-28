#include <iostream>
#include <cstdlib>
#include <string>

void split(const std::string& input, long long& p, long long& q) {
	int i=0;

	while (input[i] != '/') {
		i++;
	}

	p = atoi(input.substr(0, i).c_str());
	q = atoi(input.substr(i+1).c_str());
}

long long gcd(long long a, long long b) {
	if (b == 0) return a;
	return gcd(b, a%b);
}

void solve(long long& p, long long& q) {
	long long g = gcd(p,q);
	p /= g;
	q /= g;

	bool pow_of_two = false;

	for (int i=1; i<=q; i<<=1) {
		if (i==q) {
			pow_of_two = true;
		}
	}

	if (!pow_of_two) {
		std::cout << "impossible\n";
		return;
	}

	while (p > 1) {
		p/=2;
		q/=2;
	}

	int temp = 2;
	for (int i=1; i<q; i++) {
		if (temp == q) {
			std::cout << i << std::endl;
			break;
		}

		temp*=2;
	}
}

int main() {
	std::ios_base::sync_with_stdio(0);

	int z;
	std::cin >> z;

	for (int i=1; i<=z; i++) {
		std::string input;
		std::cin >> input;

		long long p,q;
		split(input, p, q);

		std::cout << "Case #" << i << ": ";
		solve(p, q);
	}
}