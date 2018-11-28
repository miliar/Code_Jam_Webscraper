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

ll k, c, s, t;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> t;
	for (int jj = 0; jj < t; jj++) {
		cin >> k >> c >> s;
		ll z = 1;
		for (int i = 1; i < c; i++) 
			z *= k;
		cout << "Case #" << jj + 1 << ": ";
		for (int i = 0; i < k; i++) {
			cout << z * i + 1 << ' ';
		}
		cout << endl;
	}
	return 0;
}