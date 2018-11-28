#include <algorithm>
#include <iostream>
#include <stack>
#include <vector>
#include <string>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <sstream>
#include <iomanip>

using namespace std;

#define ll long long
#define ull unsigned long long
#define len(x1, y1, x2, y2) (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)

const double pi = 2 * acos(0.);
using namespace std;

#define ll long long

const int INF = 1000000007;

int gcd(int a, int b) {
	while (b) {
		a %= b;
		swap(a, b);
	}
	return a;
}

#define rev(s) (s = (s == '+' ? '-' : '+'))

void reverse(string &s, int r) {
	for (int i = 0; i <= r / 2; ++i) {
		swap(s[i], s[r - i]);
		rev(s[i]);
		rev(s[r - i]);
	}
	if (r % 2 == 0) rev(s[r / 2]);
}

string solve() {
	string s;
	cin >> s;

	int r = s.size() - 1;
	int count = 0;
	while (r != -1) {
		while (r >= 0 && s[r] == '+') r--;

		int near_r = 0;
		while (near_r < s.size() && s[near_r] == '+') near_r++;
		near_r--;
		if (near_r >= 0) {
			reverse(s, near_r);
			count++;
		}
		if (r >= 0) {
			reverse(s, r);
			count++;
		}
	}
	return to_string(count - 1);
}

int main()
{
	ios::sync_with_stdio(false);
	freopen("B-large.in", "r", stdin);
	freopen("out", "w", stdout);
	int n;
	cin >> n;
	for (int i = 0; i < n; ++i) {
		cout << "Case #" << (i + 1) << ": " << solve() << "\n";
	}
}