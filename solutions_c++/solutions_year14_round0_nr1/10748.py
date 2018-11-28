#include <iostream>
#include <algorithm>
#include <iterator>
#include <vector>

using namespace std;

vector<int> takeInput(int rowNum) {
	vector<int> ret;
	for (int i = 0; i < 4; i ++) {
		for (int j = 0; j < 4; j++) {
			int n;
			cin >> n;
			if (i != rowNum - 1) {
				continue;
			}	
			ret.push_back(n);
		}
	}
	return ret;
}

int main() {
	int N;
	cin >> N;
	int testNum = 1;
	while (N--) {
		vector<int> arr1(4, 0);
		vector<int> arr2(4, 0);
		int row1, row2;
		cin >> row1;
		arr1 = takeInput(row1);
		cin >> row2;
		arr2 = takeInput(row2);
		sort(arr1.begin(), arr1.end());
		sort(arr2.begin(), arr2.end());
		vector<int> intersection;
		std::set_intersection(arr1.begin(), arr1.end(),
							  arr2.begin(), arr2.end(),
							  std::back_inserter(intersection));
		cout << "Case #" << testNum << ": ";
		if (intersection.size() == 1) {
			cout << intersection[0] << "\n";
		} else if (intersection.size() == 0) {
			cout << "Volunteer cheated!" << "\n";
		} else {
			cout << "Bad magician!" << "\n";
		}
		testNum++;
	}
	return 0;
}