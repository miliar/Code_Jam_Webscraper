#include <iostream>
#include <fstream>
using namespace std;


void main(){

	fstream fin, fout;

	fin.open("input.in", ios::binary | ios::in);
	fout.open("out.txt", ios::trunc | ios::out);

	int T, x1, x2;
	int grid[4][4];
	int grid2[4][4];
	int y;
	int count;

	fin >> T;

	for (int x = 1; x <= T; x++){
	
		fin >> x1;

		for (int i = 0; i < 4; i++){
		
			for (int j = 0; j < 4; j++){
			
				fin>>grid[i][j];

			}

		}

		fin >> x2;

		for (int i = 0; i < 4; i++){

			for (int j = 0; j < 4; j++){

				fin >> grid2[i][j];

			}

		}

		y = 0;
		count = 0;
		for (int i = 0; i < 4; i++){
		
			for (int j = 0; j < 4; j++){
				if (grid[x1 - 1][i] == grid2[x2 - 1][j])
				{
					y = grid[x1 - 1][i];
					count++;
				}
			}
		}

	

		if (count == 0){
		
			fout << "Case #" << x << ": Volunteer Cheated!" << endl;
			
		}
		else if (count == 1){
		
			fout << "Case #" << x << ": " << y << endl;

		}
		else {
		
			fout << "Case #" << x << ": Bad Magician!" << endl;


		}

	}

	fin.close();
	fout.close();

}