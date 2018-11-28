#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>

using namespace std;

typedef long long ll;

int t;


int main() {
	if(fopen("B.in","r")) freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	cin >> t;
	for(int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		string s;
		cin >> s;
		if(s.length() == 1) {
			if(s[0] == '-') cout << 1 << "\n";
			else cout << 0 << "\n";
			continue;
		}
		int cnt = 0;
		for(int j = 1; j < s.length(); j++) {
			if(s[j] != s[j-1]) {
				cnt++;
			}
		}
		if(s[s.length() - 1] == '-') {
			cnt++;
		}
		cout << cnt << "\n";
	}
	return 0;
}