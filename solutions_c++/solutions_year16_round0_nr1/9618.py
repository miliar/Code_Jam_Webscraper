#include <iostream>
#include <unordered_set>
using namespace std;

int countSheep(int N) {
	if (N == 0)
		return -1;
	unordered_set<int> left({0, 1, 2, 3, 4, 5, 6, 7, 8, 9});
	int count = 0, save = N;
	while (!left.empty()) {
		N = save * (++count);
		while (N) {
			int digit = N % 10;
			N /= 10;
			left.erase(digit);
		}
	}
	return count * save;
}

int main() {
	int count, N;
	cin >> count;
	for (int i = 1; i <= count; i++) {
		cout << "Case #" << i << ": ";
		cin >> N;
		int sheepN = countSheep(N);
		if (sheepN == -1)
			cout << "INSOMNIA";
		else
			cout << sheepN;
		cout << endl;
	}
	return 0;
}