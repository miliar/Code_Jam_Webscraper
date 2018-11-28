#include <bits/stdc++.h>
#define vi vector<int>
#define pi pair<int,int>
#define vii vector<pi>
#define ll long long
using namespace std;
int main() {
#ifndef ONLINE_JUDGE
	freopen("/home/shiva/Learning/1.txt", "r", stdin);
	freopen("/home/shiva/Learning/2.txt", "w", stdout);
#endif
	ios::sync_with_stdio(false); cin.tie(0);
	int t; string s;
	cin >> t;
	for (int x = 1; x <= t; x++) {
		deque<char> dq;
		cin >> s;
		int len = int(s.size());
		dq.push_back(s[0]);
		for (int i = 1; i < len; i++) {
			if (dq.front() <= s[i]) dq.push_front(s[i]);
			else dq.push_back(s[i]);
		}
		cout << "Case #" << x << ": ";
		while (!dq.empty()) {
			cout << dq.front();
			dq.pop_front();
		}
		cout << '\n';
	}

}