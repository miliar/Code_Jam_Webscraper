#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <string>

#define LL long long
#define LD long double

using namespace std;

LD a[1000], b[1000];
LL n, lk, ln, ans1, ans2;
LL T;

int main() {
	freopen("ex.in", "r", stdin);
	freopen("ex.out", "w", stdout);

	cin >> T;
	for (int it = 0; it < T; it++) {
        cin >> n;

        ans1 = 0;
        ans2 = n;
        for (int i = 0; i < n; i++) cin >> a[i];
        for (int i = 0; i < n; i++) cin >> b[i];

        sort(a, a + n);
        sort(b, b + n);
        ln = 0;
        lk = 0;
        while ((ln < n) && (a[ln] <= b[lk])) ln++;
        while (ln < n) {
            ans1++;
            lk++;
            ln++;
            while ((ln < n) && (a[ln] <= b[lk])) ln++;
        }

        ln = 0;
        lk = 0;
        while ((lk < n) && (a[ln] >= b[lk])) lk++;
        while (lk < n) {
            ans2--;
            lk++;
            ln++;
            while ((lk < n) && (a[ln] >= b[lk])) lk++;
        }

		cout << "Case #" << it + 1 << ": " << ans1 << " " << ans2 << endl;
	}
	return 0;
}
