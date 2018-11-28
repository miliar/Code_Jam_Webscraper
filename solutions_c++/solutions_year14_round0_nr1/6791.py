#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(void) {
	int T;
	cin >> T;

	for(int i = 1; i <= T; i++) {
		int first_answer;
		cin >> first_answer;
		vector<int> first_row;
		for(int j = 1; j <= 4; j++) {
			for(int k = 0; k < 4; k++) {
				int v;
				cin >> v;
				if(first_answer == j) {
					first_row.push_back(v);
				}
			}
		}

		int second_answer;
		cin >> second_answer;
		vector<int> second_row;
		for(int j = 1; j <= 4; j++) {
			for(int k = 0; k < 4; k++) {
				int v;
				cin >> v;
				if(second_answer == j) {
					second_row.push_back(v);
				}
			}
		}


		vector<int> result;
		sort(first_row.begin(), first_row.end());
		sort(second_row.begin(), second_row.end());
		set_intersection(first_row.begin(), first_row.end(), second_row.begin(), second_row.end(), back_inserter(result));

		cout << "Case #" << i << ": ";
		if(result.size() == 1) {
			cout << result[0];
		} else if(result.size() == 0) {
			cout << "Volunteer cheated!";
		} else {
			cout << "Bad magician!";
		}
		cout << endl;
	}
	return 0;
}
