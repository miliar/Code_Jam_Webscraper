#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <functional>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <limits>
#include <sstream>
#include <typeinfo>

using namespace std;

string solve(const vector<int>& P)
{
	int N = (int)P.size();
	int total = 0;
	priority_queue<pair<int, int>> PQ;
	for (int i = 0; i < N; i++) {
		total += P[i];
		PQ.push(make_pair(P[i], i));
	}
	string ans;
	if (total % 2 == 1) {
		int i;
		int n;
		tie(n, i) = PQ.top();
		PQ.pop();
		n--;
		if (n > 0)
			PQ.push(make_pair(n, i));
		total--;
		ans += ('A' + i);
	}
	while (total > 0) {
		int i;
		int n;
		tie(n, i) = PQ.top();
		PQ.pop();
		n--;
		if (n > 0)
			PQ.push(make_pair(n, i));
		total--;
		int j;
		tie(n, j) = PQ.top();
		PQ.pop();
		n--;
		if (n > 0)
			PQ.push(make_pair(n, j));
		total--;
		if (!ans.empty())
			ans += " ";
		ans += ('A' + i);
		ans += ('A' + j);
	}
	return ans;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int N;
		cin >> N;
		vector<int> P(N);
		for (int i = 0; i < N; i++) {
			cin >> P[i];
		}
		auto ans = solve(P);
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}
