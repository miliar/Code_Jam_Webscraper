#include <bits/stdc++.h>
using namespace std;











int main() {
	freopen("A-large.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int t, cas = 1;
	cin >> t;
	while(t--) {
		long long n;
		cin >> n;
		set<int>st;
		int i = 1;
		for(;i <= 1000000;i++) {
			long long x = n * i;
			while(x) {
				st.insert(x % 10);
				x /= 10;
			}
			if(st.size() == 10) {
				break;
			}
		}
		if(st.size() == 10) {
			printf("Case #%d: %lld\n", cas, n * i);
		} else {
			printf("Case #%d: INSOMNIA\n", cas);
		}
		cas++;
	}
	return 0;
}
