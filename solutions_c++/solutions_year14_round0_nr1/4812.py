#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int main() {

	int T;
	cin >> T;

	for( int i = 1; i < T+1; ++i ) {
		int first, second;
		int choice = 0;
		vector<int> row1, row2;
		vector<int> v;
		string garbage;

		cout << "Case #" << i << ": ";
		
		cin >> first;
		
		for( int j = 1; j < 5; ++j) {
			int num;
			for (int k = 0; k < 4; ++k) {
				cin >> num;
				if ( j == first ) {
					row1.push_back(num);
				}
			}
		}

		cin >> second;

		for( int j = 1; j < 5; ++j) {
			int num;
			for (int k = 0; k < 4; ++k) {
				cin >> num;
				if ( j == second ) {
					row2.push_back(num);
				}
			}
		}

		sort(row1.begin(), row1.end());
		sort(row2.begin(), row2.end());

		set_intersection(row1.begin(),row1.end(),
				 row2.begin(),row2.end(),
				 back_inserter(v));

		if (v.size() == 0) {
			cout << "Volunteer cheated!\n";
		} 
		else if (v.size() == 1) {
			cout << v[0] << '\n';
		}
		else {
			cout << "Bad magician!\n";
		}
	}

}
