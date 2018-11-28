#include <iostream>
#include <fstream>
using namespace std;
int main() {
	ifstream fin("A-small-attempt0.in");
	ofstream fout("out.txt");
	int t, x, y;
	int grid[4][4];
	int ans[4];
	fin >> t;
	for (int i = 0; i < t; i++){
		fin >> x;
		x--;
		for (int j = 0; j < 4; j++){
			ans[j] = 0;
			for (int k = 0; k < 4; k++)
				fin >> grid[j][k];
		}
		for (int j = 0; j < 4; j++){
			ans[j] = grid[x][j];
		}
		fin >> y;
		y--;
		for (int j = 0; j < 4; j++){
			for (int k = 0; k < 4; k++)
				fin >> grid[j][k];
		}
		int flag = -1;

		for (int j = 0; j < 4; j++){
			for (int k = 0; k < 4; k++){
				if (ans[j] == grid[y][k]){
					if (flag == -1)
						flag = ans[j];
					else
						flag = -2;
				}
			}
		}
		fout << "Case #" << i + 1 << ": ";
		if (flag == -2)
			fout << "Bad magician!" << endl;
		else if (flag == -1)
			fout << "Volunteer cheated!" << endl;
		else
			fout << flag << endl;
	}
	return 0;
}