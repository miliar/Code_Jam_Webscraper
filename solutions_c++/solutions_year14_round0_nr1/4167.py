#include<iostream>
#include<set>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		int pos;
		cin >> pos;
		set<int> possibles;
		possibles.clear();
		for (int i = 1; i <= 4; i++) {
			for (int j = 0; j < 4; j++) {
				int x; 
				cin >> x;
				if (i == pos) possibles.insert(x);
			}
		}

		cin >> pos;
		int matches = 0;
		int the_number = 0;
		for (int i = 1; i <= 4; i++) {
			for (int j = 0; j < 4; j++) {
				int x; 
				cin >> x;
				if (i == pos && possibles.find(x) != possibles.end()) {
					the_number = x;
					matches ++;
				}
			}
		}
		cout << "Case #" << tc << ": ";
		switch(matches) {
			case 0:
				cout << "Volunteer cheated!" << endl;
				break;
			case 1:
				cout << the_number << endl;
				break;
			default:
				cout << "Bad magician!" <<endl;
				break;
		}
	}
}
