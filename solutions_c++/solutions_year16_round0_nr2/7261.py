#include <bits/stdc++.h>
using namespace std;
#define rep(c) for (int t = 0; t < c; t++)
#define sqr(x) ((x) * (x))
const double Pi = 3.141592653589793238462643383279;
long long input() { long long n; scanf("%lld", &n); return n; }
string _input() { string s; cin >> s; return s; }
void flip(char &c) {
	c = (c == '-' ? '+' : '-');
}
int main() {
//	freopen("OUT.txt", "w", stdout);
	int n; cin >> n;
	int i = 1;
	while (n--) {
		int ans = 0;
		string s; cin >> s;
		for (int i = s.size() - 1; i >= 0; i--) {
			if (s[i] == '-') {
				for (int j = i; j >= 0; j--) {
					flip(s[j]);
				}
				ans++;
			}
		}
		cout << "Case #" << i << ": " <<  ans << endl;
		i++;
	}
}