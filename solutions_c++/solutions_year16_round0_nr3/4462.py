#include <bits/stdc++.h>
using namespace std;

long long get_base_value(string str, int base) {
	long long ret = 0;
	for (int i = 0; i < str.size(); ++i) {
		int digit = str[i] - '0';
		if (digit) {
			ret += digit * pow(base, 15 - i);
		}
	}
	return ret;
}

long long get_factor(long long num) {
	if (num % 2 == 0) {
		return 2;
	}
	for (long long i = 3; i * i <= num; i += 2) {
		if (num % i == 0) {
			return i;
		}
	}
	return -1;
}

int main()
{
	string jamcoin = "1000000000000001";
	int count = 0;
    cout << "Case #1:\n";
	for (long long i = 0; i < 99999999 && count < 50; ++i) {
		string next_str = bitset< 14 >(i).to_string();
		jamcoin.replace(1, 14, next_str);

		vector<long long> vi{};
		bool status = true;
		for (int j = 2; j <= 10; ++j) {
			long long value = get_base_value(jamcoin, j);
			long long factor = get_factor(value);
			if (factor != -1) {
				vi.push_back(factor);
			}
			else {
				status = false;
				break;
			}
		}

		if (status) {
			++count;
			cout << jamcoin << ' ';
			for (auto item : vi) {
				cout << item << ' ';
			}
			cout << '\n';
		}
	}
}