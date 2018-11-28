#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <algorithm>
#include <utility>
#include <string>
#include <bitset>
#include <cstdint>
#include <cstdio>

using ii = int64_t;
using ui = uint64_t;
#define all(v) v.begin(), v.end()

using namespace std;

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int cases; cin >> cases;
	for (ui cas = 1; cas <= cases; ++cas) {
		cout << "Case #" << cas << ": ";
		ii n, r, p, s; cin >> n >> r >> p >> s;
		string top = "a", bot = "";
		for (ii i = 0; i < n; ++i) {
			for (char c : top) {
				if (c == 'a') bot.append("ab");
				else if (c == 'b') bot.append("bc");
				else bot.append("ca");
			}
			top = move(bot);
			bot.clear();
		}
		ii aa = 0, bb = 0, cc = 0;
		for (char c : top) {
			if (c == 'a') aa++;
			else if (c == 'b') bb++;
			else cc++;
		}
		if (aa == r && bb == s && cc == p) { replace(all(top), 'a', 'R'); replace(all(top), 'b', 'S'); replace(all(top), 'c', 'P'); }
		else if (aa == p && bb == r && cc == s) { replace(all(top), 'a', 'P'); replace(all(top), 'b', 'R'); replace(all(top), 'c', 'S'); }
		else if (aa == s && bb == p && cc == r) { replace(all(top), 'a', 'S'); replace(all(top), 'b', 'P'); replace(all(top), 'c', 'R'); }
		else {
			cout << "IMPOSSIBLE\n";
			continue;
		}
		for (ii i = 0; i < n; ++i) {
			ii bs = 1 << i;
			for (ii j = 0; j < top.length(); j += 2 * bs) {
				string ll(top.begin() + j, top.begin() + j + bs);
				string rr(top.begin() + j + bs, top.begin() + j + 2 * bs);
				if (ll > rr) {
					for (ii k = j; k < j + bs; ++k) top[k] = rr[k - j];
					for (ii k = j + bs; k < j + 2 * bs; ++k) top[k] = ll[k - j - bs];
				}
			}
		}
		cout << top << '\n';
	}
}