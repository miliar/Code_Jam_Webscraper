#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

long long trans_to_ten(string str, int n) {
	long long res = 0;
	for (int i = 0; i < 16; ++i) {
		if (str[i] == '1') res += pow(n, 15 - i);
	}
	return res;
}

long long check_prime(long long x) {
	long long sqrtx = sqrt(x);
	for (long long i = 2; i <= sqrtx; ++i) {
		if (x%i == 0) return i;
	}
	return 0;
}

vector<string> create_nums() {
	vector<string> res;
	string str = "1000000000000001";
	int i = 14;
	while (i >= 0) {
		int j = 14;
		while (j > 0 && str[j] == '1') {
			str[j] = '0';
			j--;
		}
		str[j] = '1';
		if (i == j) i--;
		res.push_back(str);
	}
	return res;
}

int main() {
	ofstream output("C_small_answer.txt");
	vector<string> myvec = create_nums();
	int count = 0;
	output << "Case #1:";
	for (int i = 0; i < myvec.size(); ++i) {
		int a[11] = { 0 };

		// check each number if it is a prime number
		for (int j = 2; j <= 10; ++j) {
			long long temp = trans_to_ten(myvec[i], j);
			a[j] = check_prime(temp);
			if (a[j] == 0) break;
		}

		if (a[10]) {
			output << endl;
			output << myvec[i];
			for (int j = 2; j <= 10; ++j) {
				output << ' ' << a[j];
			}
			count++;
		}
		if (count == 50) break;
	}

	return 0;
}