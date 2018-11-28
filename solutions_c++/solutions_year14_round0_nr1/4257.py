#include <iostream>

using namespace std;

int main(){
	
	int T;
	cin >> T;
	for (int y = 1; y <= T; y++){
		int row1,row2;
		int mat1[4][4], mat2[4][4];
		cin >> row1;
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				cin >> mat1[i][j];
				}
			}
			
		cin >> row2;
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				cin >> mat2[i][j];
				}
			}
		int r1[4], r2[4];
		
		for (int i = 0; i < 4; i++){
			r1[i] = mat1[row1 - 1][i];
			r2[i] = mat2[row2 - 1][i];
		}
		int count = 0;
		int soln1;
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				if (r1[i] == r2[j]){
					count++;
					soln1 = r1[i];
					}
				}
			}
			
		if (count == 0){
			cout << "Case #" << y << ": Volunteer cheated!" << endl;
			}
		else if (count == 1){
			cout << "Case #" << y << ": " << soln1 << endl;
			}
		else {
			cout << "Case #" << y << ": Bad magician!" << endl;
			}
	}
}
