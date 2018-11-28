#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <fstream>
#include <ctime>

using namespace std;


ifstream infile;
ofstream outfile;

int T;
int N, J;
int cnt;

int num[17];

long long used_ans[51];

bool not_prime[110000000];

vector<long long> prime;

void reset() {
	return;
}

void rndm() {
	int iter;

	iter = rand() % 14 + 2;
	num[iter] = 1 - num[iter];

	iter = rand() % 14 + 2;
	num[iter] = 1 - num[iter];
}

bool judge() {
	int ans[11];
	for (int base = 2; base <= 10; ++base) {
		long long Num = 0;
		for (int i = 1; i <= N; ++i)
			Num = Num * base + num[i];

		if (base == 10) {
			for (int i = 1; i <= cnt; ++i)
				if (used_ans[i] == Num)
					return false;
		}

		for (int i = 0; i < prime.size() && prime[i] < Num; ++i) {
			if (Num % prime[i] == 0) {
				ans[base] = prime[i];

				if (base == 10)
					used_ans[cnt + 1] = Num;
				//				cout << Num << " " << prime[i] << endl;

				break;
			}
		}
		if (Num % ans[base] != 0)
			return false;
	}

	for (int i = 1; i <= N; ++i)
		outfile << num[i];

	for (int base = 2; base <= 10; ++base)
		outfile << " " << ans[base];

	outfile << endl;


	cout << cnt + 1 << endl;
	return true;
}

int main() {
	infile.open("input.txt");
	outfile.open("output.txt");

	srand(time(NULL));

	not_prime[1] = true;
	for (int i = 2; i * i < 110000000; ++i) {
		if (!not_prime[i]) {
			int tmp = i * 2;
			while (tmp < 110000000) {
				not_prime[tmp] = true;
				tmp += i;
			}
		}
	}

	for (int i = 2; i < 110000000; ++i) {
		if (!not_prime[i])
			prime.push_back(i);
	}

	for (int i = 1; i <= 16; ++i)
		num[i] = 1;

	infile >> T;

	for (int p = 1; p <= T; ++p) {
		//		reset();

		outfile << "Case #" << p << ":" << endl;

		infile >> N >> J;

		while (cnt < J) {
			rndm();
			cnt += (judge()) ? 1 : 0;
		}
	}

	infile.close();
	outfile.close();
	return 0;
}