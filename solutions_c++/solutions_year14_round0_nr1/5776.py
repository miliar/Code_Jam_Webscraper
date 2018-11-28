#include <iostream>
#include <map>
#include <vector>

using namespace std;

int main() {
	int n; cin >> n;
	for (int i = 1; i <= n; i++) {
		int a; cin >> a;
		int first[4][4];
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				cin >> first[j][k];
			}
		}
		int b; cin >> b;
		int second[4][4];
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				cin >> second[j][k];
			}
		}
	
		vector <int> hacks;
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				if (first[a-1][j] == second[b-1][k]) {
					hacks.push_back(first[a-1][j]);
				}
			}
		}
		
		
		cout << "Case #" << i << ": ";
			
		if (hacks.size() > 1) {
			cout << "Bad magician!" << endl;
		} else if (hacks.size() == 0) {
			cout << "Volunteer cheated!" << endl;
		} else {
			cout << hacks[0] << endl;
		}
	}

}
