#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>

using namespace std;

int main() {
	// freopen("input.txt", "r", stdin);

	int testcase;
	cin >> testcase;

	for (int T = 0; T < testcase; T++) {
		char arr[111];
		cin >> arr;
		int len = strlen(arr);

		int output = 0;
		while (true) {
			int f = 0;
			for (int i = 0; i < len; i++) {
				if (arr[i] == '+') f++;
			}
			if (f == len) {
				break;
			}


			char top = arr[0];
			int j = 1;
			for (j = 1; j < len; j++) {
				if (arr[j] != top) {
					break;
				}
			}
			for (int i = 0; i < j; i++) {
				arr[i] = (arr[i] == '+') ? '-': '+';
			}

			output++;
		}

		cout << "Case #" << T + 1 << ": " << output << endl;
	}
	return 0;	// 정상종료 시 반드시 0을 리턴해야 합니다.
}