#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>

using namespace std;

int Case = 1, tc = 0;
long long n = 0;

bool vis[10] = { false };

bool check() {
	for (int i = 0; i <= 9; i++) {
		if (!vis[i]) {
			return false;
		}
	}
	return true;
}
int main() {
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "w", stdout);
	cin >> tc;

	while (tc--) {
		memset(vis, false, sizeof(vis));
		cin >> n;

		if (n == 0) {
			cout << "Case #" << Case++ << ": " << "INSOMNIA" << endl;
			continue;
		}
		long long i = 1, last = 0;

		while (true) {

			long long num = last = n * i;

			while (num) {
				int x = num % 10;

				if (!vis[x]) {
					vis[x] = true;
				}
				num /= 10;
			}

			if (check()) {
				break;
			}
			i++;

		}

		cout << "Case #" << Case++ << ": " << last  << endl;
	}

	return 0;
}
//By : mohamed waleed
