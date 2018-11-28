#include <iostream>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int casenum = 1; casenum <= T; ++casenum) {
		int N;
		cin >> N;
		int samples[N];
		int maxdiff = 0;
		int mineats = 0;
		for (int i = 0; i < N; ++i) {
			cin >> samples[i];
			if (i > 0) {
				int diff = samples[i-1] - samples[i];
				if (diff > maxdiff) maxdiff = diff;
				if (diff > 0) mineats += diff;
			}
		}
		int mineatc = 0;
		for (int i = 0; i < N-1; ++i) {
			int eat = maxdiff < samples[i] ? maxdiff : samples[i];
			mineatc += eat;
		}
		cout << "Case #" << casenum << ": " << mineats << ' ' << mineatc << endl;
	}
	return 0;
}

