#include <bits/stdc++.h>
using namespace std;
int T, K;
string s;
int flip[2000];
bool st[2000];
int main() {
	freopen("A-large.in", "r", stdin); 
	freopen("A-large.out", "w", stdout); 
	cin >> T;
	for(int k=1; k<=T; k++){
		cin >> s >> K;
		memset(flip, 0, sizeof flip);
		for(int u = 0; u < s.length(); u++) st[u] = s[u] & 2; 
		bool fl = 0, flag = 1;
		int n = 0;
		for(int u = 0; u < s.length(); u++) {
			if (flip[u]) fl ^= 1;
			if (fl) st[u] ^= 1;
			if (!st[u] && (u+K <= s.length())) {
				st[u] ^= 1; 
				fl ^= 1; 
				flip[u+K] = 1;
				n++;
			}
			flag &= st[u];
		}
		if (!flag) {
			cout << "Case #" << k << ": IMPOSSIBLE" << endl;
		} else {
			cout << "Case #" << k << ": " << n << endl;
		}
	}
}
