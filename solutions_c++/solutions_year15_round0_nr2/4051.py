#include <bits/stdc++.h>

using namespace std;

map<multiset<int>, int> memo;

int find_ans(multiset<int> v) {
	auto memo_it = memo.find(v);
	if (memo_it != memo.end()) {
		return memo_it->second;
	}

	auto it = v.end(); it--;

	int ans = *it;

	for (auto i: v) {
		for (int a = 1; a <= i / 2; a++) {
			multiset<int> vt = v;
			vt.erase(vt.find(i));
			vt.insert(a);
			vt.insert(i - a);
			ans = min(ans, find_ans(vt) + 1);
		}
	}

	return memo[v] = ans;
}

int main() {
	int t;
	cin >> t;
	//t = 1;

	for (int test = 1; test <= t; test++) {
		int n;
		cin >> n;

		multiset<int> s;
		for (int i = 0; i < n; i++) {
			int cur;
			cin >> cur;
			s.insert(cur);
		}

		int ans = find_ans(s);

		/*priority_queue<int> q;
		for (int i = 0; i < n; i++) {
			int cur;
			cin >> cur;
			q.push(cur);
		}

		int ans = q.top();

		int moves = 0;
		
		while (q.top() >= 2) {
			int a = q.top() / 2;
			int b = q.top() - a;

			q.pop();
			q.push(a);
			q.push(b);
			moves++;

			ans = min(ans, moves + q.top());
		}*/

		printf("Case #%d: %d\n", test, ans);
	}
}

//3
//1 9 3

//1 5 4 3     1 6 3 3
//1 3 2 4 3   1 3 3 3 3