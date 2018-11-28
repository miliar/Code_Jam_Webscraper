#include <iostream>
#include <vector>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for(int i=1;i<=T;i++){
		int row1, row2;
		int matrix1[4][4], matrix2[4][4];

		cin >> row1;
		row1--;
		for(int j=0; j<4; j++){
			for(int k=0; k<4; k++){
				int tmp;
				cin >> tmp;
				matrix1[j][k] = tmp;
			}
		}

		cin >> row2;
		row2--;
		for(int j=0; j<4; j++){
			for(int k=0; k<4; k++){
				int tmp;
				cin >> tmp;
				matrix2[j][k] = tmp;
			}
		}

		vector<int> candidates;	
		for(int j=0; j<4; j++){
			for(int k=0; k<4; k++){
				if(matrix1[row1][j]==matrix2[row2][k]){
					candidates.push_back(matrix1[row1][j]);
				}
			}
		}

		cout << "Case #" << i << ": ";
		int size = candidates.size();
		if(size == 0){
			cout << "Volunteer cheated!";
		}else if(size == 1){
			cout << candidates[0];
		}else{
			cout << "Bad magician!";
		}
		cout << endl;
		
	}
}
