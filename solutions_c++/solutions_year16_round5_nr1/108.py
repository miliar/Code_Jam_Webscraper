#include<bits/stdc++.h>

using namespace std;
#define For(i,l,r) for (int i = l; i <= r; ++i)
#define Cor(i,l,r) for (int i = l; i >= r; --i)
#define UPD(a,b) { a = (a + (b)) % MD; }

const int MD = 1000000007;
const int INF = 0x3f3f3f3f;
const double pi = acos(-1.0);

string s;
int n;
int main() {
	int T; cin >> T;
	For(TK,1,T) {
		cin >> s;
		n = s.length();
		int ans = 0;
		while (1) {
			bool found = false ;
			for (int i = 0; i + 1 < s.length(); ++i) if (s[i] == s[i + 1]) {
				found = true;
				s = s.substr(0,i) + s.substr(i + 2);
				break ;
			}
			if (found) ans += 10; else break ;
		}
		ans += s.length() / 2 * 5;
		printf("Case #%d: %d\n", TK, ans);
	}
	return 0;
}
