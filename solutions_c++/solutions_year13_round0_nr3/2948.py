#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>

using namespace std;

#define ll long long

bool isPalindrome(ll x) {
	ll rev = 0;
	ll t = x;

	while (t > 0) {
		rev = rev * 10 + t % 10;
		t /= 10;
	}

	return x == rev;
}

int bruteforce(int start, int end) {
	int count = 0;
	for (ll i = 1; i <= end; i++) {
		if (isPalindrome(i) && i * i >= start && i * i <= end && isPalindrome(i * i)) {
			count++;
		}
	}
	return count;
}

int generateRec(ll num, int limit, int curr, int start, int end) {
	int count = 0;

	if (curr == limit) {
		if (isPalindrome(num) &&
			num * num >= start &&
			num * num <= end &&
			isPalindrome(num * num)) {
			// cout << num << endl;
			return 1;
		}
		else {
			return 0;
		}
	}

	if (num != 0) {
		count += generateRec(num * 10 + 0, limit, curr + 1, start, end);
	}

	count += generateRec(num * 10 + 1, limit, curr + 1, start, end);
	count += generateRec(num * 10 + 2, limit, curr + 1, start, end);
	return count;
}

int cleverAlgo(int start, int end) {
	int ans = 0;

	if (1 >= start && 1 <= end) {
		ans++;
	}

	if (4 >= start && 4 <= end) {
		ans++;
	}

	if (9 >= start && 9 <= end) {
		ans++;
	}

	for (int i = 2; i <= 8; i++) {
		ans += generateRec(0, i, 0, start, end);
	}
	return ans;
}

int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	//for (ll i = 1; i <= 300000000; i++) {
	//	if (isPalindrome(i) && isPalindrome(i * i)) {
	//		cout << i << ' ' << i * i << endl;
	//	}
	//}

	//for (int i = 0; i < 100; i++) {
	//	int x = rand() % 1000000 + 1;
	//	int y = rand() % 1000000 + 1;
	//	cout << (bruteforce(min(x, y), max(x, y)) == cleverAlgo(min(x, y), max(x, y))) << endl;
	//}

	//cout << (bruteforce(1, 4) == cleverAlgo(1, 4)) << endl;
	//cout << (bruteforce(10, 120) == cleverAlgo(10, 120)) << endl;
	//cout << (bruteforce(1, 100000) == cleverAlgo(1, 100000)) << endl;
	//cout << (bruteforce(1234, 12146) == cleverAlgo(1234, 12146)) << endl;
	//cout << (bruteforce(122222, 122223) == cleverAlgo(122222, 122223)) << endl;
	//cout << (bruteforce(555, 555999) == cleverAlgo(555, 555999)) << endl;
	//cout << (bruteforce(101010, 2101010) == cleverAlgo(101010, 2101010)) << endl;

	int n;
	cin >> n;

	for (int t = 0; t < n; t++) {
		int s, e;
		cin >> s >> e;
		printf("Case #%d: %d\n", t + 1, cleverAlgo(s, e));
	}

	return 0;
}