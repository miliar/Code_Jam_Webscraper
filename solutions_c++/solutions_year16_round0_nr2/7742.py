#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstring>
using namespace std;

char Data[105];

int solve() {
	int len = strlen(Data);
	--len;
	bool flip = false;
	int flipCnt = 0;
	for (int i = len; i >= 0; --i) {
		if (Data[i] == '-') {
			if (flip == false) {
				++flipCnt;
				flip = true;
			}
		}
		if (Data[i] == '+') {
			if (flip == true) {
				++flipCnt;
				flip = false;
			}
		}
	}
	return flipCnt;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		scanf("%s", &Data);
		cout << "Case #" << i << ": ";
		cout << solve() << endl;
	}

	return 0;
}
