#include <iostream>
#include <vector>
using namespace std;

void printArr(int coinJamArr[], int N) {
	for (int i = N-1; i >=0; i--)
	{
		cout << coinJamArr[i];
	}
	cout << " 3 4 5 6 7 8 9 10 11" << endl;
}

void printCoinJams(int coinJamArr[], int start, int end, int N, int& J) {
	if (J > 0) {
		printArr(coinJamArr, N);
		J--;
	}
	if (start > end)
		return;
	for (int i = start; i < end; i+=2) {
		coinJamArr[i] = 1;
		coinJamArr[i+1] = 1;
		printCoinJams(coinJamArr, start, i-1, N, J);
		coinJamArr[i] = 0;
		coinJamArr[i+1] = 0;
	}
}

int main() {
	int T, N, J;
	std::cin >> T;
	int res = 0;
	for (int i = 1; i <= T; i++) 
	{
		std::cin >> N >> J;
		int coinJamArr[N];
		for (int j = 0; j < N; j++)
			coinJamArr[j] = 0;

		coinJamArr[0] = 1;
		coinJamArr[1] = 1;
		coinJamArr[N-2] = 1;
		coinJamArr[N-1] = 1;
		cout << "Case #" << i << ":" << endl;
		printCoinJams(coinJamArr, 2, N-3, N, J);

	}

}

