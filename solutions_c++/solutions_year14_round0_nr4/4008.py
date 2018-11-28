#include	<iostream>
#include	<ostream>
#include	<vector>
#include	<algorithm>
using namespace std;

int main(void) {
	int T; cin >> T;

	for (int t = 1; t <= T; ++t) {
		int N;
		cin >> N;

		vector<double>	naomi(N), ken(N);
		for (int i = 0; i < N; ++i)
			cin >> naomi[i];
		for (int i = 0; i < N; ++i)
			cin >> ken[i];

		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());

		int		war_points = 0;
		auto	k_rit = ken.rbegin();
		for (auto rit = naomi.rbegin(); rit != naomi.rend(); ++rit) {
			if (*rit > *k_rit) {
				++war_points;
			} else {
				++k_rit;
			}
		}

		int		deceitful_war_points = 0;
		auto	k_it = ken.begin();
		for (auto it = naomi.begin(); it != naomi.end(); ++it) {
			if (*it > *k_it) {
				++deceitful_war_points;
				++k_it;
			}
		}

		cout << "Case #" << t << ": " << deceitful_war_points << " " << war_points << endl;
	}

	return 0;
}