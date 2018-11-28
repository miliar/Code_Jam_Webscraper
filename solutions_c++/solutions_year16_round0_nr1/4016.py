#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <vector>
#include <map>
using namespace std;
typedef long long ll;
void alter(int num, int& mask) {
	if (num == 0) mask |= 1;
	while (num) {
		mask |= 1<<(num % 10);
		num /= 10;
	}
}
int main() {
	int T, N;
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> N;
		int temp = 0, mask = 0;
		bool can = false;
		for (int j = 0; j < 200 &&!can; j++) {
			temp += N;
			alter(temp, mask);
			if (mask == (1 << 10) - 1) {
				cout << "Case #" << (i + 1) << ": " << temp << endl;
				can = true;
			}
		}
		if (!can) {
			cout << "Case #" << (i + 1) << ": " << "INSOMNIA" << endl;
		}
	}
	return 0;
}