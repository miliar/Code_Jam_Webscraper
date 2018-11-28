#include <cstdio>
#include <cstdlib>
#include <string>
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

string to_bin(long long x) {
	
	string s;

	while (x > 0) {
		
		if (x % 2 == 0) {

			s += '0';

			x /= 2;

		}

		else {

			s += '1';

			x = (x - 1) / 2;

		}

	}

	return s;

}

string generate_s(long x, int reset=0) {

	static long long d;
	
	long long m = 1<< (x-2);
	
	string s;

	if (reset) {
		
		d = 1;

		return "";

	}

	if (d < m) {
		
		s = to_bin(d);

		++d;

	}

	else return "LOL";

	for (long i = s.size(); i < (x-2); ++i) s += '0';

	s += '1';

	s = string(s.rbegin(), s.rend());

	s += '1';

	return s;

}

long long is_prime(long long x) {
	
	for (long long i = 2; i < sqrt(x); ++i) {

		if (x % i == 0) return i;
	
	}

	return 0;
}

vector<long long> coin_jam(string s, long x) {

	long long n[9], d;

	vector<long long> divs;

	if (s == "LOL") {

		for (int i = 0; i < 13; ++i) divs.push_back(1);

		return divs;

	}

	for (long i = 0; i < 9; ++i) n[i] = 0;

	for (long i = 0; i < 9; ++i) {

		for (long j = 0; j < x; ++j) {

			n[i] += (s[j] - 48) * pow(i + 2, x - 1 - j);

		}
		
		d = is_prime(n[i]);

		if (d == 0) {

			divs.clear();

			return divs;

		}

		divs.push_back(d);

	}
	
	return divs;

}

int main() {
	
	long n, x, y;
	
	string s;

	vector<long long> divs;

	scanf("%ld", &n);

	for (long z = 0; z < n; ++z) {
	
		scanf("%ld %ld", &x, &y);

		printf("Case #%ld:\n", z+1);
		
		generate_s(x, 1);

		for (long i = 0; i < y; ++i) {
			
			while (divs.size() == 0) {

				s = generate_s(x);
		
				divs = coin_jam(s, x);
			
			}

			if (divs.size() > 10) break;

			printf("%s", s.c_str());

			for (long j = 0; j < 9; ++j) printf(" %lld", divs[j]);			
			
			printf("\n");

			divs.clear();

		}

	}

	return 0;

}
