#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <unordered_map>
#include <unordered_set>

using namespace std;

string s;

map <pair <int, int>, int> cache;
int dummy_helper(int b, int e) {
	if (b >= e)
		return 0;
	auto it = cache.find(make_pair(b, e));
	if (it != cache.end())
		return it->second;
	int ans = 0;
	for (int i = b; i <= e; i++)
		if (s[i] == s[e - i + b])
			ans += 10;
		else
			ans += 5;
	ans /= 2;
	int add = 5;
	if (s[b] == s[e])
		add = 10;
	ans = max(ans, dummy_helper(b + 1, e - 1) + add);
	for (int i = b + 2; i < e; i += 2)
		ans = max(ans, dummy_helper(b, i - 1) + dummy_helper(i, e));
	return cache[make_pair(b, e)] = ans;
}

int dummy() {
	cache.clear();
	return dummy_helper(0, s.length() - 1);
}

int greedy() {
	stack <char> st;
	int n = s.length();
	int ans = 0;
	for (int i = 0; i < n; i++) {
		if (st.empty()) {
			st.push(s[i]);
			continue;
		}
		if (st.top() == s[i] || st.size() == n - i) {
			if (st.top() == s[i])
				ans += 10;
			else
				ans += 5;
			st.pop();
			continue;
		}
		st.push(s[i]);
	}
	return ans;
}

void solve(int t) {
	cin >> s;
	//int ans = dummy();
	int nans = greedy();
	//if (ans != nans)
	printf("Case #%d: %d\n", t, nans);
}

int main() {
	freopen("A-large.in", "r", stdin);
	//freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;
	cin >> tc;
	for (int t = 1; t <= tc; t++)
		solve(t);
}