#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<algorithm>

using namespace std;

int optimalDeceitfulWar(float *sortedNaomi, float *sortedKen, int size) {
	int win = 0;
	int naomiMinIndex = 0;
	int naomiMaxIndex = size - 1;
	int kenMinIndex = 0;
	int kenMaxIndex = size - 1;
	for (int i = 0; i < size; i++) {
		if (sortedNaomi[naomiMinIndex] < sortedKen[kenMinIndex]) {
			++naomiMinIndex;
			--kenMaxIndex;
		}
		else if (sortedNaomi[naomiMinIndex] > sortedKen[kenMinIndex]) {
			++kenMinIndex;
			++naomiMinIndex;
			win++;
		}
	}
	return win;
}

int optimalWar(float *sortedNaomi, float *sortedKen, int size) {
	int win = 0;
	int kenMinIndex = 0;
	int kenMaxIndex = size - 1;

	for (int i = size - 1; i >= 0; i--) {
		if (sortedNaomi[i] > sortedKen[kenMaxIndex]) {
			++kenMinIndex;
			++win;
		}
		else {
			--kenMaxIndex;
		}
	}
	return win;
}

int main() {
	int n;
	float naomi[1005];
	float ken[1005];

	int testcaseSize = 0;
	cin >> testcaseSize;
	for (int tc = 1; tc <= testcaseSize; tc++) {
		cin >> n;

		for (int i = 0; i < n; ++i){
			cin >> naomi[i];
		}

		for (int i = 0; i < n; ++i) {
			cin >> ken[i];
		}

		sort(naomi, naomi + n);
		sort(ken, ken + n);

		/*for (int i = 0; i < n; i++) {
			cout << naomi[i] << " ";
			}
			cout << endl;
			for (int i = 0; i < n; i++) {
			cout << ken[i] << " ";
			}
			cout << endl;*/


		int ans1 = optimalDeceitfulWar(naomi, ken, n);
		int ans2 = optimalWar(naomi, ken, n);
		cout << "Case #" << tc << ": " << ans1 << " " << ans2 << endl;
	}
	return 0;
}