/* Tic Tac Tomek */

/*
            0,3
		1,2
	2,1
3,0

*/

#include <iostream>
#include <cstdio>
	using namespace std;

char matrix[4][4];
const int n = 4;

void readBoard() {

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin>>matrix[i][j];
		}
	}
			
}

void calculate() {

	int rowO = 0, rowX = 0, colO = 0, colX = 0, diagO = 0, diagX = 0, hasEmpty = 0, odrDiagX = 0, odrDiagO = 0;
	char win = 'N';
	
	for (int i = 0; i < n; i++) {
	
		for (int j = 0; j < n; j++) {

			if (matrix[i][j] == '.')
				hasEmpty = 1;
		
			//For row-wise
			
			if (matrix[i][j] == 'X' || matrix[i][j] == 'T')	rowX++;
			if (matrix[i][j] == 'O' || matrix[i][j] == 'T')	rowO++;
			
			//For column-wise
			
			if (matrix[j][i] == 'X' || matrix[j][i] == 'T')	colX++;
			if (matrix[j][i] == 'O' || matrix[j][i] == 'T')	colO++;
					
			//For diagonal
			
			if (i == 0) {
			
				if (matrix[j][j] == 'X' || matrix[i][j] == 'T')	diagX++;
				if (matrix[j][j] == 'O' || matrix[i][j] == 'T')	diagO++;
				
			}
			
			if (i+j == n-1) {
			
				if (matrix[i][j] == 'X' || matrix[i][j] == 'T')	odrDiagX++;
				if (matrix[i][j] == 'O' || matrix[i][j] == 'T')	odrDiagO++;
			
			}
			
		}
		
		//Now check for winners
	
		if (rowX == n || colX == n || diagX == n) {
			
			win = 'X';
			break;
			
		}
		
		else if (rowO == n || colO == n || diagO == n) {
			
			win = 'O';
			break;
			
		}
		
		rowX = colX = rowO = colO = 0;
		
	}
	
	if (odrDiagX == n)	win = 'X';
	if (odrDiagO == n)	win = 'O';
	
	//Now output

	if (win != 'N')
		cout<<win<<" won"<<endl;
		
	else if (hasEmpty == 0)
		cout<<"Draw"<<endl;
		
	else
		cout<<"Game has not completed"<<endl;

}

int main() {

	int total;
	cin>>total;
	
	char bakwas;

	for (int i = 0; i < total; i++) {
		readBoard();
		cout<<"Case #"<<(i+1)<<": ";
		calculate();
		
	}
	
}