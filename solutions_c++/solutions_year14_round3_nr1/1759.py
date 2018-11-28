#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <algorithm>

#define IN_FILE "input.txt"
#define OUT_FILE "output.txt"

#define all(a) (a).begin(),(a).end()
#define sz(a) (a).size()
#define len(a) (a).length()

#define ll long long

using namespace std;

int gcd (ll a, ll b) {
	while (b) {
		a %= b;
		swap (a, b);
	}
	return a;
}

int main() {

	freopen(IN_FILE, "r", stdin);
	freopen(OUT_FILE, "w", stdout);

	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		ll P, Q;
		scanf("%lld/%lld", &P, &Q);

		if (P == 0) {
			printf("Case #%d: impossible\n", t + 1);
			continue;
		}

		ll g = gcd(P, Q);
		P /= g;
		Q /= g;

		ll p = 1;
		int e = 0;
		while (p != Q && e < 41) {
			p <<= 1;
			++e;
		}

		if (e == 41) {
			printf("Case #%d: impossible\n", t + 1);
			continue;
		}

		ll pp = 1;
		int ee = 0;
		while (pp <= P && ee < 41) {
			pp <<= 1;
			++ee;
		}

		printf("Case #%d: %d\n", t + 1, (e - ee) + 1);
	}

	return 0;
}