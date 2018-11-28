#include<iostream>
#include<iomanip>
#include<fstream>
#include<string>
#include<cstring>

using namespace std;

class board{

	private:
		char matrix[4][4];

	public:
		board();
		~board();
		void setBoard(string, string, string, string);
		int evaluate();
};

board::board(){

	for(int i = 0; i < 4; i++){

		for(int j = 0; j < 4; j++){

			matrix[i][j] = 'a';
		}
	}
}

board::~board(){

	//Nothing
}

void board::setBoard(string a, string b, string c, string d){

	for(int i = 0; i < 4; i++){

		matrix[0][i] = a[i];
	}

	for(int i = 0; i < 4; i++){

		matrix[1][i] = b[i];
	}

	for(int i = 0; i < 4; i++){

		matrix[2][i] = c[i];
	}

	for(int i = 0; i < 4; i++){

		matrix[3][i] = d[i];
	}

	return;
}

int board::evaluate(){

	int tx = 100;
	int ty = 99;
	
	if(matrix[0][0] == matrix[0][1] && matrix [0][0] == matrix[0][2] && matrix[0][0] == matrix[0][3]){

		if(matrix[0][0] == 'X'){

			return 0;
		}
		else if(matrix[0][0] == 'O'){

			return 1;
		}
	}

	if(matrix[1][0] == matrix[1][1] && matrix [1][0] == matrix[1][2] && matrix[1][0] == matrix[1][3]){

		if(matrix[1][0] == 'X'){

			return 0;
		}
		else if(matrix[1][0] == 'O'){

			return 1;
		}
	}

	if(matrix[2][0] == matrix[2][1] && matrix [2][0] == matrix[2][2] && matrix[2][0] == matrix[2][3]){

		if(matrix[2][0] == 'X'){

			return 0;
		}
		else if(matrix[2][0] == 'O'){

			return 1;
		}
	}

	if(matrix[3][0] == matrix[3][1] && matrix [3][0] == matrix[3][2] && matrix[3][0] == matrix[3][3]){

		if(matrix[3][0] == 'X'){

			return 0;
		}
		else if(matrix[3][0] == 'O'){

			return 1;
		}
	}

	if(matrix[0][0] == matrix[1][0] && matrix [0][0] == matrix[2][0] && matrix[0][0] == matrix[3][0]){

		if(matrix[0][0] == 'X'){

			return 0;
		}
		else if(matrix[0][0] == 'O'){

			return 1;
		}
	}

	if(matrix[0][1] == matrix[1][1] && matrix [0][1] == matrix[2][1] && matrix[0][1] == matrix[3][1]){

		if(matrix[0][1] == 'X'){

			return 0;
		}
		else if(matrix[0][1] == 'O'){

			return 1;
		}
	}

	if(matrix[0][2] == matrix[1][2] && matrix [0][2] == matrix[2][2] && matrix[0][2] == matrix[3][2]){

		if(matrix[0][2] == 'X'){

			return 0;
		}
		else if(matrix[0][2] == 'O'){

			return 1;
		}
	}

	if(matrix[0][3] == matrix[1][3] && matrix [0][3] == matrix[2][3] && matrix[0][3] == matrix[3][3]){

		if(matrix[0][3] == 'X'){

			return 0;
		}
		else if(matrix[0][3] == 'O'){

			return 1;
		}
	}

	if(matrix[0][0] == matrix[1][1] && matrix [0][0] == matrix[2][2] && matrix[0][0] == matrix[3][3]){

		if(matrix[0][0] == 'X'){

			return 0;
		}
		else if(matrix[0][0] == 'O'){

			return 1;
		}
	}

	if(matrix[0][3] == matrix[1][2] && matrix [0][3] == matrix[2][1] && matrix[0][3] == matrix[3][0]){

		if(matrix[0][3] == 'X'){

			return 0;
		}
		else if(matrix[0][3] == 'O'){

			return 1;
		}
	}

	for(int s = 0; s < 4; s++){

		for(int t = 0; t < 4; t++){

			if(matrix[s][t] == 'T'){

				tx = s;
				ty = t;
				break;
			}
		}
	}

	if(matrix[((tx + 1) % 4)][ty] == matrix[((tx + 2) % 4)][ty] && matrix[((tx + 1) % 4)][ty] == matrix[((tx + 3) % 4)][ty]){

		if(matrix[((tx + 1) % 4)][ty] == 'X'){

			return 0;
		}
		else if(matrix[((tx + 1) % 4)][ty] == 'O'){

			return 1;
		}
	}

	if(matrix[tx][((ty + 1) % 4)] == matrix[tx][((ty + 2) % 4)] && matrix[tx][((ty + 1) % 4)] == matrix[tx][((ty + 3) % 4)]){

		if(matrix[tx][((ty + 1) % 4)] == 'X'){

			return 0;
		}
		else if(matrix[tx][((ty + 1) % 4)] == 'O'){

			return 1;
		}
	}

	if((tx == ty) || ((tx + ty) == 3)){

		if(tx == ty){

			if(matrix[((tx + 1) % 4)][((ty + 1) % 4)] == matrix[((tx + 2) % 4)][((ty+ 2) % 4)] && matrix[((tx + 1) % 4)][((ty + 1) % 4)] == matrix[((tx + 3) % 4)][((ty + 3) % 4)]){

				if(matrix[((tx + 1) % 4)][((ty + 1) % 4)] == 'X'){

					return 0;
				}
				else if(matrix[((tx + 1) % 4)][((ty + 1) % 4)] == 'O'){

					return 1;
				}
			}
		}
		else{

			if(matrix[((tx - 1) % 4)][((ty + 1) % 4)] == matrix[((tx - 2) % 4)][((ty + 2) % 4)] && matrix[((tx - 1) % 4)][((ty + 1) % 4)] == matrix[((tx - 3) % 4)][((ty + 3) % 4)]){

				if(matrix[((tx - 1) % 4)][((ty + 1) % 4)] == 'X'){

					return 0;
				}
				else if(matrix[((tx - 1) % 4)][((ty + 1) % 4)] == 'O'){

					return 1;
				}
			}
		}

	}

	int full = 1;

	for(int m = 0; m < 4; m++){

		for(int n = 0; n < 4; n++){

			if(matrix[m][n] == '.'){

				full = 0;
				break;
			}
		}
	}

	if(full == 1){

		return 2;
	}
	else{

		return 3;
	}

	return 5;
}

int main(){

	int count = 1;
	string numTest;
	int testNum = 1;
	int getEval = 0;
	board A;
	string one, two, three, four, dummy;

	ifstream in_file;
	in_file.open("smallA.txt");

	getline(in_file, numTest);

	char* dum = &numTest[0];
	int numTestN = atoi(dum);

	for(int i = 0; i < numTestN; i++){

		getline(in_file, one);
		getline(in_file, two);
		getline(in_file, three);
		getline(in_file, four);

		A.setBoard(one, two, three, four);
		getEval = A.evaluate();

		if(getEval == 0){

			cout << "Case #" << count << ": " << "X won" << endl;
		}
		else if(getEval == 1){

			cout << "Case #" << count << ": " << "O won" << endl;
		}
		else if(getEval == 2){

			cout << "Case #" << count << ": " << "Draw" << endl;
		}
		else if(getEval == 3){

			cout << "Case #" << count << ": " << "Game has not completed" << endl;
		}
		else{

			cout << "Let's hope it doesn't come to this..." << endl;
		}

		count++;

		getline(in_file, dummy);
	}

	return 0;	
}
