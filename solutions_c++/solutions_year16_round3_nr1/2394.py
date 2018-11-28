#include <bits/stdc++.h>

using namespace std;

int main() {
	int n;
	cin >> n;
	for(int t =  1; t <= n; t++) {
		int p;
		cin >> p;
		vector<pair<int, char>> vs(p);
		for (int i = 0; i < p; i++) {
			cin >> vs[i].first;
			vs[i].second = 'A' + i;
		}
		sort(vs.begin(), vs.end(), std::greater<std::pair<int, char>>());
		cout << "Case #" << t << ":";
		while (vs[0].first > vs[1].first) {
			cout << " " << vs[0].second;
			vs[0].first --;
		}
		for (int i = 2; i < p; i++) {
			for (int j = 0; j < vs[i].first; j++) {
				cout << " " << vs[i].second;
			}
		}
		for (int i = 0; i < vs[0].first; i++) {
			cout << " " << vs[0].second << vs[1].second;
		}
		cout << endl;
	}
}
