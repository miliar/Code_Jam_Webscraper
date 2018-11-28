#include <iostream>
#include <cmath>

using namespace std;

int CACHE[1<<17];
int N, J;

char num[40];


bool isPrime(unsigned long long num) {
	if (num == 1) return true;
	if (num % 2 == 0) return false;
	unsigned long long d = 3;
	while (d*d <= num) {
		if (num%d == 0) return false;

		d+=2;
	}

	return true;
}


void next(char c[]) {
	bool carry = true;
	int n = strlen(c)-2;
	while (carry && n >= 0) {
		if (c[n] == '0') {
			carry = false;
			c[n] = '1';
		}
		else {
			c[n] = '0';
		}
		n--;
	}
}


unsigned long long get_num_base(char n[], int base) {
	int N = strlen(n);

	unsigned long long ans = 0;
	int e = 0;
	for (int i = N-1; i>= 0; i--) {
		ans += (n[i] - '0')*pow(base, e);
		e++;
	}

	return ans;
}


unsigned long long get_divisors(unsigned long long n) {
	for (unsigned long long i = 2; i < n/2; i++) 
		if (n%i == 0)
			return i;

	return 0;
}

void process_ans(int N, int J) {
	int count = 0;

	while (count < J) {
		bool state = true;
		// cout << num << endl;
		for (int b = 2; b <= 10; b++) {
			unsigned long long numero = get_num_base(num, b);
			if (isPrime(numero) || get_divisors(numero) == 0) {
				state = false;
				break;
			}
		}
		if (state) {
			cout << num;
			for (int b = 2; b <= 10; b++)
				cout << " " << get_divisors(get_num_base(num, b));
			cout << endl;
			count++;
		}
		next(num);
	}
}


int main() {
	int T;


	cin >> T;
	cin >> N >> J;

	for (int i = 0; i < 40; i++)
		num[i] = '0';
	num[0] = '1';
	num[N-1] = '1';
	num[N] = '\0';

	cout << "Case #1:" << endl;

	process_ans(N, J);

}

