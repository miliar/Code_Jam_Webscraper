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
string s;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> t;
	for (int jj = 0; jj < t; jj++) {
		cin >> s;
		ll ans = 0;
		s += '+';
		for (int i = 1; i < s.length(); i++) {
			if (s[i] != s[i - 1]) {
				ans++;
				for (int j = 0; j <= (i - 1) / 2; j++) {
					if (s[j] == '-')
						s[j] = '+';
					else 
						s[j] = '-';
					if (j != i - 1 - j && s[i - 1 - j] == '-')
						s[i - 1 - j] = '+';
					else if (j != i - 1 - j)
						s[i - 1 - j] = '-';
					swap(s[j], s[i - 1 - j]);
				}
				i = 0;
			}
		}
		cout << "Case #" << jj + 1 << ": " << ans << endl;
	}
	return 0;
}