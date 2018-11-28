#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	cout.precision(10);

	int T; cin >> T;
    for (int t = 1; t <= T; ++t) {
		int N; cin >> N;
		vector<double> naomi(N,0);
		for (int i = 0; i < N; ++i) {
			cin >> naomi[i];
		}
		vector<double> ken(N,0);
		for (int i = 0; i < N; ++i) {
			cin >> ken[i];
		}

		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());

		// Kens' WAR strategy:
		// - If he has heavier use the least heavier.
		// - If he does NOT have a heavier use lightest.

		int war = N;
		for (int ni = 0, ki = 0; ni < N && ki < N; ++ki, ++ni) {
			for (;ki < N && ken[ki] < naomi[ni]; ++ki);
			if (ki < N)	--war;
		}

		int deceitful = 0;
		for (int ni = 0, ki = 0; ni < N && ki < N; ++ki, ++ni) {
			for (; ni < N && ken[ki] > naomi[ni]; ++ni);
			if (ni < N) ++deceitful;
		}
		
		cout << "Case #" << t << ": " << deceitful << " " << war << endl;
	}

	return 0;
}