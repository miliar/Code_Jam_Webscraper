#include <iostream> 
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <stack>
#include <functional>
#include <cstring>
#include <algorithm>
#include <map>
#include <cmath>
#include <ctime>
#include <unordered_map>

using namespace std;

string hand = "PRS";

string getstr(int n, int i) {
	if (!n) return string(1, hand[i]);

	string s = getstr(n - 1, i);
	string t = getstr(n - 1, (i + 1) % 3);

	if (s < t) return s + t;
	return t + s;
}

bool valid(string &str, int p, int r, int s) {
	for (auto & c : str) {
		if (c == 'P') --p;
		if (c == 'R') --r;
		if (c == 'S') --s;
	}
	return !p && !r && !s;
}

string solve() {
	int n, r, p, s;
	cin >> n >> r >> p >> s;

	string ans = "z";
	for (int i = 0; i < 3; ++i) {
		string cand = getstr(n, i);
		if (valid(cand, p, r, s)) ans = min(ans, cand);
	}
	if (ans == "z") ans = "IMPOSSIBLE";
	return ans;
}

int main(){
	cin.tie(0);
	ios::sync_with_stdio(false);

	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: ", i);
		cout << solve() << endl;
	}

}