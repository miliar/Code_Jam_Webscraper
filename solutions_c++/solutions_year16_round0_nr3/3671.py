#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <time.h>

using namespace std;
const int N = 1e6 + 5;

long long check(string s, int b) {
	long long d = 1;
	long long ans = 0;
	
	for (int i = 0; i < s.length(); i++) {
		ans += (s[i] - '0') * 1LL * d;
		d *= b;
	}

	for (long long i = 2; i * i <= ans; i++) {
		if (ans % i == 0) {
			return i;
		}
	}
	return -1;
}

vector<int> calc(string s) {
	vector<int> ans;
	for (int i = 2; i <= 10; i++) {
		int d = check(s, i);
		if (d == -1) {
			return vector<int>();
		}
		else {
			ans.push_back(d);
		}
	}
	return ans;
}

int main() {
#ifdef _DEBUG 
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif 
	int n = 16;
	int j = 50;
	cout << "Case #1:" << endl;
	for (int i = 0; i < (1 << n) && j > 0; i++) {
		if (((1 << (n - 1)) & i) && (i & 1)) {
			string s;
			int x = i;
			while (x > 0) {
				s.push_back('0' + (x % 2));
				x /= 2;
			}
			vector <int> ans = calc(s);
			if (!ans.empty()) {
				reverse(s.begin(), s.end());
				cout << s << " ";

				for (int i = 0; i < ans.size(); i++) {
					cout << ans[i] << " ";
				}
				cout << endl;
				j--;
			}
		}
	}
}