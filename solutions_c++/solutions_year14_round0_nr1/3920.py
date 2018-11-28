#include <string>
#include <iostream>
#include <vector>

using namespace std;

int main(){
	int T;
	int i,j,k;

	cin >> T;

	for (i=1;i<=T;i++){
		int one_row, two_row;
		int board_1[4][4];
		int board_2[4][4];

		cin >> one_row;
		for (j=0;j<4;j++){
			for (k=0;k<4;k++){
				cin >> board_1[j][k];
			}
		}

		cin >> two_row;

		for (j=0;j<4;j++){
			for (k=0;k<4;k++){
				cin >> board_2[j][k];
			}
		}

		bool found = false;
		bool found_again = false;
		int ans_col = 0;

		for (j=0;j<4;j++){
			for (k=0;k<4;k++){
				if (board_1[one_row-1][j] == board_2[two_row-1][k]){
					if (found){
						found_again = true;
					}
					found = true;
					ans_col = k;
				}
			}
		}

		cout << "Case #" << i <<": ";

		if (found && !found_again){
			cout << board_2[two_row-1][ans_col] << endl;
		}else if (found_again){
			cout << "Bad magician!" << endl;
		}else{
			cout << "Volunteer cheated!" << endl;
		}


		
	}
}