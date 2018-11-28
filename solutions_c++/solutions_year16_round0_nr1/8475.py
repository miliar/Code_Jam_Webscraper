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

string solve() {
	ll n;
	cin >> n;
	if (n == 0) return "INSOMNIA";

	ll count = 0;
	ll mul = 1;
	ll tmp;
	vector<char> u(10, false);
	while (count != 10) {
		tmp = mul * n;
		while (tmp != 0) {
			if (!u[tmp % 10]) {
				u[tmp % 10] = true;
				count++;
			}
			tmp /= 10;
		}
		mul++;
	}

	string res = to_string(n * (mul - 1));
	return res;
}

int main()
{
	ios::sync_with_stdio(false);
	freopen("A-large.in", "r", stdin);
	freopen("out", "w", stdout);
	int n;
	cin >> n;
	for (int i = 0; i < n; ++i) {
		cout << "Case #" << (i + 1) << ": " << solve() << "\n";
	}
}