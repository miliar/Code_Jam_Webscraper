#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <map>
using namespace std;
typedef long long ll;
int main() {
	int T;
	string s;
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> s;
		s += s[s.size() - 1] == '+' ? '-' : '+';
		int ans = 0;
		char front = s[0];
		for (int i = 1; i < s.size(); i++) {
			if (s[i] == front) {
				if (s[i - 1] != front) {
					ans++;
					front = s[i - 1];
				}
			}
		}
		if (front == '-') ans++;
		printf("Case #%d: %d\n", i + 1, ans);
	}
	return 0;
}