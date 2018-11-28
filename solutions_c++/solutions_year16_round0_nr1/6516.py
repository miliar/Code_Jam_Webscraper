#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>

using namespace std;


int main() {

	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		int N;
		cin >> N;
		set<int> nums;
		set<int> digits;
		int curN = N;
		cout << "Case #" << (t+1) << ": ";
		while (true) {
			if (nums.find(curN) != nums.end()) {
				cout << "INSOMNIA" << endl;
				break;
			}
			nums.insert(curN);
			int n = curN;
			while (n > 0) {
				int rem = n % 10;
				digits.insert(rem);
				n /= 10;
			}
			if (digits.size() >= 10) {
				cout << curN << endl;
				break;
			}
			curN += N;
		}
	}

	return 0;
}