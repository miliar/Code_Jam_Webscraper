#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <numeric>
#include <utility>
#include <functional>
#include <algorithm>
#include <bitset>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

int main(int argc, char *argv[])
{
	int T;

	cin >> T;
	for (int ti = 1; ti <= T; ti++) {
		int n;
		cin >> n;
		vector<int> a, b;
		for (int i = 0; i < n; i++) {
			int t;
			cin >> t;
			a.push_back(t);
			b.push_back(t);
		}

		sort(b.begin(), b.end());

		int ans = 0;

		for (int k = 0; k < n; k++) {
			int t = b[k];
			for (int i = 0; i < a.size(); i++)
				if (a[i] == t) {
					ans += min(i, (int) a.size() - 1 - i);
					a.erase(a.begin() + i);
					break;
				}
		}

		printf("Case #%d: %d\n", ti, ans);
	}

	return 0;
}
