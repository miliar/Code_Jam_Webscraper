#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <string>
#include <tuple>
#include <queue>
#include <utility>
#include <stack>
#include <set>
#include <map>
#include <deque>
#include <limits>
#include <new>
#include <functional>
#include <unordered_map>
#include <unordered_set>

using namespace std;



int main(void) {
	cin.tie(nullptr);
	cin.sync_with_stdio(false);

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		string p;
		cin >> p;
		int res = 0;
		char prev = '+';
		for (int j = p.size() - 1; j >= 0; j--) {
			if (prev != p[j]) res++;
			prev = p[j];
		}
		cout << "Case #" << i << ": " << res << '\n';
	}

	return 0;
}