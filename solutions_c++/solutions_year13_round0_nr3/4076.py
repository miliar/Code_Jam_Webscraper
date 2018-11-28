#include <iostream>




using namespace std;


char line[10][10];


bool test_heng(int n,char c) {
	for(int i=0;i<4;i++){
		if(line[n][i]!=c && line[n][i]!='T'){
			return false;
		}
	}
	return true;
}


bool test_shu(int n,char c) {
	for(int i=0;i<4;i++){
		if(line[i][n]!=c && line[i][n]!='T'){
			return false;
		}
	}
	return true;
}


bool test_diag(char c) {
	for(int i=0;i<4;i++){
		if(line[i][i]!=c && line[i][i]!='T'){
			return false;
		}
	}
	return true;
}


bool test_anti_diag(char c) {
	for(int i=0;i<4;i++){
		if(line[i][3-i]!=c && line[i][3-i]!='T'){
			return false;
		}
	}
	return true;
}

bool not_finished() {
	for (int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(line[i][j]=='.'){
				return true;
			}
		}
	}
	return false;
}

//1: X won
//2: O won
//3: Draw
//4: Game has not completed
int test() {
	for(int i = 0;i<4;i++){
		if(test_heng(i,'X')) {
			return 1;
		}
		if(test_shu(i,'X')) {
			return 1;
		}
	}
	if(test_diag('X')) {
		return 1;
	}
	if(test_anti_diag('X')) {
		return 1;
	}

	for(int i = 0;i<4;i++){
		if(test_heng(i,'O')) {
			return 2;
		}
		if(test_shu(i,'O')) {
			return 2;
		}
	}
	if(test_diag('O')) {
		return 2;
	}
	if(test_anti_diag('O')) {
		return 2;
	}

	if(not_finished()) {
		return 4;
	}

	return 3;

}


int main(){


	int TotalCases;
	cin>>TotalCases;


	for(int iCase = 1; iCase <= TotalCases ; iCase ++ ) {
	
		for (int i=0;i<4;i++){
			cin.getline(line[i],8);
			if(line[i][0]!='.' && line[i][0]!='T' && line[i][0]!='X' && line[i][0]!= 'O') {
				cin.getline(line[i],8);
			}
		}

		typedef char * str;
	
		str msg[5];

		msg[1]="X won\n";
		msg[2]="O won\n";
		msg[3]="Draw\n";
		msg[4]="Game has not completed\n";


		cout<<"Case #"<<iCase<<": "<<msg[test()];

	}




	return 0;

}
