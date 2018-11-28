#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
#include "iostream"

using namespace std;

void solve() {
	set<int> ans;
	for (int i = 1; i <= 16; ++i) ans.insert(i);

	int l, a;
	for (int t = 0; t < 2; ++t) {
		cin >> l;
		--l;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				cin >> a;
				if (i != l) ans.erase(a);
			}
		}
	}

	if (ans.size() == 1) {
		cout << *ans.begin();
	}
	else if (ans.size() == 0) {
		cout << "Volunteer cheated!";
	}
	else
	{
		cout << "Bad magician!";
	}
}

int main() {

	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);

	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";
		solve();
		cout << endl;
	}
	
	return 0;
}
