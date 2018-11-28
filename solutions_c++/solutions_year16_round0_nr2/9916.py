#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int T;

int main() {
	freopen("B-large.in", "r", stdin);
	scanf("%d", &T);
	for(int nt = 1; nt <= T; nt++) {
		string s;
		cin >> s;
		reverse(s.begin(), s.end());
		int flip = 0, ans = 0;
		for(char x: s) {
			if(flip^(x == '-')) {
				ans++;
				flip ^= 1;
			}
		}
		printf("Case #%d: %d\n", nt, ans);
	}
}