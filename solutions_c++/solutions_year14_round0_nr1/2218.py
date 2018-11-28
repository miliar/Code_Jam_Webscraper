#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdlib>
#include <cmath>
#include <iomanip>

using namespace std;

int main(){
	ifstream fin;
	ofstream fout;
	fin.open("input.in");
	fout.open("result.txt");

	int times;
	int row1[2][4];
	int choosed_row;
	fin >> times;
	int a;

	for (int i = 0; i < times; i++){
		fin >> choosed_row;
		
		for (int j = 0; j < 16; j++){
			if (j / 4 == choosed_row - 1){
				fin >> row1[0][j % 4];
			}
			else{
				fin >> a;
			}
		}

		fin >> choosed_row;
		int k = 0;
	
		for (int j = 0; j < 16; j++){
			if (j / 4 == choosed_row - 1){
				fin >> row1[1][k];
				k++;
			}
			else{
				fin >> a;
			}
		}

		int indicator = 0;
		for (int j = 0; j < 4; j++){
			for (int k = 0; k < 4; k++){
				if (row1[0][j] == row1[1][k] && indicator == 0){
					indicator = row1[0][j];
				}
				else if (row1[0][j] == row1[1][k] && indicator != 0){
					indicator = 17;
				}
			}
		}
		
		if (indicator < 17 && indicator > 0){
			fout << "Case #" << i + 1 << ": " << indicator << endl;
		}
		else if (indicator >= 17){
			fout << "Case #" << i + 1 << ": Bad magician!" << endl;
		}
		else{
			fout << "Case #" << i + 1 << ": Volunteer cheated!" << endl;
		}
	}

	fin.close();
	fout.close();
	return 0;
}