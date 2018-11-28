#include <iostream>
#include <set>
#include <vector>

using ull = unsigned long long;

ull gcd(ull a, ull b) 
{
	while (b != 0) {
		ull c = b;
		b = a % b;
		a = c;
	}
	return a;
}

ull gcm(ull a, ull b)
{
	return (a / gcd(a, b)) * b;
}



int main()
{
	int T;
	std::cin >> T;
	for (int c = 1; c <= T; ++c) {
		ull B, N;
		std::cin >> B >> N;
		std::set<std::pair<ull, ull>> barbers;
		std::vector<ull> times(B + 1);
		for (int i = 1; i <= B; ++i) {
			int tmp;
			std::cin >> tmp;
			barbers.insert(std::make_pair(0, i));
			times[i] = tmp;
		}
		ull gcma = gcm(times[1], times[2]);
		for (int i = 3; i <= B; ++i) {
			gcma = gcm(gcma, times[i]);
		}
		ull howmany = 0;
		for (int i = 1; i <= B; ++i) {
			howmany += gcma / times[i];
		}
		ull n1 = N - 1;
		n1 %= howmany;
		if (n1 != 0) {
			while (n1--) {
				std::pair<ull, ull> beg = *barbers.begin();
				barbers.erase(*barbers.begin());
				beg.first += times[beg.second];
				barbers.insert(beg);
			}
		}
		std::cout << "Case #" << c << ": " << barbers.begin()->second << '\n';
	}

	return 0;
}