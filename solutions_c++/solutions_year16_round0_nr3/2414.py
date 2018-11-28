#include <stdio.h>
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;

string convert(int num);
long long confirm(string str, long long digit);
long long sosu(long long num);

int main() {

	int T;
	scanf("%d", &T);

	for (int tt = 1; tt <= T; tt++) {

		int N, J;
		scanf("%d %d", &N, &J);

		vector<pair<string, vector<long long> > > myV;

		int cnt = 0;

		for (int i = 32769; i <= 65535; i+=2) {
			string str = convert(i);
//			cout << i << " : " << str << endl;

			bool chk = true;

			vector<long long>ans;

			for (long long d = 2; d <= 10; d++) {

				long long temp = confirm(str, d);
				if (temp == -1) {
					chk = false;
					break;
				}
				else {
					ans.push_back(temp);
				}
			}

			if (chk) {
				myV.push_back(make_pair(str, ans));
				cnt++;
				if (cnt == J) break;
			}
		}
		printf("Case #%d:\n", tt);
		for (int i = 0; i < myV.size(); i++) {
			printf("%s ", myV[i].first.c_str());
			for (int j = 0; j < 9; j++) printf("%lld ", myV[i].second[j]);
			printf("\n");

//			cout << myV[i] << endl;
		}
	}
}

string convert(int num) {

	int num_temp = num;
	string str;

	while (num > 0) {
		if (num % 2 == 1) str.push_back('1');
		else str.push_back('0');
		num /= 2;
	}

	reverse(str.begin(), str.end());
	return str;
}

long long confirm(string str, long long digit) {

	long long num = 0;
	long long mul = 1;

	for (int i = str.size() - 1; i >= 0; i--) {
		if (str[i] == '1') {
			num += mul;
		}
		mul *= digit;
	}
	return sosu(num);
}

long long sosu(long long num) {

	for (long long i = 2; i <= sqrt(num); i++) {
		if (num%i == 0) {
			return i;
		}
	}
	return -1;
}