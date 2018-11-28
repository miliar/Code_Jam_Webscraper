#include <iostream>
#include <algorithm>
using namespace std;

int getOptimalWarScore(double *first, double *second, int n) {
	int score = 0;

	for (int i = 0, j = 0; i < n && j < n; i++, j++) {
		while (j < n && second[j] < first[i]) j++;
		
		if (j < n) score++;
	}

	return score;
}

int main(void) {
	int numCases;
	
	cin >> numCases;
	for (int numCase = 1; numCase <= numCases; numCase++) {
		int N;
		double nb[1001], kb[1001];
	
		cin >> N;
		for (int i = 0; i < N; i++) cin >> nb[i];
		for (int i = 0; i < N; i++) cin >> kb[i];
		
		sort(nb, nb + N);
		sort(kb, kb + N);
		
		cout << "Case #" << numCase << ": " << getOptimalWarScore(kb, nb, N) << " " << N - getOptimalWarScore(nb, kb, N) << endl;
	}
}
