#include <iostream>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int people;
		cin >> people;
		int nums[people];
		for (int i = 0; i <= people; i++) {
			char x;
			cin >> x;
			nums[i] = x - '0';
		}
		int total = 0;
		int numNew = 0;
		total = nums[0];
		for (int j = 1; j <= people; j++) {
			int current = nums[j];
			if (total < j) {
				numNew = numNew + (j - total);
				total = total + (j - total);
			}
			total = total + current;
		}
		cout << "Case #" << i + 1 << ": " << numNew << endl;
	}
}