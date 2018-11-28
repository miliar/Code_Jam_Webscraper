#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

long long divisor(long long x) {
	if (x == 2) return 0;
	else if (x % 2 == 0) return 2;
	else if (x == 1) return 1;
	for (long long i = 3; i * i <= x; i += 2) {
		if (x % i == 0) return i;
	}
	return 0;
}

string to2(long long x) {
	string ret = "";
	while (x) {
		ret = char('0' + (x % 2)) + ret;
		x /= 2;
	}
	return ret;
}

long long to10(string x, long long base) {
	long long ret = 0;
	long long temp = 1;
	for (int i = x.size() - 1; i >= 0; i--) {
		if (x[i] == '1') ret += temp;
		temp *= base;
	}
	return ret;
}

int main(void) {
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int test_case;
	fin >> test_case;
	for (int test_idx = 1; test_idx <= test_case; test_idx++) {
		long long n, j;
		// cin >> n >> j;
		fin >> n >> j;

		cout << "Case #" << test_idx << ":" << endl;
		fout << "Case #" << test_idx << ":" << endl;
		int cnt = 0;
		for (long long bin = ((long long)1 << (n - 1)) + 1; bin <= ((long long)1 << n) - 1; bin += 2) {
			bool flag = true;
			vector<long long> divs;

			for (long long base = 2; base <= 10; base++) {
				long long t = divisor(to10(to2(bin), base));
				if (t == 0) {
					flag = false;
					break;
				}
				else {
					divs.push_back(t);
				}
			}

			if (flag) {
				cout << to2(bin);
				fout << to2(bin);
				for (int di = 0; di < divs.size(); di++) cout << ' ' << divs[di];
				for (int di = 0; di < divs.size(); di++) fout << ' ' << divs[di];
				cout << endl;
				fout << endl;
				++cnt;
				if (cnt == j)
					break;
			}
		}
	}

	return 0;
}