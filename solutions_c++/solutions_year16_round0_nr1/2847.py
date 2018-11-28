#include <iostream>
#include <cmath>
#include <vector>
#include <iomanip>
using namespace std;

typedef long long ll;

bool allDigits(bool* nums) {
	for (int i = 0; i < 10; i++) {
		if (!nums[i]) {
			return false;
		}
	}
	return true;
}

void confirmDigits(bool* nums, int x) {
	while (x > 0) {
		//cout << x << endl;
		nums[x % 10] = 1;
		x /= 10;
	}
}

int main() {
	ll n, t, term = -1, tempn;
	bool checks[10];
	cin >> t;
	for (int i = 1; i <= t; i++) {
		for (int j = 0; j < 10; j++) checks[j] = 0;
		cin >> n;
		int cnt = 2;
		tempn = n;
		//cout << n << endl;
		while (cnt < 1000 && !allDigits(checks)) {
			confirmDigits(checks, tempn);
			/*cout << tempn << endl;
			for (int j = 0; j < 10; j++) cout << checks[j] << " ";
			cout << endl;*/
			tempn = n * cnt;
			cnt++;
			//cout << n << endl;
		}
		//cout << allDigits(checks) << endl;
		if (allDigits(checks))
			term = tempn/(cnt - 1)*(cnt - 2);
		else
			term = -1;
		cout << "Case #" << i << ": ";
		if (term != -1)
			cout << term << endl;
		else
			cout << "INSOMNIA" << endl;
	}

	return 0;
}