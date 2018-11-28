#include <iostream>
#include <set>
#include <vector>
#include <algorithm>

using namespace std;

int grid1[4][4] = {};
int grid2[4][4] = {};
set<int> row1, row2;

int main() {
	int nCases = 0;
	cin >> nCases;
	for(int i = 0; i < nCases; i++) {
		row1.clear(); 
		row2.clear();
		short bad = 0; // 0 == good, 1 == bad magician, 2 == bad volunteer
		int A1, A2;
		
		cin >> A1;
		A1--; // convert to 0-based index
		for(int y = 0; y < 4; y++) {
			for(int x = 0; x < 4; x++) {
				cin >> grid1[y][x];
				if(y == A1) row1.insert(grid1[y][x]);
			}
		}
		cin >> A2;
		A2--;
		for(int y = 0; y < 4; y++) {
			for(int x = 0; x < 4; x++) {
				cin >> grid2[y][x];
				if(y == A2) row2.insert(grid2[y][x]);
			}
		}
		/*
		for(auto it = row1.begin(); it != row1.end(); it++) {
			cout << *it << " ";
		}
		cout << endl;
		for(auto it = row2.begin(); it != row2.end(); it++) {
			cout << *it << " ";
		}
		cout << endl;
		*/
		
		// check for cheating volunteer - row1 has none of row2
		if(find_first_of(row1.begin(), row1.end(), row2.begin(), row2.end()) == row1.end()) {		
			bad = 2;
			cout << "Case #" << i+1 << ": Volunteer cheated!" << endl;
			continue;
		}
		
		// check for correct card - row1 and row2 have only 1 element in common
		vector<int> v;
		set_intersection(row1.begin(), row1.end(), row2.begin(), row2.end(), back_inserter(v));
		if(v.size() == 1) {
			bad = 0;
			cout << "Case #" << i+1 << ": " << v[0] << endl;
			continue;
		}  
		
		// check for bad magician - all cards in row1 should be in different columns
		for(int y = 0; y < 4; y++) {
			bool found = false;
			for(int x = 0; x < 4; x++) {
				if(row1.find(grid2[y][x]) != row1.end()) {
					if(found) {
						bad = 1;
						break;
					}
					else {
					    found = true;
					}
				} 
			}
		}
		if(bad == 1) {
			cout << "Case #" << i+1 << ": Bad magician!" << endl;
		}
	}
}
