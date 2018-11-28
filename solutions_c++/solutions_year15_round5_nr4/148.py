#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

int t;
int p;
int e[11111];
int f[11111];

void solve(int x) {
	cin >> p;
	for (int i = 0; i < p; i++) cin >> e[i];
	for (int i = 0; i < p; i++) cin >> f[i];
	f[0]--;
	vector<int> v;
	vector<int> q;
	unordered_map<int,int> z;
	for (int i = 0; i < p; i++) {
		z[e[i]] = i;
	}
	int a = 0;
	while (true) {
		bool ok = false;
		for (int i = a; i < p; i++) {
			if (f[i]) {
				a = i;
				ok = true;
				f[i]--;
				vector<int> u;
				for (int j = 0; j < v.size(); j++) {
					f[z[v[j]+e[i]]]--;
					u.push_back(v[j]+e[i]);
				}
				for (int j = 0; j < u.size(); j++) {
					v.push_back(u[j]);
				}
				v.push_back(e[i]);
				q.push_back(e[i]);
				break;
			}
		}
		if (!ok) break;
	}
	sort(v.begin(), v.end());
	cout << "Case #" << x << ":";
	for (int i = 0; i < q.size(); i++) {
		cout << " " << q[i];
	}
	cout << "\n";
}

int main() {
	cin >> t;
	for (int i = 1; i <= t; i++) solve(i);
}
