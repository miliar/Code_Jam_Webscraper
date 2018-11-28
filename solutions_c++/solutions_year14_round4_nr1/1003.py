#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int main() {
	int kases;
	cin >> kases;
	for (int kase = 1; kase <= kases; kase++) {
		cout << "Case #" << kase << ": ";

		int N, X;
		cin >> N >> X;
		vector<int> fs(N);
		for (int i = 0; i < N; i++)
			cin >> fs[i];

		sort(fs.begin(), fs.end());
		int j = N-1;
		int doubles = 0;
		for (int i = 0; i < N && i < j; i++) {
			for (; j > i; j--) {
				if (fs[i] + fs[j] <= X) {
					doubles++;
					j--;
					break;
				}
			}
		}

		cout << N - doubles << endl;
	}
	return 0;
}
