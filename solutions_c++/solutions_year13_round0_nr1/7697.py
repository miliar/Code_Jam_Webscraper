#include <iostream>

using namespace std;

char test(string);

void dots(string, bool&);

int main(int argc, char *argv[]){
	int testCases;	
	cin >> testCases;
	string *results = new string[testCases];
	for(int in = 0; in < testCases; in++) results[in] = "";
	bool foundDots;	
	string junk; //holds the carriage return
	string matrix[4]; //x,y	
	
	for(int i = 0; i < testCases; i++){ //for each case
		foundDots = false;
		bool xWon = false;
		bool oWon = false;
		for(int j = 0; j < 4; j++){ //populate the matrix	
			cin >> matrix[j];
			//test horizontal
			string row = matrix[j];
			char result = test(row);
			dots(row, foundDots);
			if (result == 'X'){
				xWon = true;			
			}else if(result == 'O'){
				oWon = true;
			}
		}
		//finished populating the matrix	
		//test vertically
		string column = "";
		for(int colnum = 0; colnum < 4; colnum++){
			column = "";
			for(int row = 0; row < 4; row++){
				column += matrix[row][colnum];
			}
			//cout << "column " << "0" << " is: " << column << endl;
			char result = test(column);	
			if (result == 'X'){
				//cout << "Case #" << i << ": " << "X won" << endl;
				xWon = true;
				break;			
			}else if(result == 'O'){
				//cout << "Case #" << i << ": " << "O won" << endl;
				oWon = true;
				break;
			}
		}
		//test diagonally
		string diag = "";
		diag += matrix[0][0];
		diag += matrix[1][1];
		diag += matrix[2][2];
		diag += matrix[3][3];
		char result = test(diag);
		if (result == 'X'){
			xWon = true;			
		}else if(result == 'O'){
			oWon = true;
		}
	
		diag = "";
		diag += matrix[0][3];
		diag += matrix[1][2];
		diag += matrix[2][1];
		diag += matrix[3][0];

		result = test(diag);
		if (result == 'X'){
			xWon = true;			
		}else if(result == 'O'){
			oWon = true;
		}		
		if(xWon) results[i] = "X won";
		else if(oWon) results[i] = "O won";
		//test if there are .s, or if the game is a draw
		else if (foundDots) results[i] = "Game has not completed";
		else results[i] = "Draw";
		getline(cin, junk);
			
			
	}
	//loop through the array and print results for each round	
	for(int y = 0; y < testCases; y++) cout << "Case #" << y+1 << ": " << results[y] << endl;
	//free the memory!
	delete[] results;
	return 0;
}

char test(string row){
	int xCount = 0;
	int oCount = 0;
	for(int k = 0; k < 4; k++){
		//count the Xs, if 3, and if t present, X win
		//count the Os, if 3, and if t present, O win
		if(row[k] == 'X') xCount++;
		if(row[k] == 'O') oCount++;				
	}					
	if((row.find('T')) != (std::string::npos)){
		if(xCount == 3) return 'X';
		else if(oCount == 3) return 'O';		 
	}else if(xCount == 4){
		return 'X';
	}else if(oCount == 4){
		return 'O';
	}
	return 'Z';
}

void dots(string row, bool &foundDots){ //returns true if dots found
	int numDots = 0;	
	for(int k = 0; k < 4; k++) if(row[k] == '.') numDots++;
	if (numDots > 0) foundDots = true;
}


