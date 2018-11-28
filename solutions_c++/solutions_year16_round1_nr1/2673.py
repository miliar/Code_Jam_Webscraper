#include <bits/stdc++.h>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		string S;
		cin >> S;
		deque<char> q;
		for (char c : S) {
			if (q.empty() || c >= q.front()) q.push_front(c);
			else q.push_back(c);
		}
		cout << "Case #" << (t+1) << ": ";
		while (!q.empty()) {
			cout << q.front();
			q.pop_front();
		}
		cout << endl;
	}
}