#include <iostream>
#include <cstdlib>
#include <fstream>

using namespace std;

int main() {
    ofstream ofile;
    ofile.open ("output.txt");

    ifstream ifile;
    ifile.open("input.txt");

	int test = 0;
	int row1 = 0;
	int row2 = 0;
	int arr[4][4];
	int memo1[4];
	int memo2[4];
	ifile >> test;
	for(int t = 1; t <= test; t++){
		ifile >> row1;
		row1--;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				ifile >> arr[i][j];
			}
		}

		for(int i = 0; i < 4; i++){
			memo1[i] = arr[row1][i];
		}

		ifile >> row2;
		row2--;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				ifile >> arr[i][j];
			}
		}

		for(int i = 0; i < 4; i++){
			memo2[i] = arr[row2][i];
		}

		int count = 0;
		int answer = 0;
		for(int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++) {
				if(memo1[i] == memo2[j]){
					answer = memo1[i];
					count++;
				}
			}
		}

		if(count == 0){
			ofile << "Case #" << t << ": Volunteer cheated!" << endl;
		} else if (count == 1) {
			ofile << "Case #" << t << ": " << answer << endl;
		} else {
			ofile << "Case #" << t << ": Bad magician!" << endl;
		}
	}
	return 0;
}
