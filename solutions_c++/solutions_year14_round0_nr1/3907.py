#include<iostream>
#include<vector>
#include<fstream>
using namespace std;
int main() {
	ifstream cin("input.txt");
	int row;
	int row1;
	int num;
	int count = 0;
	int vec[4][4];
	int vec1[4][4];
	int loops;
	cin >> loops;
	for(int i = 1; i <= loops; i++) {
		cin >> row;
		for(int j = 0; j < 4; j++) {
			for(int k = 0; k < 4; k++) {
				cin >> vec[j][k];
			}
		}
		cin >> row1;
		for(int j = 0; j < 4; j++) {
			for(int k = 0; k < 4; k++) {
				cin >> vec1[j][k];
			}
		}
		for(int j = 0; j < 4; j++) {
			for(int k = 0; k < 4; k++) {
				if(vec[row - 1][j] == vec1[row1 - 1][k]) {
					count = count + 1;
					num = vec[row][j];
				}
			}
		}
		if(count == 1) {
			cout << "Case #" << i << ": " << num << endl;
		}else if(count > 1) {
			cout << "Case #" << i << ": Bad magician!" << endl;
		} else if(count == 0) {
			cout << "Case #" << i << ": Volunteer cheated!" << endl;
		}
		count  = 0;
	}
}