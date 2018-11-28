#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

int main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int T;
	cin >> T;

	for(int test = 1; test <= T; ++test) {
		long long r, t;
		cin >> r >> t;

		int ans = 0;
		long long sum = 0;
		for(int i = 0;; ++i) {
			sum += (r + 1) * (r + 1) - r * r;
			if(sum > t) {
				ans = i;
				break;
			}

			r += 2;
		}

		cout << "Case #" << test << ": " << ans << endl;
	}

	return EXIT_SUCCESS;
}
