#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <sstream>
#include <cmath>

using namespace std;

//const long long VALUE_MAX = 9999999999999;

long long first_divisor(long long n) {
	for (int i = 2; i <= ((long long)(sqrt(n))+1); i++) {
		if (n % i == 0) {
			return i;
		}
	}
	return -1;
}

long long value_in_base(const string& s, int base) {
	long long res = 0;
	long long power = 1;

	for (int i = s.size()-1; i >= 0; i--) {
		res += ((long long)(s[i]-'0'))*power;
		power *= base;
	}

	return res;
}

int main() {
	int n_tests;

	cin >> n_tests;
	cin.ignore();

	for (int test = 0; test < n_tests; test++) {
		// input
		int j;
		int n;
		vector<pair<string,vector<long long>>> result;
		string tmp;
		cin >> n >> j;
		cin.ignore();

		for (int i = 0; i < n; i++) {
			tmp += ((i == 0 || i == n-1) ? ('1') : ('0'));
		}

		while (result.size() < j) {
			//cout << tmp << endl;
			//cout << result.size() << endl;
			vector<long long> divisors;

			for (int base = 2; base <= 10; base++) {
				long long value = value_in_base(tmp, base);
				//if (value < VALUE_MAX) {
					long long divisor = first_divisor(value);
					if (divisor != -1) {
						divisors.push_back(divisor);
					}
				//}
			}

			if (divisors.size() >= 9) {
				result.push_back(make_pair(tmp, divisors));
			}

			for (int i = tmp.size() - 2; i > 0; i--) {
				
				if (tmp[i] == '0') {
					tmp[i] = '1';
					break;
				}
				if (tmp[i] == '1') {
					tmp[i] = '0';
				}
			}

		}




		cout << "Case #" << test+1 << ": " << endl; 

		// output
		for (int i = 0; i < result.size(); i++) {
			auto a = result[i];

			cout << a.first;

			for (int k = 0; k < a.second.size(); k++) {
				cout << " " << a.second[k];
			}

			cout << endl;
		}

	}

	return 0;
}