#include <iostream>

using namespace std;

bool is_over(bool *a) {
	for(int i = 0; i < 10; i++) {
		if(!a[i]) {
			return false;
		}
	}
	return true;
}

void mark_digits(int n, bool *a) {
	do {
		int digit = n % 10;
		a[digit] = true;
		n /= 10;
	} while(n > 0);
}

int solve(int n) {
	bool a[10] = { 0 };
	int times = 1;
	while(!is_over(a)) {
		//cout << "marking digits " << n * times << endl;
		mark_digits(n * times, a);
		times++;
	}
	return n * (times - 1);
}

int main() {
	int tc;
	cin >> tc;
	for(int ctc = 1; ctc <= tc; ctc++) {
		int n;
		cin >> n;
		if(n == 0) {
			cout << "Case #" << ctc << ": INSOMNIA" << endl;
			continue;
		}
		cout << "Case #" << ctc << ": " << solve(n) << endl;
	}
	return 0;
}
