#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

#define HEIGHT_TOTAL 2500

using namespace std;

int main() {

	vector<vector<int> > allItems;

	int T;
	scanf("%d\n", &T);
	for (int i = 0; i < T; ++i) {
		int N;
		scanf("%d\n", &N);

		int heights[HEIGHT_TOTAL + 1];
		for (int j = 0; j < (HEIGHT_TOTAL + 1); ++j) {
			heights[j] = 0;
		}

		int total = 2*N - 1;
		for (int j = 0; j < total; ++j) {
			vector<int> mini;
			for (int k = 0; k < N; ++k) {
				int num;
				scanf("%d ", &num);
				mini.push_back(num);

				heights[num]++;
				heights[num] %= 2;
			}
			allItems.push_back(mini);
		}

		vector<int> interestItems;
		for (int j = 0; j < HEIGHT_TOTAL; ++j) {
			if (heights[j] == 1) {
				interestItems.push_back(j);
			}
		}

		sort(interestItems.begin(), interestItems.end());

		cout << "Case #" << (i + 1) << ": ";
		for (int j = 0; j < N; ++j) {
			cout << interestItems[j] << " ";
		}
		cout << endl;
	}

	return 0;
}
