#include<iostream>
#include<vector>
using namespace std;
int main() {
	int t, q1, q2;
	int matrix[4][4], row1[4], row2[4];
	cin >> t;
	for(int k = 0; k < t; k++) {
		cin >> q1;
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				cin >> matrix[i][j];
			}
		}
		for(int i = 0; i < 4; i++)
			row1[i] = matrix[q1 - 1][i];;

		cin >> q2;
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				cin >> matrix[i][j];
			}
		}
		for(int i = 0; i < 4; i++)
			row2[i] = matrix[q2 - 1][i];;
		int count = 0;
		int val = -1;
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				if(row2[j] == row1[i]) {
					count++;
					val = row2[j];
				}
			}
		}
		cout << "Case #" << k + 1 << ": "; 
		if(val == -1)
			cout << "Volunteer cheated!\n";
		else if(count > 1)
			cout << "Bad magician!\n";
		else
			cout << val << "\n";


	}
	return 0;
}
