#include <bits/stdc++.h>
using namespace std;

#define oo (1LL<<30)
#define SZ(x) ((int)x.size())
#define valid(x,u) (x>=0 && x<u)
#define ll (long double)

int di [] = {0, 0, 1, -1, 1, 1, -1, -1};
int dj [] = {1, -1, 0, 0, 1, -1, 1, -1};

bool fu(long long num) {
	while(num > 1) {
		if(num % 2)
			return false;
		num /= 2;
	}
	return true;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	freopen("in.in", "rt",stdin);
	freopen("out.out", "wt", stdout);

	int t, id = 0; cin >> t;
	while(t --) {
		cout << "Case #" << ++id << ": ";
		long long a, b; char c; cin >> a >> c >> b;
		long long g = __gcd(a, b);
		a /= g, b /= g;
		b *= 2;
		bool good = fu(b);
		if(good) {
			int ans = 0; b /= 2;
			while(b > 1 && a < b) {
				b /= 2;
				++ ans;
			}
			cout << ans << "\n";
		} else {
			cout << "impossible\n";
		}
	}

	return 0;
}
