#include <iostream>

using namespace std;

int main(int argc, char* argv[]){

	int tests;
	cin >> tests;
	for(int i = 0; i < tests; i++){
		int X, R, C;
		cin >> X >> R >> C;
		if(R < C){int tmp = C; C = R; R = tmp;} // R always greater than C
		bool richardWins;
		if((R * C) % X != 0){richardWins = true;goto output;}
		if(X >= 7){richardWins = true;goto output;}
		if(X == 1){richardWins = false;goto output;}
		if(X == 2){
			if((R * C) % 2 == 0){richardWins = false;}
		} else if(X == 3){
			if(C < 2){richardWins = true;}
			else {richardWins = false;}
		} else if(X == 4){
			if(C == 1){richardWins = true;}
			else if(R <= 4 && C <= 2){richardWins = true;}
			else {richardWins = false;}
		} else {
			richardWins = true;	
		}


		// process here
		
		
		// output here
		output:
		cout << "Case #" << (i + 1) << ": ";
		if(richardWins){
			cout << "RICHARD" << endl;
		} else {
			cout << "GABRIEL" << endl;
		}

	}

	return 0;
}
