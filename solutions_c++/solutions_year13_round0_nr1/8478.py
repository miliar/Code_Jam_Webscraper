#include <fstream>
#include <string>

using namespace std;

ifstream input("input");
ofstream output("output");

int main() {
	int T;
	input >> T;
	for (int i = 1; i <= T; i++) {
		string row[4];
		for (int j = 0; j < 4; j++) input >> row[j];
		int horizontalO[4] = {0}, verticalO[4] = {0}, diagonalO[2] = {0};
		int horizontalX[4] = {0}, verticalX[4] = {0}, diagonalX[2] = {0};
		bool ended = true;
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				if ( (row[j])[k] == 'T' || (row[j])[k] == 'X' ) {
					horizontalX[j]++;
					verticalX[k]++;
					if (j-k == 0) diagonalX[0]++;
					if (j+k == 3) diagonalX[1]++;
				}
				if ( (row[j])[k] == 'T' || (row[j])[k] == 'O' ) {
					horizontalO[j]++;
					verticalO[k]++;
					if (j-k == 0) diagonalO[0]++;
					if (j+k == 3) diagonalO[1]++;
				}
				if ( (row[j])[k] == '.' ) ended = false;
			}
		}
		bool hasAWinner = false;
		for (int j = 0; j < 4; j++) {
			if (horizontalO[j] == 4) { output << "Case #" << i <<": O won" << endl; hasAWinner = true; }
			if (horizontalX[j] == 4) { output << "Case #" << i <<": X won" << endl; hasAWinner = true; }
			if (verticalO[j] == 4) { output << "Case #" << i <<": O won" << endl; hasAWinner = true; }
			if (verticalX[j] == 4) { output << "Case #" << i <<": X won" << endl; hasAWinner = true; }
		}
		if (diagonalO[0] == 4) { output << "Case #" << i <<": O won" << endl; hasAWinner = true; }
		if (diagonalX[0] == 4) { output << "Case #" << i <<": X won" << endl; hasAWinner = true; }
		if (diagonalO[1] == 4) { output << "Case #" << i <<": O won" << endl; hasAWinner = true; }
		if (diagonalX[1] == 4) { output << "Case #" << i <<": X won" << endl; hasAWinner = true; }
		if (!hasAWinner)
			if (!ended) output << "Case #" << i << ": Game has not completed" << endl;
			else output <<  "Case #" << i << ": Draw" << endl;
	}	
	input.close();
	output.close();
	return 0;
}

