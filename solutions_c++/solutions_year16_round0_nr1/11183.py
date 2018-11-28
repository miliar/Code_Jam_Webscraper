#include <bits/stdc++.h>

using namespace std;

typedef pair < int, int > pii;
typedef long long LL;
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)

void print(int ans, int test) {
	printf("Case #%d: %d\n", test, ans);
}


int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);

	int t;
	scanf("%d", &t);
	forn(tt, t) {
		int q;
		scanf("%d", &q);
		
		if (q == 0) {
			printf("Case #%d: INSOMNIA\n", tt + 1);
			continue;
		}


		vector < bool > w(10, false);
		int cnt = 0;

		for (int i = 1; ; ++i) {
			for (int j = i * q; j; j /= 10) {
				if (!w[j % 10]) {
					++cnt;
					w[j % 10] = true;
				}
				if (cnt == 10)
					break;
			}
			if (cnt == 10) {
				print(i * q, tt + 1);
				break;
			}
		}
	}


	return 0;
}

