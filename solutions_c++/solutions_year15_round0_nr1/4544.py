//============================================================================
// Name        : T.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include<iostream>
#include<cstdio>
using namespace std;
int main() {
	int T;
	int ca = 1;
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin >> T;
	while (T--) {
		int n;
		string str;
		cin >> n >> str;
		int ans = 0;
		int cnt = 0;
		for (int i = 0; i < str.length(); ++i) {
			int tmp = str[i] - '0';
			if (cnt < i && tmp) {
				ans += i - cnt;
				cnt += i - cnt;
			}
			cnt += tmp;
		}
		cout << "Case #" << ca++ << ": " << ans << endl;
	}
	return 0;
}
