#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector<string> str(4);

bool check(char p){
	bool blD = true;
	bool brD = true;

	bool bWon = false;
	for(int r = 0 ; r < 4 ; r++) {
		bool bRow = true;
		bool bCol = true;
		for(int i = 0; i < 4 ; i++) {
			if(str[r][i] != p && str[r][i] != 'T')
				bRow = false;
			if(str[i][r] != p && str[i][r] != 'T')
				bCol = false;
		}
		if(bRow || bCol) bWon = true;
		
		if(str[r][r] != p && str[r][r] != 'T') 
			blD = false;
		if(str[r][3-r] != p && str[r][3-r] != 'T')
			brD = false;
	}
	if(blD || brD) bWon = true;
	return bWon;
}

bool hasEmpty() {
	for(int i = 0 ; i < 4 ; i++) {
		for(int j = 0 ; j < 4 ; j++){
			if(str[i][j] == '.')
				return true;
		}
	}
	return false;
}

int main() {
	int N; 
	cin>> N ; 

	for(int T = 1 ; T <= N ; T++) {
		for(int i = 0 ;i < 4 ; i++)
			cin>> str[i]; 

		bool bx = check('X') ;
		bool bo = check('O') ; 

		string ret;
		if(bx)  ret = "X won";
		else if(bo)  ret = "O won";
		else if(hasEmpty()) ret = "Game has not completed";
		else ret = "Draw";

		cout<<"Case #"<<T<<": "<<ret<<endl;
	}
	return 0 ;
}