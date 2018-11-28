#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <string>
#include <queue>
#include <assert.h>

using namespace std;
typedef unsigned long long int LLI;

bool f(LLI val, vector<LLI>& v) {
	if (val % 2 == 0) return false;
	v.clear();
	for (int i = 2; i <= 10; i++) {
		LLI cnt = 0;
		LLI val1 = val;
		LLI pow = 1;
		while (val1 > 0) {
			cnt += (val1 % 2) * pow;
			val1 /= 2;
			pow *= i;
		}
		for (LLI j = 2; j <= sqrt(cnt) + 1; j++) {
			if (cnt % j == 0) {
				v.push_back(j);
				break;
			}
		}
		if (v.size() < i - 1) return false;
	}
	return true;
}
void print(LLI val, vector<LLI> v) {
	string res;
	while (val > 0) {
		if(val%2 == 1) res.push_back('1');
		else res.push_back('0');
		val /= 2;
	}
	reverse(res.begin(), res.end());
	cout << res;
	for (int i = 0; i < v.size(); i++) {
		cout << " " << v[i];
	}
	cout << "\n";
}
int main() {
	freopen("output.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int N = 16, J = 50;
	LLI val = (1 << (N-1)) + 1;
	cout << "Case #1:\n";
	while (J > 0) {
		vector<LLI> v;
		if (f(val, v)) {
			print(val, v);
			J--;
		}
		val++;
	}
	/*for (int i = 0; i < 50; i++) {
		string s;
		cin >> s;
		for (int j = 0; j < 9; j++) {
			LLI val = 0;
			LLI pow = 1;
			for (int k = 0; k < 16; k++) {
				val += (s[15 - k]-'0') * pow;
				pow *= (j + 2);
			}
			LLI div;
			cin >> div;
			if (val % div != 0) {
				cout << "Her\n";
			}
		}
	}*/
	return 0;
}