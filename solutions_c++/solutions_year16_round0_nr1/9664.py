#include<iostream> 
using namespace std;

unsigned digit(unsigned n) {
	unsigned N = n;
	unsigned result = 0;
	while (n > 0) {
		unsigned digit = n % 10;
		result |= (1 << digit);
		n /= 10;
	}
	//printf("digit expand of %d = %x\n", N, result);
	return result;
}

void count(unsigned N) {
	if (N == 0) {
		cout << "INSOMNIA" << endl;
		return;
	}

	unsigned uBound = 1;
	while (uBound < N) {
		uBound *= 10;
	}
	uBound = uBound * 10 + 1;

	unsigned result = 0;
	for (unsigned i = 1; i < uBound; i++) {
		//cout << "testing " << i << "*" << N << "=" << i * N << endl;
		result |= digit(i * N);
		if (result == 0x3FF) {
			cout << i * N << endl;
			return;
		}
	}
	cout << "INSOMNIA" << endl;
}

int main() {
	unsigned T, N[256];

	cin >> T;
	for (unsigned t = 0; t < T; t++) {
		cin >> N[t];
	}
	for (unsigned t = 0; t < T; t++) {
		cout << "case #" << t + 1 << ": ";
		count(N[t]);
		//digit(N);
	}
	//system("pause");
	return 0;
}
