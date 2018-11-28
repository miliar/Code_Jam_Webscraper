#include <iostream>

using namespace std;

int main() {
	int T, row1, row2, count, index;
	int first[4][4], second[4][4];
	cin >> T;
	int k = 1;
	while(T--) {
		cin >> row1;
		for(int i=0;i<4;i++) {
			for(int j=0;j<4;j++)
				cin >> first[i][j];
		}
		cin >> row2;
		for(int i=0;i<4;i++) {
			for(int j=0;j<4;j++)
				cin >> second[i][j];
		}
		count = 0;
		for(int i=0;i<4;i++) {
			for(int j=0;j<4;j++) {
				if(first[row1-1][i] == second[row2-1][j]) {
					count++;
					index = i;
				}
			}
		}
		if(count == 1)
			cout << "Case #" <<k << ": " << first[row1-1][index] << "\n";
		else if(count == 0)
			cout << "Case #" <<k << ": Volunteer cheated!\n" ;
		else
			cout << "Case #" <<k << ": Bad magician!\n" ;
		k++;
	}
	return 0;
}