#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <vector>

using namespace std;

int a[1000], n, k, t, j, c;
vector <int> ans[1000];

void gen(int k, int n, int p1, int p2) {
	if (c == j)
		return;
	if (k == n) {
		if (p1 == p2) {
			c++;
			for (int i = 1; i <= n; i++)
				ans[c].push_back(a[i]);

		}
	}
	else {
		a[k] = 0;
		gen(k + 1, n, p1, p2);
		a[k] = 1;
		if (k % 2 == 1)
			gen(k + 1, n, p1 + 1, p2);
		else
			gen(k + 1, n, p1, p2 + 1);
	}
}

int main() {
	ifstream cin("in.txt");
	ofstream cout("out.txt");
	cin >> t;
	cin >> n >> j;
	a[1] = 1;
	a[n] = 1;
	gen(2, n, 0, 0);
	cout << "Case #1:" << endl;
	for (int i = 1; i <= c; i++) {
		for (int j = 0; j < ans[i].size(); j++)
			cout << ans[i][j];
		cout << " 3 4 5 6 7 8 9 10 11" << endl;
	}
	return 0;
}