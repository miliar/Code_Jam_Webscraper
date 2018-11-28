/*
 * a.cpp
 *
 */

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <complex>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define forn(i, n) for (int i = 0; i < (n); ++i)
#define foreach(it, a) for (__typeof((a).begin()) it = (a).begin(); it != (a).end(); ++it)

template<typename T> inline void ignore(T) {}

int main(void) {
	int t; cin >> t;
	forn(k, t) {
		int r;
		vector<int> count(16, 0);
		cin >> r;
		forn(i, 4) {
			forn(j, 4) {
				int x; cin >> x;
				if (i == r-1) { count[x - 1] += 1; }
			}
		}
		cin >> r;
		forn(i, 4) {
			forn(j, 4) {
				int x; cin >> x;
				if (i == r-1) { count[x - 1] += 1; }
			}
		}
		int ans = 0;
		int ngood = 0;
		forn(i, 16) {
			if (count[i] == 2) {
				++ngood;
				ans = i + 1;
			}
		}
		cout << "Case #" << (k+1) << ": " ;
		if (ngood > 1) {
			cout << "Bad magician!" << endl;
		} else if (ngood == 0) {
			cout << "Volunteer cheated!" << endl;
		} else {
			cout << ans << endl;
		}
	}
	return 0;
}
