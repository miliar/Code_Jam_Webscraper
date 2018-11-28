#include <set>
#include <map>
#include <vector>
#include <iostream>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <cmath>
#include <string>
#include <climits>
#include <ctime>
#include <cassert>
#include <bitset>
#include <cstdio>

using namespace std;

#define mp make_pair
#define ll long long

ll n, t;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> t;
	for (int jj = 0; jj < t; jj++) {
		cin >> n;
		set<int> s;
		for (int i = 1; i <= 1000000; i++) {
			ll x = n * i;
			if (!x)
				s.insert(0);
			while (x) {
				s.insert(x % 10);
				x /= 10;
			}
			if (s.size() == 10) {
				cout << "Case #" << jj + 1 << ": "  << n * i << endl;
				break;
			}
		}
		if (s.size() != 10) {
			cout << "Case #" << jj + 1 << ": " << "INSOMNIA" << endl;
		}
	}
	return 0;
}