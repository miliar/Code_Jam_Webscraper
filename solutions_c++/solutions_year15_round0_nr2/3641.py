/*mohitmangnani*/
#include<bits/stdc++.h>

#define ll long long int
#define pb push_back
#define mp make_pair
#define s(x) scanf("%lld", &x)
#define SET(x, a) memset(x, a, sizeof(x));
#define trace(x) cerr << #x << ": " << x << endl;
#define trace2(x, y) cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z) cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;

using namespace std;
ll a[10010];
int main()
{
	ll test,n;
	s(test);

	for (int t = 1; t <= test; t++) {
		s(n);
		ll maxmins = INT_MIN;
		for (int i = 0; i < n; i++) {
			s(a[i]);
			if (a[i] > maxmins) {
				maxmins = a[i];
			}
		}
		ll curmins,res = maxmins,curmax;
		for (int i = 1; i <= maxmins; i++) {
			curmins = 0;
			curmax = INT_MIN;
			for (int j = 0; j < n; j++) {
				if (a[j] > i) {
					if (i > curmax) {
						curmax = i;
					}

					curmins += (a[j] / i);

					if (a[j] % i != 0) {
						curmins += 1;
					}
					curmins--;
				} else {
					if (a[j] > curmax) {
						curmax = a[j];
					}
				}
			}
			curmins += curmax;

			if (curmins < res) {
				res = curmins;
			}
		}

		printf("Case #%d: %lld\n",t,res);
	}

	return 0;
}

