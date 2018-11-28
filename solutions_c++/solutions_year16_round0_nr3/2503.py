#include <iostream>
#include <fstream>
using namespace std;
unsigned long long int ConvertBasen(unsigned long long int Num, int N) {
	unsigned long long int rem;
	unsigned long long int mul = 1;
	unsigned long long int final = 0;
	while (Num > 0) {
		rem = Num % 10;
		final += rem * mul;
		mul *= N;
		Num = Num / 10;
	}
	return final;
}

void ConvertToBinary(unsigned long long int &A1, unsigned long long int N) {
	unsigned long long int rem;
	A1 = 0;
	while (N > 0) {
		rem = N % 2;
		A1 = A1 * 10 + rem;
		N /= 2;
	}
}

bool isPrime(unsigned long long int n) {
	if (n == 2)
		return true;
	if (n == 3)
		return true;
	if (n % 2 == 0)
		return false;
	if (n % 3 == 0)
		return false;

	unsigned long long int i = 5;
	unsigned long long int w = 2;

	while (i * i <= n) {
		if (n % i == 0)
			return false;

		i += w;
		w = 6 - w;
	}
	return true;
}

unsigned long long int Divisor(unsigned long long int N) {
	for (unsigned long long int i = 2; i < N; i++)
		if (N % i == 0)
			return i;
	return 0;
}

int main() {
	ifstream fin("C-small-attempt1.in", ios::in);
	ofstream fout("C-small-attempt1.out", ios::out);
	unsigned long long int A1 = 1, A2 = 10, BEA1, BEA2;
	int N, J;
	int T;
	fin >> T;
	for (int i = 0; i < T; i++) {
		fout << "Case #" << i + 1 << ": \n";
		fin >> N >> J;
		N--;
		for (int j = 0; j < N; j++) {
			A1 *= 10;
			A2 *= 10;
		}
		A1++;
		A2++;
		BEA1 = ConvertBasen(A1, 2);
		BEA2 = ConvertBasen(A2, 2);
		for (unsigned long long int j = BEA1; j < BEA2 - 1; j += 2) {
			int k;
			ConvertToBinary(A1, j);
			for (k = 2; k < 11; k++) {
				if (isPrime(ConvertBasen(A1, k)))
					break;
			}
			if (k == 11) {

				fout << A1;
				for (k = 2; k < 11; k++) {
					fout << " " << Divisor(ConvertBasen(A1, k));
				}
				fout << endl;
				J--;
				if (J <= 0)
					break;
			}
		}
	}
	return 0;
}
