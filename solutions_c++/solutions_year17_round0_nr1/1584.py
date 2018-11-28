//============================================================================
// Name        : C.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <stack>
using namespace std;
#define MAXN 2010
#define oo 1e9
#define MOD 1000000007
typedef long long LL;
bool check(string str) {
	for (int i = 0; i < str.length(); ++i) {
		if (str[i] == '-') {
			return false;
		}
	}
	return true;
}
int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		int n;
		string str;
		cin >> str >> n;
		int ans = 0;
		for (int i = 0; i + n <= str.length(); ++i) {
			if (str[i] == '-') {
				++ans;
				for (int j = i; j < i + n; ++j) {
					str[j] = str[j] == '-' ? '+' : '-';
				}
			}
		}
		if (check(str)) {
			printf("Case #%d: %d\n", t, ans);
		} else {
			printf("Case #%d: IMPOSSIBLE\n", t);
		}
	}
	return 0;
}
