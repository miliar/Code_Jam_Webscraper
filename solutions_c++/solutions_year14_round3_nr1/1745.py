#include <iostream>
#include <vector>
#include <stack>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <cmath>

using namespace std;

long long Euclid(long long P, long long Q);

int main()
{
	int T;
	long long P, Q;

	cin >> T;
	for (int CCnt = 1; CCnt <= T; CCnt++) {
		cout << "Case #" << CCnt << ": ";
		scanf("%d/%d", &P, &Q);
		long long gcd = Euclid(P, Q);
		P /= gcd;
		Q /= gcd;
		long long tp = 2;
		while (tp < Q) {
			tp *= 2;
		}
		if (tp > Q) {
			cout << "impossible\n";
		} else {
			int ans = 0;
			while (P / Q < 1) {
				Q /= 2;
				ans++;
			}
			cout << ans << endl;
		}
	}

	return 0;
}

long long Euclid(long long P, long long Q)
{
 	while (Q > 0) {
		long long t = Q;
		Q = P % Q;
		P = t;
	}
	return P;
}
