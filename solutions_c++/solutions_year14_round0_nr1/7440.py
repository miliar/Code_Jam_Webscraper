
#include <iostream>
#include <vector>
using namespace std;

int main() {
	int testsCount;
	cin >> testsCount;
	for (int test = 1; test <= testsCount; ++test) {
		vector<int> seen(17, 0);
		int pairs = 0;
		int answer = -1;
		for (int arrangement = 0; arrangement < 2; ++arrangement) {
			int specialRow;
			cin >> specialRow;
			for (int row = 0; row < 4; ++row)
				for (int col = 0; col < 4; ++col) {
					int num;
					cin >> num;
					if (row == specialRow - 1) {
						seen[num]++;
						if (seen[num] == 2) {
							++pairs;
							answer = num;
						}
					}
				}
		}
		cout << "Case #" << test << ": ";
		if (pairs == 0)
			cout << "Volunteer cheated!";
		else if (pairs == 1)
			cout << answer;
		else 
			cout << "Bad magician!";
		cout << endl;
	}
	return 0;
}