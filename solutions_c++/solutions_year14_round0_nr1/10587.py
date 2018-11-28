using namespace std;

#include <fstream>
#include <string>

int main()
{
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	int grid[4][4];
	int numTest, firstAns, secAns;
	fin >> numTest;
	for (int a=0; a<numTest; a++){
		fin >> firstAns;
		int possible[16];
		int posCount = 0;
		for (int i=0; i<4; i++)	{
			for (int j=0; j<4; j++){
				fin >> grid[i][j];
				if (i==firstAns-1){
					possible[posCount]=grid[i][j];
					posCount++;
				}
			}
		}
		fin >> secAns;
		int newPosCount = 0;
		int foundVal;
		for (int i=0; i<4; i++){
			for (int j=0; j<4; j++){
				fin >> grid[i][j];
				if (i==secAns-1){
					bool found = false;
					for (int k=0; k<posCount; k++){
						if (grid[i][j]==possible[k]){
							found = true;
							foundVal = grid[i][j];
						}
					}
					if (found){
						newPosCount++;
					}
				}
			}
		}
		fout << "Case #" << a+1 << ": ";
		if (newPosCount == 0){
			fout << "Volunteer cheated!" << endl;
		}
		else if (newPosCount == 1){
			fout << foundVal << endl;
		}
		else{
			fout << "Bad magician!" << endl;
		}
	}
	return 0;
}