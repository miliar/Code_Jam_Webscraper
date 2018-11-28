#include <bits/stdc++.h> 
using namespace std;

//long long memo[1000006];

long long reverse(long long n) {
	long long res = 0, p = 1, tmp = n;
	n /= 10;
	while (n) {
		n /= 10;
		p *= 10;
	}
	while (tmp) {
		res += (tmp % 10) * p;
		tmp /= 10;
		p /= 10;
	}
	return res;
}
//
//long long fn1(long long n) {
//	return memo[n];
//}

long long nD(long long n) {
	long long ans = 0;
	while (n) {
		n /= 10;
		++ans;
	}
	return ans;
}

long long fn2(long long n) {
	long long ans = 1, i = 1, nnD = nD(n);
	if (i < 10) {
		if (n < 10) return n;
		ans += 10 - i;
		i = 10;
	}
	while (i < n) {
//		cout << i << ' ' << ans << endl;
		long long nd = nD(i);
		if (nd == nnD) {
			long long mx = i, a = n - i, up = pow(10, nd / 2) + 17;
			for (long long inc = 0; inc < up; ++inc) {
				long long r = reverse(i + inc);
				if (r <= n && r > mx && inc + n - r + 1 < a) {
					mx = r;
					a = inc + n - r + 1;
				}
			}
			ans += a;
			break;
		}
		else {
			long long tmp = i, antmp = i;
			for (long long i = 0; i < nd / 2; ++i)
				tmp /= 10;
			for (long long i = 0; i < nd / 2; ++i) {
				tmp = 10 * tmp + 9;
			}
			ans += tmp - i;
			i = reverse(tmp);
			long long tmp2 = 1;
			for (long long i = 0; i < nd; ++i)
				tmp2 *= 10;
			ans += min(tmp2 - i + 1, tmp2 - antmp);
			i = tmp2;
//			cout << i << ' ' << ans << endl;
		}
	}
	return ans;
}

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
//	fill(memo, memo + 1000006, 1e7);
//	memo[1] = 1;
//	for (long long i = 1; i < 1e6 + 1; ++i) {
//		memo[i + 1] = min(memo[i + 1], memo[i] + 1);
//		long long r = reverse(i);
//		memo[r] = min(memo[r], memo[i] + 1);
//	}

	long long tests, n;
	cin >> tests;
	for (long long tst = 1; tst <= tests; ++tst) {
		cin >> n;
		cout << "Case #" << tst << ": " << fn2(n) << '\n';
	}

}
