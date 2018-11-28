#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

bool greaterpair(const pair<char, int>& a, const pair<char, int>& b) {
	if (a.second > b.second)
		return true;
	else
		return false;
}

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		cout << "Case #" << i + 1 << ":";

		int N;
		cin >> N;
		vector<pair<char, int> > v;
		for (int j = 0; j < N; ++j) {
			int party;
			cin >> party;
			v.push_back(make_pair('A'+j, party));
		}
		sort(v.begin(), v.end(), greaterpair);
		
		/*
		for (const auto& p : v) {
			cout << " ";
			cout << p.first << "/" << p.second;
		}
		*/

		int rem = N;
		while(v[0].second > 0) {
			if (rem % 2 != 0) { // odd, evacuate one
				cout << " " << v[0].first;
				v[0].second -= 1;
				if (v[0].second == 0)
					rem -= 1;
			} else {
				cout << " " << v[0].first << v[1].first;
				v[0].second -= 1;
				v[1].second -= 1;
				if (v[0].second == 0)
					rem -= 1;
				if (v[1].second == 0)
					rem -= 1;
			}
			sort(v.begin(), v.end(), greaterpair);

		}

		cout << endl;
	}

	return 0;
}
