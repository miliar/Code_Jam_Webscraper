#include <iostream>
#include <cstdio>
#include <string>
#include <cmath>

using namespace std;

int numlen(long long a) {
	int ans = 0;
	if (a == 0) return ans;
	while (a > 0) {
		ans++;
		a /= 10;
	}
	return ans;
}

long long reversenum(long long a) {
	int ans = 0;
	while (a > 0) {
		ans *= 10;
		ans += a % 10;
		a /= 10;
	}

	return ans;
}

long long get(long long n) {
//cerr << " > " << n << "\n";
	long long ans = 0;
	if (n <= 20) {
		return n;
	}

	if (n % 10 == 0) {
		return get(n - 1) + 1;
	}
	int l = (numlen(n) + 1) / 2;
	int r = (numlen(n)) / 2;
	long long tenl = pow(10, l);
	long long tenr = pow(10, r);

	long long taill = n % tenl;
	long long n2 = reversenum(n - taill + 1);
	long long tailr = n2 % tenr;

	if (tailr == 1) {
//cerr << "lol1\n";
		ans += taill + get(n - taill);
	}
	else {
		ans += taill + tailr + get(n2 - tailr);
	}

//cerr << tenl << " " << tenr << " " << taill << " " << tailr << " " << n << " " << n2 <<"\n";

	return ans;
}

int main() {
	long long n;
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		cin >> n;
		long long ans = get(n);
		cout << "Case #" << t + 1 << ": " << ans << "\n";
	}
	return 0;
}



