#include <iostream>
#include <string>

using namespace std;

int main(){

	int T, X, R, C;
	bool TF = true;
	
	cin >> T;

	for(int TC = 1; TC <=T; TC++){

		cin >> X >> R >> C;

		switch(X){
		case 1:
			TF = true;
			break;
		case 2:
			if((R*C) % X != 0)
				TF = false;
			else 
				TF = true;
			break;
		case 3:
			if(R==1 || C==1)
				TF = false;
			else if((R*C) % X != 0)
				TF = false;
			else
				TF = true;
			break;
		case 4:
			if((R*C) % X != 0)
				TF = false;
			else{
				int RC = R * C;
				if(RC == 4 || RC == 8)
					TF = false;
				else if(RC == 12 || RC == 16)
					TF = true;
			}
			break;
		}
		
		cout << "Case #" << TC << ": ";
		if(TF)
			cout << "GABRIEL" << " " << endl;
		else
			cout << "RICHARD" << " " << endl;
	}
	return 0;
}