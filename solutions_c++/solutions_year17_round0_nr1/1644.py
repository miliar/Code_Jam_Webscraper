#define _CRT_SECURE_NO_WARNINGS

#include <algorithm>
#include <assert.h>
#include <bitset>
#include <cmath>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> llp;

int main() {
	ll t;
	cin >> t;

	for (ll q = 0; q < t; q++) {
		string s;
		ll k, c = 0;
		cin >> s >> k;

		for (ll i = 0; i < s.length() - k + 1; i++) {
			if (s[i] == '-') {
				c++;
				for (ll j = 0; j < k; j++) {
					s[i + j] = (s[i + j] == '-' ? '+' : '-');
				}
			}
		}

		bool flag = true;
		for (ll i = 0; i < s.length(); i++) {
			if (s[i] != '+') { flag = false; }
		}

		cout << "Case #" << q + 1 << ": ";
		if (flag) {
			cout << c;
		}
		else {
			cout << "IMPOSSIBLE";
		}
		cout << "\n";
 	}

	return 0;
}