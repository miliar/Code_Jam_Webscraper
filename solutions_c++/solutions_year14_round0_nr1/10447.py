#include<iostream>
#include<fstream>
int board1[4][4];
int board2[4][4];
int T;
int ans1;
int ans2;

int main (void){
	std::ifstream fin ("input.txt");
	std::ofstream fout("output.txt");
	fin >> T;
	for (int i = 0; i < T; i++){
		fin >> ans1;
		ans1--;
		for (int j = 0; j < 4; j++){
			for (int k = 0; k < 4; k++){
				fin >> board1[j][k];
			}
		}
		fin >> ans2;
		ans2--;
		for (int j = 0; j < 4; j++){
			for (int k = 0; k < 4; k++){
				fin >> board2[j][k];
			}
		}
				int num;
		int count = 0;
		int found = 0;
		for (int r = 0; r < 4; r++){
			num = board1[ans1][r];
			for (int j = 0; j < 4; j++){
				if (board2[ans2][j] == num){
					count++;
					found = num;
				}
			}
		}
		if (count == 1) fout << "Case #" << i+1 << ": " << found << "\n";
		else if (count == 0) fout << "Case #" << i+1 << ": Volunteer cheated!\n";
		else if (count > 1) fout << "Case #" << i+1 << ": Bad magician!\n";
	}
	fin.close();
	fout.close();
	return 0;
}