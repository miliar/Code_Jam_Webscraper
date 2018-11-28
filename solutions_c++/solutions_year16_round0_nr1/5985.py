#define DEBUG 0
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

bool found[10];

int main()
{
	cerr << fixed << setprecision(0);

	if (!DEBUG) {
		freopen("in", "r", stdin);
		freopen("out", "w", stdout);
	}

	int _c, _start = static_cast<int>(clock());
	scanf("%d", &_c);
	

	for(int _cc = 1; _cc <= _c; ++_cc) {
		int _t = static_cast<int>(clock());
		printf("Case #%d: ", _cc);

		ll n;
		cin >> n;
		ll orig = n;

		if (n == 0) {
			printf("INSOMNIA\n");
			continue;
		}
		memset(found, 0, sizeof(found));
		int cnt = 0;

		for (int i = 1; i <= 100; ++i) { 
			ll tmp = n;
			while (tmp != 0) {
				if (!found[tmp % 10]) {
					found[tmp % 10] = true;
					++cnt;
				}
				tmp /= 10;
			}
			if (cnt == 10) {
				break;
			}
			n += orig;
		}

		printf("%lld\n", n);

		cerr << "[Case #" << _cc << " complete, " << static_cast<int>(clock() - _t) << " ms, " << 100. * _cc / _c << "%]" << endl;
	}

	cerr << "Total time: " << static_cast<int>(clock() - _start) << " ms" << endl;

	return 0;
}

