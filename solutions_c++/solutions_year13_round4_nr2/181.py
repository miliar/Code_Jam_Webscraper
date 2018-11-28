#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
const double pi = acos(-1.0);

int bitcount(long long num) {
	int cnt = 0;
	while (num > 0) {
		cnt++;
		num = (num - 1) / 2;
	}

	return cnt;
}

long long maxplace(long long num, int n) {
	int lim = bitcount(num - 1);
	long long ans = 1;
	for (int i = 1; i <= lim; i++)
		ans += (1ll << (n - i));

	return ans;
}

long long minplace(long long num, int n) {
	return (1ll << n) - maxplace((1ll << n) - num + 1, n) + 1;
}

int main() {
	freopen("problem_bb.in", "r", stdin);
	freopen("problem_bb.out", "w", stdout);
	
	int tc, n;
	long long p;
	cin >> tc;
	for (int tnum = 0; tnum < tc; tnum++) {
		cin >> n >> p;
		long long lb = 1;
		long long rb = (1ll << n);
		while (lb < rb) {
			long long mid = (lb + rb + 1) / 2;
			if (maxplace(mid, n) > p)
				rb = mid - 1;
			else
				lb = mid;
		}
		long long ans1 = lb;

		lb = 1;
		rb = (1ll << n);
		while (lb < rb) {
			long long mid = (lb + rb + 1) / 2;
			if (minplace(mid, n) > p)
				rb = mid - 1;
			else
				lb = mid;
		}
		long long ans2 = lb;

		cout << "Case #" << tnum + 1 << ": " << ans1 - 1 << ' ' << ans2 - 1 << endl;
	}

	return 0;
}