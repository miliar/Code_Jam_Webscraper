#include <iostream>
#include <vector>
#include <sstream>
#include <string>

using namespace std;

int main () {
	int test_cases;
	cin >> test_cases;
	vector<int> result(test_cases, -100);
	
	for (int i = 0; i < test_cases; i++) {
		int row1, row2;
		cin >> row1;	// get first choice
		vector<vector<int> > arrangement(4);
		
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				int a;
				cin >> a;
				arrangement[j].push_back(a);	
			}
		}
		
		vector<int> c1 = arrangement[row1-1];	
		cin >> row2;
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				int a;
				cin >> a;
				arrangement[j][k] = a;	
			}
		}
		
		vector<int> c2 = arrangement[row2-1];
		
		int count = 0;
		for (int j = 0; j < 4; j++) {
			int c = c1[j];
			for (int k = 0; k<4; k++) {
				//cout << c << ' ' << c2[k] << endl;
				if (c2[k] == c) {
					count++;
					if (count == 1) {
						result[i] = c;
					} else {
						result[i] = -1;
					}
				}	
			}
		}
	}
	string s = "Case #";
	int count = 1;
	for (int i = 0; i < test_cases; i++) {
		cout << s;
		cout << to_string(count) << ": ";
		if (result[i] >= 0) {
			cout << result[i] << endl;
		} else if (result[i] == -1) {
			cout << "Bad magician!" << endl;
		} else {
			cout << "Volunteer cheated!" << endl;
		}
		count++;
	}
}
