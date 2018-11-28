#include <bits/stdc++.h>

#define INF 0x3f3f3f3f
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define ForC(i, n) for (int i = 0; i < int(n); i++)
#define ForD(i, n) for (int i = int(n-1); i >= 0; i--)

using namespace std;
const double PI = acos(-1.0);

typedef long long ll;
typedef pair<int, int> pii;

bool numbers[10];
int main (void) {
	int t;
	scanf("%d", &t);
	for (int cases = 1; cases <= t; cases++) {
		memset (numbers, true, sizeof numbers);
		ll n; scanf("%lld", &n);
		if (!n) {
			printf("Case #%d: INSOMNIA\n", cases);
			continue; 
		}
		int counter = 10;
		ll i;
		for (i = 1; i < 100000; i++) {
			ll res = i * n;
			while (res) {
				ll k = res % 10;
				if (numbers[k]) {
					counter--;
					numbers[k] = false;
				}
				res /= 10;				
			}
			if (!counter) break;
		}
		printf("Case #%d: %lld\n", cases, i * n);
	}
	return 0;
}
