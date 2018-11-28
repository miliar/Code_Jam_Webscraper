#include <iostream>
#include <algorithm>
using namespace std;

double naomi[1000];
double ken[1000];

int maxwon(int N, double* good, double* bad) {
	int pos = 0;
	int ans = 0;
	for (int i = 0; i < N; i++) {
		if (good[i] > bad[pos]) {
			ans++;
			pos++;
		}
	}
	return ans;
}

int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		int N;
		cin >> N;
		for (int i = 0; i < N; i++)
			cin >> naomi[i];
		for (int i = 0; i < N; i++)
			cin >> ken[i];
		sort(naomi, naomi+N);
		sort(ken, ken+N);
		cout << "Case #" << t << ": " << maxwon(N, naomi, ken) << ' ' << N-maxwon(N, ken, naomi) << '\n';
	}

	return 0;
}
