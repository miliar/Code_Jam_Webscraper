#include <iostream>
#include <vector>
using namespace std;

struct NotSeenDigits {
	bool digits[10];
	int left;	
};

inline bool missing(int num, NotSeenDigits &digits) {
	while(num) {
		if (digits.digits[num % 10]) {
			digits.digits[num % 10] = false;
			--digits.left;
		}
		num /= 10;
	}
	if (digits.left == 0) return false;
	return true;
}


int main() {
	int cases;
	cin >> cases;
	for(int i = 1;i <= cases; ++i) {
		NotSeenDigits digits;
		for(int j = 0; j < 10; j++) {
			digits.digits[j] = true;
		}
		digits.left = 10;
		int start;
		cin >> start;
		if (start == 0) {
			cout << "Case #" << i << ": INSOMNIA" << endl;
			continue;
		}
		int num;
		for(num = start; missing(num, digits); num+=start);
		cout << "Case #" << i << ": " << num << endl;
	}
}