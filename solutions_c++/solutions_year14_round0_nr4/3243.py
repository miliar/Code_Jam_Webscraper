#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int T, N;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		cin >> N;
		vector<int> naomi, ken;
		double d;
		for (int j = 0; j < N; j++) {
			cin >> d;
			naomi.push_back(d * 100000);
		}
		for (int j = 0; j < N; j++) {
			cin >> d;
			ken.push_back(d * 100000);
		}
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());

		int s1 = 0, s2 = 0;
		int is1 = 0, is2 = 0, ie1 = N - 1, ie2 = N - 1;
		while (is1 <= ie1) {
			// cout << "naomi[is1]" << naomi[is1] << "  ken[is2]" << ken[is2] << endl;
			if (naomi[is1] > ken[is2]) {
				s1++;
				is1++;
				is2++;
			} else {
				is1++;
				ie2--;
			}
		}
		is1 = is2 = 0;
		while (is2 < N) {
			// cout << "naomi[is1]" << naomi[is1] << "  ken[is2]" << ken[is2] << endl;
			while (is2 < N && naomi[is1] > ken[is2]) {
				is2++;
			}
			if (is2 != N) {
				is1++;
				is2++;
				s2++;
			}
		}

		cout << "Case #" << i << ": " << s1 << ' ' << (N - s2) << '\n';
	}

	return 0;
}