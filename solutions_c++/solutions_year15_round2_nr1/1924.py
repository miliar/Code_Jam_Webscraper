#include <cmath>
#include <iostream>
#include <vector>

long long reverse(long long input) {
	long long reverse = 0;
	while (input != 0) {
		reverse *= 10;
		reverse += input % 10;
		input /= 10;
	}
	return reverse;
}

int main()
{
	std::vector<long long> values(1000001);
	for (std::size_t i = 0; i < values.size(); ++i) {
		values[i] = i;
	}
	long long current = 0;
	for (std::size_t i = 1; i < values.size(); ++i) {
		++current;
		current = std::min(current, values[i]);
		long long rev = reverse(i);
		if (values[i] > current) {
			values[i] = current;
		}
		if (values[rev] > current + 1) {
			values[rev] = current + 1;
		}
	}
	int testCases;
	std::cin >> testCases;
	for (int t = 1; t <= testCases; ++t) {
		long long input;
		std::cin >> input;
		std::cout << "Case #" << t << ": " << values[input] << std::endl;
	}
}
