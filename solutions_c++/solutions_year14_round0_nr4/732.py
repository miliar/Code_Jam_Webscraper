#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int war_score(vector<double> naomi, vector<double> ken) {
	int result = 0;

	for (double x: naomi) {
		auto iter = upper_bound(ken.begin(), ken.end(), x);
		if (iter == ken.end()) {
			ken.erase(ken.begin());
			result++;
		} else {
			ken.erase(iter);
		}
	}

	return result;
}

int deceitful_war_score(vector<double> naomi, vector<double> ken) {
	int result = 0;	

	while (naomi.size()) {
		if (naomi.back() < ken.back()) {
			naomi.erase(naomi.begin());
			ken.pop_back();
		} else {
			naomi.pop_back();
			ken.pop_back();
			result++;
		}
	}

	return result;
}

int main() {
	int t;
	cin >> t;

	for (int test = 1; test <= t; test++) {
		int n;
		cin >> n;

		vector<double> naomi, ken;

		for (int i = 0; i < n; i++) {
			double t;
			cin >> t;
			naomi.push_back(t);
		}

		for (int i = 0; i < n; i++) {
			double t;
			cin >> t;
			ken.push_back(t);
		}

		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());

		cout << "Case #" << test << ": " << deceitful_war_score(naomi, ken) << " " << war_score(naomi, ken) << endl;
	}
}