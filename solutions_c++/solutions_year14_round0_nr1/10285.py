#include <iostream>
using namespace std;
int main(){
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("MyOutput.txt", "w", stdout);
	int T; cin >> T;
	for(int tc = 1; tc<=T; tc++){
		int matrix1[4][4],matrix2[4][4], row1,row2;
			cin >> row1;
			for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				cin >> matrix1[i][j];
		cin >> row2;
		for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			cin >> matrix2[i][j];
		int counter = 0, target;
		for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++){
			if (matrix1[row1-1][i] == matrix2[row2-1][j]) counter++, target = matrix2[row2-1][j];
		}
		cout << "Case #" << tc << ": ";
		if (!counter) cout << "Volunteer cheated!\n";
		else if (counter == 1) cout << target << endl;
		else if (counter > 1) cout << "Bad magician!\n";
	}
	return 0;
}