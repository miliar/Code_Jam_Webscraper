#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
using namespace std;

int main() {
	int n;
	cin >> n;
	vector<int> a(n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &a[i]);
	}
	map<int, int> current;
	vector<int> ans;
	int prev = 0;
	for (int i = 0; i < n; i++) {
		if (current.find(a[i]) != current.end()) {
			ans.push_back(prev + 1);
			ans.push_back(i + 1);
			prev = i + 1;
			current.clear();
		} else {
			current[a[i]] = i;
		}
	}
	if (ans.empty()) {
		cout << -1 << endl;
	} else {
		if (ans.back() != n) {
			ans[ans.size() - 1] = n;
		}
		cout << ans.size() / 2 <<endl;
		for (int i = 0; i < ans.size(); i += 2) {
			cout << ans[i] << ' ' << ans[i + 1] << endl;
		}
	}
	return 0;
}