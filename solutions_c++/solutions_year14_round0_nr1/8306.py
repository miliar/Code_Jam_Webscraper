#include<fstream>
#include<map>
using namespace std;

int main(void){
	ifstream fin;
	ofstream fout;
	fin.open("A-small-attempt0.in", ios_base::in);
	fout.open("A-small-attempt0.out", ios_base::trunc);
	int T;
	fin >> T;
	for(int c = 1; c <= T; c++){
		int row1, row2;
		int grid1[4][4], grid2[4][4];
		fin >> row1;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				fin >> grid1[i][j];
		fin >> row2;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				fin >> grid2[i][j];
		row1--;
		row2--;
		int count[17];
		for(int i = 0; i < 17; i++)
			count[i] = 0;
		for(int i = 0; i < 4; i++){
			int key1 = grid1[row1][i];
			int key2 = grid2[row2][i];
			count[key1]++;
			count[key2]++;
		}
		int card = -1;
		int state = 2; // 0 - success, 1 - bad, 2 - cheated
		for(int i = 1; i <= 16; i++){
			if(count[i] > 1){
				card = i;
				if(state == 0)
					state = 1;
				if(state == 2)
					state = 0;
			}
		}
		if(state == 0){
			fout << "Case #" << c << ": " << card << endl;
		}
		else if(state == 1){
			fout << "Case #" << c << ": " << "Bad magician!" << endl;
		}
		else if(state == 2){
			fout << "Case #" << c << ": " << "Volunteer cheated!" << endl;
		}
	}
	return 0;
}
