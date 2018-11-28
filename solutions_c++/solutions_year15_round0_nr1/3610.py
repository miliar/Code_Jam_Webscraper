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
		int sMax;
		cin >> sMax;
		sMax++;
		string s;
		cin >> s;

		int curUp = 0;
		int ans = 0;
		for (int i = 0; i < sMax; ++i) {
			if (i > curUp) {
				ans += (i - curUp);
				curUp += (i - curUp);
			}
			curUp += s[i] - '0';
		}

		printf("Case #%d: %d\n", q+1, ans);
	}
}

int main() {
	#ifdef _WIN32
		FILE *stream_in, *stream_out;
		freopen_s(&stream_in, "A-small-attempt0.in", "r", stdin);
		freopen_s(&stream_out, "output.txt", "w", stdout);
	#else
		freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	#endif

    solve();
    return 0;
}
