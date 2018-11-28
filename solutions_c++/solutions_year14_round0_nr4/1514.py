#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	vector <double> naomi;
	vector <double>	ken;

	int T; cin >> T;
	for (int t = 0; t < T; ++t) {
		naomi.clear();
		ken.clear();
		int N; cin >> N;
		for (int i = 0; i < N; ++i) {
			double tmp; cin >> tmp; naomi.push_back(tmp);
		}
		for (int i = 0; i < N; ++i) {
			double tmp; cin >> tmp; ken.push_back(tmp);
		}
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		int ret1 = 0; int deduct = 0;
		for (int i = 0; i < N; ++i) {
			if (naomi[i] < ken[i-deduct]) {
				deduct++;
			}
			else {
				ret1++;
			}
		}
		int ret2 = 0; int ptr = N - 1;
		for (int i = N-1; i >= 0; --i) {
			if (naomi[i] < ken[ptr]) {
				ptr--;
			}
			else {
				ret2++;
			}
		}

		cout << "Case #" << t + 1 << ": " << ret1 << " " << ret2 << endl;
		
	}
}