#include <iostream>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <set>
#include <cstring>
#include <climits>
#include <map>
#include <vector>
#include <queue>
#include <string>

using namespace std;

bool digits[10];

string s;
void add(string n) {
	int carry = 0;
	for (int i = 0; i < n.length(); i++) {
		int t = (int)(s[i]-'0');
		s[i] = (t + (int)(n[i]-'0') + carry)%10 + '0';
		if (t + (int)(n[i]-'0') + carry > 9) carry = 1;
		else carry = 0;
	}
	for (int i = n.length(); i < s.length(); i++) {
		if (carry == 0) break;
		int t = (int)(s[i]-'0');
		s[i] = (t + carry)%10 + '0';
		if (t + carry > 9) carry = 1;
		else carry = 0;
	}
	if (carry == 1) s += '1';
}

void calculateDigits() {
	for (int i = 0; i < s.length(); i++)
		digits[s[i] - '0'] = 1;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("OUTPUT.TXT", "w", stdout);
	int test;
	cin >> test;
	for (int t = 0; t < test; t++) {
		memset(digits, 0, sizeof(digits));

		string n;
		cin >> n;
		if (n.length() == 1 && n[0] == '0') {
			cout << "Case #" << t+1 << ": INSOMNIA\n";
			continue;
		}
		reverse(n.begin(), n.end());
		s = n;
		while(1) {
			calculateDigits();
			int cnt = 0;
			for (int i = 0; i < 10; i++)
				if (digits[i]) cnt++;
			if (cnt == 10) break;
			add(n);
		}
		reverse(s.begin(), s.end());
		cout << "Case #" << t+1 << ": " << s << "\n";
	}

	//system("pause");
    return 0;
}