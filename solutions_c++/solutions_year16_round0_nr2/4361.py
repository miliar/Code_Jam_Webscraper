#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <time.h>

using namespace std;
const int N = 1e6 + 5;

string rev(string s, int n) {
	for (int i = 0; i < n; i++) {
		int j = (n - 1 - i);
		if (j > i) swap(s[i], s[j]);
		if (s[i] == '-') s[i] = '+';
		else s[i] = '-';
	}
	return s;
}

int calc(string s) {
	int ans = 0;
	int j = s.length() - 1;
	while (j >= 0 && s[j] == '+') j--;
	while (j >= 0) {
		int i = 0;
		for (i = 0; i < s.length() && s[i] == '+'; i++);
		if (i > 0) {
			ans++;
			s = rev(s, i);
		}
		ans++;
		s = rev(s, j + 1);
		while (j >= 0 && s[j] == '+') j--;
	}
	return ans;
}
int main(){
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		string s;
		cin >> s;
		cout << "Case #" << i << ": " << calc(s) << endl;
	}
	return 0;
}