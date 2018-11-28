#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long ll;
int T, n;
string s;
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin>>T;
	for (int cas = 1; cas <= T; ++cas) {
		cin>>n>>s;
		ll ans = 0;
		ll tot = s[0] - '0';
		for (int i = 1; i <= n; ++i) {
			if (tot >= i) {
				tot += (ll)(s[i] - '0');
			} else {
				ll delta = (ll)i - tot;
				ans += delta;
				tot += delta + (ll)(s[i] - '0');
			}
		}
		printf("Case #%d: ",cas);
		cout<<ans<<endl;
	}
	return 0;
}
