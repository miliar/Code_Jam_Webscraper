#include <iostream>
#include <string>
#include <deque>

using namespace std;

string solve(const string &s) {
	deque<char> q;

	for (auto c : s) {
		if (q.empty() || q.front() <= c)
			q.push_front(c);
		else
			q.push_back(c);
	}

	string ans(q.begin(), q.end());
	return ans;
}

int main(void) {
	cout.sync_with_stdio(false);

	int nTests;
	cin >> nTests;
	for (int t = 1; t <= nTests; ++t) {
		string seq;
		cin >> seq;
		cout << "Case #" << t << ": " << solve(seq) << endl;
	}
	return 0;
}
