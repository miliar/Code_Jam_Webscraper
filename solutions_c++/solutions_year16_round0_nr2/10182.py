#include <bits/stdc++.h>
using namespace std;

int t;
int main() {
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for(int zzz = 1; zzz <= t; zzz++) {
		int p = 0, m = 0;
		string s;
		cin >> s;
		for(int i = 0; i < s.length(); i++) {
			if(s[i] == '+') {
				if(i == 0 or s[i] != s[i-1]) p++;
			} else {
				if(i == 0 or s[i] != s[i-1]) m++;
			}
		}
		if(s[0] == '+') {
			if(s[s.length()-1] == '+') printf("Case #%d: %d\n", zzz, 2*(p-1));
			else printf("Case #%d: %d\n", zzz, 2*p);
		} else printf("Case #%d: %d\n", zzz, 2*(m-1)+1);
		// printf("%d %d\n", p, m);
	}
}
