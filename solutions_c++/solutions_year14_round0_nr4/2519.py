#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int dominated(vector<double> &v1, vector<double> &v2) {
	int curr_pot = 0;
	int total = 0;

	for (int i = 0; i < v1.size(); ++i) {
		while (v1[i] < v2[curr_pot] && curr_pot < v2.size()) ++curr_pot;
		if (curr_pot == v2.size()) break;
		++total;
		++curr_pot;
	}
	
	return total;
}

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		int n;
		cin >> n;
		vector<double> naomi;
		vector<double> ken;
		double x;
		for (int j = 0; j < n; ++j) {
			cin >> x; naomi.push_back(x);
		}
		for (int j = 0; j < n; ++j) {
			cin >> x; ken.push_back(x);
		}

		sort(naomi.rbegin(), naomi.rend());
		sort(ken.rbegin(), ken.rend());

		printf("Case #%d: %d %d\n", i, dominated(naomi, ken), n - dominated(ken, naomi));
	}

	return 0;
}

