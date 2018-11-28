#include <iostream>
#include <string>
#include <cstdlib>
#include <fstream>
#include <string>
#include <sstream>
#include <math.h>
using namespace std;

bool is_prime(long long n) {
	if ((n % 2 == 0) || (n % 3 == 0)) {
		return false;
	}
	for (int i = 3; i * i <= n / 2; i += 2) {
		if ((n % i == 0) || (n % (i + 2) == 0)) {
			return false;
		}
	}
	return true;
}

void add_binary(string& jamcoin) {
	for (int i = jamcoin.length() - 2; i >= 1; i--) {
		if (jamcoin[i] == '0') {
			jamcoin[i] = '1';
			jamcoin[i-1] = '1';
			break;
		} else {
			jamcoin[i] = '0';
		}
	}
}

long long convert_base(string jamcoin, int base) {
	long long sum = 0;
	int index = 0;
	for (int i = jamcoin.length() - 1; i >= 0; i--) {
		if (jamcoin[i] == '1') {
			sum += pow(base, index);
		}
		index++;
	}
	return sum;
}

bool isjamcoin(string jamcoin) {
	int base = 2;
	for (; base <= 10; base++) {
		long long jam = convert_base(jamcoin, base);
		if (is_prime(jam)) {
			return false;
		}
	}
	return true;
}

int main() {
	std::ifstream fin("C-small-attempt2.in");
	std::ofstream fout("C-small.out");

	int T, N, J;
	string add;
	fin >> T;
	cout << T << endl;
	string jamcoin;
	for (int t = 1; t <= T; t++) {
		fout << "Case #" << t << ":\n";
		fin >> N >> J;
		for (int i = 0; i < N; i++)
			jamcoin.append("0");
		jamcoin[0] = '1';
		jamcoin[N - 1] = '1';
		cout << jamcoin << endl;
		while (!isjamcoin(jamcoin)) {
			add_binary(jamcoin);
		}
		cout << "DONE\n";
		int j = 0;
		int nums[9];
		for (; j < J;) {
			cout << "J: " << j << endl;
			int base = 2;
			for (; base <= 10;) {
				long long jam = convert_base(jamcoin, base);
				for (long long i = 2; i <= jam; i++) {
					if (jam % i == 0) {
						nums[base - 2] = i;
						base++;
						break;
					}
				}
			}
			fout << jamcoin << " ";
			for (int i = 0; i < 9; i++)
				fout << nums[i] << " ";
			fout << endl;
			j++;
			add_binary(jamcoin);
			cout << jamcoin << endl;
			while (1) {
				if (isjamcoin(jamcoin))
					break;
				add_binary(jamcoin);
			}
		}
	}
	//exit(0);

	return 0;
}

