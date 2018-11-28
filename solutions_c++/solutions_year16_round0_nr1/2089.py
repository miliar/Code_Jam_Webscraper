#include <bits/stdc++.h>

using namespace std;

#define fr(a, b, c) for(int a = b; a < c; a++)

typedef long long ll;

ll n;
short mask[10000111];
short END = (1 << 10) - 1;

int main() {
	ios_base::sync_with_stdio(false);
	
	fr(i, 0, 10000111) {
		int x = i;
		
		do {
			mask[i] = mask[i] | (1 << (x%10));
			x /= 10;
		} while(x);
	}
	
	int T;
	
	cin >> T;
	
	fr(cas, 1, T+1) {
		cin >> n;
	
		if(n == 0) {
			printf("Case #%d: INSOMNIA\n", cas);
			continue;
		}

		ll x = n;
		short m = mask[n];
		
		while(m != END) {
			x += n;
			m = m | mask[x];
		}
	
		printf("Case #%d: %lld\n", cas, x);
	}

	return 0;
}
