#include <iostream>
#include <string>

using namespace std;

int main() {
	int T;
	cin >> T;
	for(int i=1;i <=T; i++) {
		int X,R,C;
		cin >> X >> R >> C;
		string S;
		if(X == 1 ) {
			S = "GABRIEL";
		}
		else if( X == 2 ) {
			if(R == 1 || R == 3) {
				if(C == 1 || C == 3)
					S = "RICHARD";
				else 
					S = "GABRIEL";
			}
			else
					S = "GABRIEL";
		}
		else if( X == 3)  {
			if(R == 1 )
					S = "RICHARD";
			else if(R == 3) {
				if(C == 1)
					S = "RICHARD";
				else
					S = "GABRIEL";
			}
			else if(R == 2) {
				if(C == 3)
					S = "GABRIEL";
				else
					S = "RICHARD";
			}
			else {
				if(C == 3)
					S = "GABRIEL";
				else
					S = "RICHARD";
			}
		}
		else {
			if(R == 4 ){
				if(C == 4 || C == 3)
					S = "GABRIEL";
				else
					S = "RICHARD";
			}
			else if(R == 3 ) {
				if(C == 4)
					S = "GABRIEL";
				else
					S = "RICHARD";
			}
			else 
				S = "RICHARD";
		}
		cout << "Case #"<< i << ": " << S << endl;
	}
	return 0;
}
