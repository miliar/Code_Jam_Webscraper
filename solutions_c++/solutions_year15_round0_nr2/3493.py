#include <stdio.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <unordered_map>
#include <sstream>
#include <set>
#include <unordered_set>
#include <algorithm>
#include <tuple>
#include <queue>

using namespace std;

void solve() {
	int t;
	cin >> t;
	for (int q = 0; q < t; ++q) {
		int d;
		cin >> d;
		map<int, int> a;
		for (int i = 0; i < d; ++i) {
			int cur;
			cin >> cur;
			a[cur]++;
		}

		int ans = a.rbegin()->first;

		for (int min_a = 1; min_a < a.rbegin()->first; ++min_a) {
			int tmpans = min_a;
			for (auto i = a.begin(); i != a.end(); ++i)
				if (i->first > min_a)
					tmpans += i->second * ((i->first + min_a - 1) / min_a - 1);
			ans = min(tmpans, ans);
		}

		printf("Case #%d: %d\n", q+1, ans);
	}
}

int main() {
	#ifdef _WIN32
		FILE *stream_in, *stream_out;
		freopen_s(&stream_in, "A-small-attempt0.in", "r", stdin);
		//freopen_s(&stream_in, "input.txt", "r", stdin);
		freopen_s(&stream_out, "output.txt", "w", stdout);
	#else
		freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	#endif

    solve();
    return 0;
}
