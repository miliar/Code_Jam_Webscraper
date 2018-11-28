#include <bits/stdc++.h>
using namespace std;

#define vi vector<int>

int main() {
	int t, c = 0;
	string s;
	cin >> t;
	while (t--) {
		cout << "Case #" << ++c << ": ";
		cin >> s;
		vi q;
		q.push_back(s[0]);
		for (int i = 0; i < s.size(); i++) {
			if (q.back() == s[i]) 
				continue;
			q.push_back(s[i]);
		}
		if (q.back() == '+')
			q.pop_back();
		cout << q.size() << endl;
	}
	return 0;
}
