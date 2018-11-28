/*/**/

#include <bits/stdc++.h>

using namespace std;

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for(int tt = 1; tt <= t; tt++) {
		int n;
		cin >> n;
		priority_queue < pair < int, int > > pq;
		for(int i = 0; i < n; i++) {
			int x;
			cin >> x;
			pq.push(make_pair(x, i));
		}
		vector < string > foo;
		cout << "Case #" << tt << ":";
		while(pq.size()) {
			pair < int, int > u = pq.top(); pq.pop();
			string s = "";
			if(u.first != 1)
			cout << ' ' << char(u.second + 'A');
			else s += char(u.second + 'A');
			if(pq.size()) {
				pair < int, int > v = pq.top(); pq.pop();
				if(v.first == u.first) {
					if(u.first != 1)
					cout << char(v.second + 'A');
					else s+= char(v.second + 'A');
					if(v.first > 1) {
						pq.push(make_pair(v.first - 1, v.second));
					}
				}
				else {
					pq.push(v);
				}
			}
			if(u.first > 1) {
				pq.push(make_pair(u.first - 1, u.second));
			}
			else {
				foo.push_back(s);
			}
		}
		for(int i = foo.size() - 1; i >= 0; i--) {
			cout << ' ' << foo[i];
		}
		cout << endl;
	}
	return 0;
}
