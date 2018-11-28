#include <iostream>
#include <cstring>

using namespace std;

int main(){
	int T, cas;
	cas = 1;
	cin >> T;
	while (cas <= T) {
		cout << "Case #" << cas << ": ";
		int row1, row2;
		int grid1[4][4];
		int grid2[4][4];
		memset(grid1,0,sizeof grid1);
		memset(grid2,0,sizeof grid2);

		cin >> row1;
		--row1;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				cin >> grid1[i][j];
		cin >> row2;
		--row2;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				cin >> grid2[i][j];

		int result = 0;
		int finds[16];
		memset(finds,0,sizeof finds);

		for (int i = 0; i < 4; ++i) {
			++finds[grid1[row1][i]-1];
			++finds[grid2[row2][i]-1];
		}

		int duplicates = 0;
		for (int i = 0; i < 16; ++i) {
			if (finds[i] == 2) {
				++duplicates;
				result = i+1;
			}
		}

		if (duplicates == 1)
			cout << result << endl;
		else if (duplicates == 0)
			cout << "Volunteer cheated!" << endl;
		else 
			cout << "Bad magician!" << endl;

		++cas;
	}
}