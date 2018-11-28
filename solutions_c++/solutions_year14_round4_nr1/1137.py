#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector>
using namespace std;

int main() {
	int N, X, T, discs[10000];
	bool done[10000];
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		cin >> N >> X;
		for (int n = 0; n < N; n++) cin >> discs[n];
		memset(done, 0, sizeof done);
		sort(discs, discs+N);
		int count = 0;
		for (int n = 0; n < N; n++) {
			if (done[n]) continue;
			done[n] = true;
			int left = X - discs[n];
			int pos = n;
			while(pos < N && (done[pos] || discs[pos] <= left)) pos++;
			pos--;
			while (done[pos] && pos > 0) pos--;
			if (!done[pos] && pos != N) {
				done[pos] = true;
			}
			count++;
		}
		cout << "Case #" << tc << ": " << count << endl;
	}
}
