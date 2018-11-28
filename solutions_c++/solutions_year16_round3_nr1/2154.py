#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include <utility>
using namespace std;

typedef long long LL;
const LL INF = 0x3f3f3f3f3f3f3f3fLL;

struct Party {
	char name;
	int num;
	Party(int n, int order) {
		num = n;
		name = 'A' + order;
	}
	bool operator<(const Party& val) const {
		return num > val.num;
	}
};
//const int maxn = 30;
//
//int n;
//string s0, t0;
//string s, t;
//
//LL ans; 
//string res[2];
int N;

void calc0(int p) {
}

void calc(int p) {
}

void solve() {

	vector<Party> parties;
	cin >> N;
	for (int i = 0; i < N; ++i) {
		int k;
		cin >> k;
		Party p(k, i);
		parties.push_back(p);
	}
	std::sort(parties.begin(), parties.end());
	int order = 0;
	while (true) {
		if (parties.size() == 0) break;
		if (parties[0].num < parties[1].num) {
			std::sort(parties.begin(), parties.end());
		}
		else if (parties[0].num > parties[1].num) {
			cout << parties[0].name;
			parties[0].num = parties[0].num - 1;
			if (parties[0].num == 0) {
				parties.erase(parties.begin());
				cout << " ";
				continue;
			}
			if (parties[0].num == 1 && parties.size() == 2) {
				cout << " ";
				continue;
			}
			cout << parties[0].name;
			parties[0].num = parties[0].num - 1;
			if (parties[0].num == 0) {
				parties.erase(parties.begin());
				cout << " ";
				continue;
			}
		} else if (parties[0].num == parties[1].num) {

			if (parties[0].num == 1 && parties.size() % 2 == 1) {
				cout << parties[0].name;
				parties.erase(parties.begin());
				cout << " ";
				continue;
			}

			cout << parties[0].name;
			parties[0].num = parties[0].num - 1;
			if (parties[0].num == 0) {
				parties.erase(parties.begin());
				cout << parties[0].name;
				parties[0].num = parties[0].num - 1;
				if (parties[0].num == 0) {
					parties.erase(parties.begin());
				}
			}
			else {
				cout << parties[1].name;
				parties[1].num = parties[1].num - 1;
				if (parties[1].num == 0) {
					parties.erase(parties.begin());
				}
			}

			std::sort(parties.begin(), parties.end());
		}
		

		cout << " ";
	}
	//cin >> s0 >> t0;
	//cout << res[0] << ' ' << res[1] << endl;
}

int main() {
	int t; 
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
	return 0;
}
