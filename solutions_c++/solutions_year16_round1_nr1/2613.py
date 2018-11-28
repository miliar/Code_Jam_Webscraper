#include <bits/stdc++.h>

using namespace std;

void solve(string s) {
	char first = 'A';

	deque<char> out;

	for(int i = 0; i < s.length(); i++) {
		if(s[i] >= first) {
			out.push_front(s[i]);
			first = s[i];
		}
		else {
			out.push_back(s[i]);
		}
	}

	for(int i = 0; i < s.length(); i++)
	{
		cout << out[i];
	}

	cout << endl;
}

int main() {
	int t;
	cin >> t;

	for(int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";

		string s;
		cin >> s;

		solve(s);
	}

	return 0;
}
