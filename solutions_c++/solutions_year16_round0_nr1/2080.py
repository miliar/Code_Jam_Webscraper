#include <iostream>
#include <bitset>

using namespace std;

struct Res {
	int sleep_number;
	int iterations;
	Res(): sleep_number(-1), iterations(-1) {}
	Res(int sleep_number, int iterations): 
		sleep_number(sleep_number), iterations(iterations) {}

};

bitset<10> get_digit_mask(int x) {
	bitset<10> ans;
	if (x == 0) {
		ans[0] = 1;
		return ans;
	}
	while (x != 0) {
		ans[x % 10] = 1;
		x /= 10;
	}
	return ans;
}

Res get_sleep(int x) {
	if (x == 0) {
		return Res(-1, -1);
	}
	Res res(x, 0);
	bitset<10> seen_digits = get_digit_mask(x);
	while(!seen_digits.all()) {
		res.sleep_number += x;
		seen_digits |= get_digit_mask(res.sleep_number);
		++res.iterations;
	}
	return res;
}

int main() {
	int T;
	cin >> T;
	for (int case_n = 1;  case_n <= T; ++case_n) {
		int n;
		cout << "case #" << case_n << ": ";
		cin >> n;
		Res res = get_sleep(n);
		if (res.sleep_number == -1) {
			cout << "INSOMNIA" << endl;
		} else {
			cout << res.sleep_number << endl;
		}
	}
	return 0;
}