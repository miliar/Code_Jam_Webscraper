#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

long long int number(vector<bool>& digits, int base) {
	long long int num = 0;
	for (int i = digits.size() - 1; i >= 0; i--) {
		num += (digits[i] == 1)? pow(base,(digits.size() - 1) - i) : 0;
	}
	
	return num;
}

void print(vector<bool>& digits, vector<long long int>& divs) {
	cout << endl;
	for (int i = 0; i < digits.size(); i++) {
		cout << digits[i];
	}
	for (int i = 0; i < divs.size(); i++) {
		cout << " " << divs[i];
	}
}

bool isPrime(long long int num, vector<long long int>& divs) {
	for (int d = 2; d <= sqrt(num); d++) {
		if (num % d == 0) {
			divs.push_back(d);
			return false;
		}
	}
	return true;
}

int main() {
	int T;
	cin >> T;
	
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ":";
		int N, J;
		cin >> N;
		cin >> J;
		vector<bool> digits(N,false);
		digits[0] = true;
		
		int counter = 1;
		int count = 0;
		while(N >= counter && count < J) {
			digits[N-counter] = true;
			do {
				vector<long long int> divisors;
				for (int i = 2; i <= 10; i++) {
					long long int num = number(digits,i);
					if(isPrime(num, divisors)) {
						break;
					} 
				}
				if (divisors.size() == 9) {
					print(digits, divisors);
					count++;
				} 
			} while (count < J && next_permutation(digits.begin()+1, digits.end()-1));
			sort(digits.begin()+1, digits.end()-1);
			counter++;
		}

	}
	
	return 0;
}
