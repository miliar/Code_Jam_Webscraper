#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector <int> getDigits(int n) {
	vector<int> digits;
	while(n) {
		digits.push_back(n % 10);
		n = n / 10;
	}
	//reverse(digits.begin(), digits.end());
	return digits;
}

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		int n;
		cin >> n;
		vector<int> original;
		original = getDigits(n);
		vector<bool> seen(10,false);
		vector<int> digits;
		int count = 1;
		int counter = 0;
		bool nonew = false;
		
		while(counter < 10) {
			int carry = 0;
			digits.clear();
			for (int j = 0; j < original.size(); j++) {
				int c = (original[j] * count + carry)/10;
				digits.push_back((original[j] * count + carry) % 10);
				carry = c;
			}
			if (carry != 0) {
				digits.push_back(carry);
			}
			
			/*
			for (int j = digits.size() - 1; j >= 0; j--) {
				cout << " " << digits[j];
			}
			cout << endl;*/
			if (n == 0) {
				nonew = true;
			}
			for (int j = 0; j < digits.size(); j++) {
				if (!seen[digits[j]]) {
					seen[digits[j]] = true;
					counter++;
					//nonew = false;
				}
			}
			if (nonew) {
				break;
			}
			count++;
		}
		
		if (nonew) {
			cout << "Case #" << i << ": INSOMNIA\n";
			continue;
		}
		int number = 0;
		for (int j = digits.size() - 1; j >= 0; j--) {
			//cout << " " << digits[j];
			number = number*10 + digits[j];
		}
		cout  << "Case #" << i << ": " << number << endl;
	}
	return 0;
}