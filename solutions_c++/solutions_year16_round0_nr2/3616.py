#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
#define sz(x) ((int)(x).size())

void flip(char &ch) {
	switch (ch) {
		case '+' : {
			ch = '-';
			break;
		}
		case '-' : {
			ch = '+';
			break;
		}
	}
}

int main() {
	int test;
	cin >> test;
	for (int test_case = 1; test_case <= test; ++test_case) {
		string str;
		cin >> str;
		cout << "Case #" << test_case << ": ";
		char ch = '-';
		int cnt = 0;
		for (int i = sz(str) - 1; i >= 0; i--) {
			if (ch == str[i]) {
				flip(ch);
				cnt++;
			}
		}
		cout << cnt << endl;
	}
	return 0;
}
