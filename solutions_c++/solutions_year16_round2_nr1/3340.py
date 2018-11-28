#include <bits/stdc++.h>
using namespace std;

//int main() {
//	string coderString, jammerString;
//	int t;
////	freopen("out.txt", "w", stdout);
//	cin >> t;
//	for (int tc = 1; tc <= t; ++tc) {
//		cin >> coderString >> jammerString;
//		int bigger = 0;
//		for (int i = 0; i < coderString.length(); ++i) {
//			if (coderString[i] == '?' ^ jammerString[i] == '?') {
//				if (coderString[i] == '?') {
//					if (bigger == 0) {
//						coderString[i] = jammerString[i];
//					} else {
//						if (bigger == 1) {
//							coderString[i] = '0';
//						} else {
//							coderString[i] = '9';
//						}
//					}
//				} else {
//					if (bigger == 0) {
//						jammerString[i] = coderString[i];
//					} else {
//						if (bigger == 1) {
//							jammerString[i] = '9';
//						} else {
//							jammerString[i] = '0';
//						}
//					}
//				}
//			} else {
//				if (coderString[i] == '?' && jammerString[i] == '?') {
//					if (bigger == 0) {
//						coderString[i] = jammerString[i] = '0';
//					} else {
//						if (bigger == 1) {
//							coderString[i] = '0';
//							jammerString[i] = '9';
//						} else {
//							jammerString[i] = '0';
//							coderString[i] = '9';
//						}
//					}
//				} else {
//					if (bigger == 0) {
//						bigger = coderString[i] == jammerString[i] ? 0: coderString[i] > jammerString[i] ? 1 : -1;
//					}
//				}
//			}
//		}
//		cout << "Case #" << tc << ": " << coderString << " " << jammerString << endl;
//	}
//	return 0;
//}

string digits[10] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX",
		"SEVEN", "EIGHT", "NINE" }; // zero, four, six, seven, eight, five, two, nine, one, three
int dg[10] = { 0, 4, 6, 7, 8, 5, 2, 9, 1, 3 };
vector<vector<int> > v;
string s;
int coderStringhars[30], t;

bool digitExists(int digit) {
	for (int i = 0; i < 30; ++i) {
		if (v[digit][i] > coderStringhars[i]) {
			return false;
		}
	}
	return true;
}

void substractDigit(int digit) {
	for (int i = 0; i < 30; ++i) {
		coderStringhars[i] -= v[digit][i];
	}
}

int main() {
	ios::sync_with_stdio(0);
	freopen("out.txt", "w", stdout);
	for (int i = 0; i < 10; ++i) {
		v.push_back(vector<int>());
		v[i].resize(30);
		for (int j = 0; j < digits[i].length(); ++j) {
			int tmpChar = digits[i][j] - 'A';
			v[i][tmpChar]++;
//			printf("v[%d,%d]:%d\n", i, tmpChar, v[i][tmpChar]);
		}
	}
	cin >> t;
	for (int tc = 1; tc <= t; ++tc) {
		string ans = "";
		memset(coderStringhars, 0, sizeof coderStringhars);
		cin >> s;
		for (int i = 0; i < s.length(); ++i) {
			int tmpChar = s[i] - 'A';
			coderStringhars[tmpChar]++;
//			printf("coderStringhar[%d]:%d\n", tmpChar, coderStringhars[tmpChar]);
		}
		for (int i = 0; i < 10; ++i) {
			int d = dg[i];
			while (digitExists(d)) {
//				printf("%d exists\n", d);
//				printf("s now %s\n", ans.c_str());
				ans += char(d + '0');
				substractDigit(d);
			}
		}
		sort(ans.begin(), ans.end());
		cout << "Case #" << tc << ": " << ans << endl;
	}
	return 0;
}
