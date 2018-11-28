#include <iostream>
using namespace std;

char str[110] = {};
int arr[110] = {};
int temp[110] = {};
int len = 0;

int ans = 999999;

int memo[5000] = {};

bool isfinish() {
	for (int i = 0; i < len; i++) {
		if (arr[i] == -1) {
			return false;
		}
	}
	return true;
}

void change(int a) {
	for (int i = 0; i <= a; i++) {
		temp[i] = arr[i] * -1;
	}
	for (int i = 0; i <= a; i++) {
		arr[i] = temp[a - i];
	}
}

int go(int depth, int prev) {

	if (depth > ans) {
		return 99999;
	}
	if (isfinish()) {
		if (depth < ans) {
			ans = depth;
		}
		return 0;
	}

	int min = 99999;
	for (int i = 0; i < len; i++) {
		if (i != prev) {
			if (i == len - 1 || (arr[i] != arr[i + 1])) {

				change(i);
				int tmp = 99999;
				int magic = 0;
				for (int k = 0; k < len; k++) {
					int tt = arr[k];
					if (tt == -1) {
						tt = 1;
					}
					else {
						tt = 0;
					}
					magic += tt;
					magic *= 2;
				}
				if (memo[magic] == -1) {
					memo[magic] = tmp = go(depth + 1, i) + 1;
				}
				else {
					tmp = memo[magic];
				}

				if (tmp < min) {
					min = tmp;
				}
				change(i);
			}
		}
	}
	return min;
}

int main() {
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("B-small-attempt1.out", "w", stdout);


	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		for (int i = 0; i < 5000; i++) {
			memo[i] = -1;
		}

		cin >> str;
		len = 0;
		for (int i = 0; i < 110; i++) {
			if (str[i] == '\0') {
				break;
			}
			len++;
		}
		for (int i = 0; i < len; i++) {
			if (str[i] == '+') {
				arr[i] = 1;
			}
			else if (str[i] == '-') {
				arr[i] = -1;
			}
		}
		ans = 3000;
		cout << "Case #" << t << ": " << go(0, -1) << endl;;

		//cout << "Case #" << t << ": " << ans << endl;

	}

	return 0;
}


/*
cout << "d" << depth << " ";
for (int i = 0; i < len; i++) {
if (arr[i] == -1) {
cout << "-";
}
else {
cout << "+";
}
}
cout << endl;
*/