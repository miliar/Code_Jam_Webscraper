#include <iostream>
#include <set>

using namespace std;

int main(int argc, char** argv) {

	int T;
	
	cin >> T;
	
	for (int k = 0; k < T; k++) {
		int first, dummy;
		cin >> first;
		set<int> possibles1;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> dummy;
				if (i+1 == first) {
					possibles1.insert(dummy);
				}
			}
		}
		
		int second;
		cin >> second;
		set<int> possibles2;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				cin >> dummy;
				if (i+1 == second) {
					possibles2.insert(dummy);
				}
			}
		}
		
		set<int> intersection;
		for (set<int>::iterator it = possibles1.begin(); it != possibles1.end(); it++) {
			for (set<int>::iterator it2 = possibles2.begin(); it2 != possibles2.end(); it2++) {
				if (*it == *it2) intersection.insert(*it);
			}
		}
		
		cout << "Case #" << (k+1) << ": ";
		
		if (intersection.size() == 1) {
			cout << *intersection.begin();
		} else if (intersection.size() > 1) {
			cout << "Bad magician!";
		} else {
			cout << "Volunteer cheated!";
		}
		cout << endl;
	}

}