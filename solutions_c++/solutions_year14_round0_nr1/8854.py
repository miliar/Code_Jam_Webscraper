#include <iostream>
using namespace std;

int main() {
	int T = 0;
	int curr = 0;
	int first [4][4];
	int second [4][4];
	int firstRow = 0;
	int secondRow = 0;
	int count = 0;
	int pos;
	
	cin >> T;
	
	for(int i = 1; i <= T; i++) {
		count = 0;
		cin >> firstRow;
		firstRow = firstRow - 1;
		for(int x = 0; x < 4; x++) {
			for(int y = 0; y < 4; y++){
				cin >> first[x][y];
			}
		}
		cin >> secondRow;
		secondRow = secondRow - 1;
		for(int x = 0; x < 4; x++) {
			for(int y = 0; y < 4; y++){
				cin >> second[x][y];
			}
		}
		for(int x = 0; x < 4; x++) {
			for(int y = 0; y < 4; y++){
				if(first[firstRow][x] == second[secondRow][y]) {
					count++;
					pos = x;
				}
			}
		}
		cout << "Case #" << i << ": ";
		if(count > 1) {
			cout << "Bad magician!" << endl;
		}
		else if(count == 1) {
			cout << first[firstRow][pos] << endl;
		}
		else if(count < 1){
			cout << "Volunteer cheated!" << endl;
		}
	}
	
	return 0;
}