#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef unsigned long long ull;

ull steps(ull n, ull l)
{
	if (n <= l) return 0;
	ull k = n / l;
	ull r = n % l;
	return r == 0 ? (k - 1) : k;
}

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int N;
		cin >> N;
		vector<int> bin(N, 0);
		int mx = 0;
		for (int i = 0; i < N; i++) {
			cin >> bin[i];
			if (mx < bin[i])
				mx = bin[i];
		}

		ull best_score = numeric_limits<ull>::max();
		for (int l = 1; l <= mx; l++) {
			ull score = 0;
			for (int i = 0; i < N; i++)
				score += steps(bin[i], l);
			//cout << l << " " << score << endl;
			if (l + score < best_score) {
				best_score = l + score;
			}
		}
		if (mx == 0) best_score = 0;
		cout << "Case #" << t << ": " << best_score << endl;
	}
}