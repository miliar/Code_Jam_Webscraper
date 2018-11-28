#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define mk make_pair
#define pi pair<int, int>
#define fi first
#define se second
using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for(int tt = 1; tt <= t; tt++) {
		printf("Case #%d: ", tt);
		ll n;
		scanf("%lld", &n);
		if(n == 0) {
			printf("INSOMNIA\n");
			continue;
		}
		int i = 1;
		set < int > s;
		while(1) {
			ll val = n * i;
			while(val > 0) {
				s.insert(val % 10);
				val /= 10;
			}
			if(s.size() == 10) {
				n = n * i;
				break;
			}
			i++;
		}
		printf("%lld\n", n);
	}
	return 0;
}

