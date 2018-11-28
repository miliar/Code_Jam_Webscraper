#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(void) {
  	cin.sync_with_stdio(false);
	int T;
	cin >> T;
	for (int case_num = 1; case_num <= T; ++case_num) {
		vector<int> s1;
		int row1;
		cin >> row1;
		for (int y = 1; y <= 4; ++y) {
			for (int x = 1; x <=4; ++x) {
				int val;
				cin >> val;
				if (y == row1) {
					s1.push_back(val);
				}
			}
		}
		vector<int> s2;
		int row2;
		cin >> row2;
		for (int y = 1; y <= 4; ++y) {
			for (int x = 1; x <=4; ++x) {
				int val;
				cin >> val;
				if (y == row2) {
					s2.push_back(val);
				}
			}
		} 
		sort(s1.begin(), s1.end()); 
		sort(s2.begin(), s2.end()); 
		vector<int>::iterator it; 
		vector<int> intersection(8);
		it = set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(), intersection.begin() );
		int count = it - intersection.begin();
		cout << "Case #" << case_num << ": ";
		if (count == 1) {
		  cout << intersection.front();
		} else if (count > 1) {
		  cout << "Bad magician!";
		} else {
		  cout << "Volunteer cheated!";
		}
		cout << endl;


	}
	return 0;
}
