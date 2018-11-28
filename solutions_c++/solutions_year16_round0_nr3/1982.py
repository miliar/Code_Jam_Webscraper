#include <fstream>
#include <iostream>
#include <cstring>
#include <bitset>
#include <cmath>

int T, curr;
int N, J;
int* basediv;

long long int change(long long int n, int base) {
	long long int r = 0;
	for (int k = 0; k < N; k++) {
		if(n == (n | 1 << k)) r += pow(base, k);
	}
	return r;
}

bool check(long long int num) {
	for (int base = 2; base <= 10; base++) {
		long long int kk = change(num, base);
		if (kk % basediv[base] != 0) return true;
	}
	return false;
}

int main() {
	std::ifstream fin("C-large.in");
	std::ofstream fout("coin-big-output.out");

	if(!fin.is_open() || !fout.is_open()) return 1;
	fin >> T;
//	scanf("%d", &T);
	fin >> N >> J;
//	scanf("%d%d", &N, &J);

	fout << "Case #1:\n";
//	printf("Case #1:\n");

	int num = (N % 4 == 0) ? 4 : (N % 3 == 0) ? 3 : 2;
	int divnum = 1;
	for (int i = 1; i < num; i++) divnum |= (1 << i);

	basediv = new int[11];
	for (int i = 2; i <= 10; i++) {
		basediv[i] = 1;
		for (int k = 1; k < num; k++) basediv[i] += pow(i, k);
	}

	long long int rightret = 1, leftret = (1 << (N / 2 - 1));
	while (rightret % divnum != 0) rightret += 2;

	while (check(leftret)) {
		leftret++;
	}
	int firstright = rightret;

	while(J > 0) {
		if (rightret > (1 << (N / 2))) { 
			rightret = firstright; 
			leftret += divnum * 2;
			while (check(leftret)) leftret += divnum * 2;
		}

		if (rightret % divnum == 0) {

			bool notans = false;
			for (int base = 2; base <= 10; base++) {
				long long int kk = change(rightret, base);
				if (kk % basediv[base] != 0) { notans = true; break; }
			}
			if (notans) { rightret += divnum * 2; continue; }

			for (int i = N/2 - 1; i >= 0; i--)
				if (leftret == (leftret | (1 << i))) fout << '1';
				else fout << '0';
			for (int i = N/2 - 1; i >= 0; i--)
				if (rightret == (rightret | (1 << i))) fout << '1';
				else fout << '0';

			for (int base = 2; base <= 10; base++) {
				fout << " " << basediv[base];
			}
			J--;
			fout << '\n';
			rightret += divnum*2;
		}
	}
}