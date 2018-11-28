#include <iostream>
#include <cstdio>
#include <cmath>

typedef long long ll;

using namespace std;

bool ispalindrome(ll n) {

	ll m = n, reverse = 0;

	while (n > 0) {

		reverse *= 10;
		reverse += n % 10;
		n *= 0.1;
	}

	return reverse == m;
}

bool isfairpalindrome(ll n) {

	double square = sqrt(n);

	return (square == (ll)square) ? (ispalindrome(n) && ispalindrome((ll) square)) : false;
}

int main() {

	ll a = 0, b = 0, count = 0;
	int t = 0;
	scanf("%d", &t);
	for (int i = 1; i <= t && ((count = 0) || true); ++i)
	{
		scanf("%lld %lld", &a, &b);
		for (ll j = a; j <= b; ++j)
		{
			if (isfairpalindrome(j)) {
				count++;
			}
		}
		printf("Case #%d: %lld\n", i, count);
	}
}
