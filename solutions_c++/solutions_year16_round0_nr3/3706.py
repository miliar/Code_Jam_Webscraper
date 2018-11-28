#include <iostream>
#include <math.h>
using namespace std;

long long createNumber(int* arr, int base, int n) {
	long long number = 0;
	long long base_power = 1;
	for(int i = 0; i < n; i++) {
		number += (base_power * arr[i]);
		base_power *= base;
	}
	return number;
}

long long isPrime(long long n) {
	if(n % 2 == 0) {
		return 2;
	}
	for(int i = 3; i <= sqrt(n); i+=2) {
		if(n % i == 0) {
			return i;
		}
	}
	return -1;
}

int main() {
	int t,n,j;
	cin >> t >> n >> j;
	int* arr = new int[n];
	int* divisors = new int[11];

	arr[0] = 1;
	arr[n-1] = 1;
	for(int i = 1; i < n-1; i++) {
		arr[i] = 0;
	}

	int count = 0;
	long long currNumber = createNumber(arr, 2, n);
	cout << "Case #1:" << endl;
	while(count < j) {
		bool found = true;
		long long number;
		for(int i = 0; i < 11; i++) {
			divisors[i] = 0;
		}
		for(int i = 2; i < 11; i++) {
			number = createNumber(arr, i, n);
			long long divisor = isPrime(number);
			if(divisor == -1) {
				found = false;
				break;
			}
			divisors[i] = divisor;
		}
		if(found) {
			count++;
			for(int i = n-1; i >= 0; i--) {
				cout << arr[i];
			}
			cout << " ";
			for(int i = 2; i < 11; i++) {
				cout << divisors[i] << " ";
			}
			cout << endl;
		}
		currNumber += 2;
		long long temp = currNumber;
		for(int i = 0; i < n; i++) {
			arr[i] = temp % 2;
			temp = temp >> 1;
		}
	}
}