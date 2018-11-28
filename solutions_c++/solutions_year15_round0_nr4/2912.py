#include <iostream>
#include <string>

using namespace std;

int main(){
	int T;
	cin >> T;
	for(int i=1; i<=T; ++i){
		int X, R, C;
		cin >> X >> R >> C;
		string c;
		if(X == 1){
			c = "GABRIEL";
			//c = "RICHARD";
		} else if(X == 2){
			if(R * C % 2 == 0){
				c = "GABRIEL";
			}
			else {
				c = "RICHARD";
			}
		} else if(X == 3){
			if(R * C % 3 == 0 && R * C != 3){
				c = "GABRIEL";
			}
			else {
				c = "RICHARD";
			}
		} else {
			if(R * C % 4 == 0 && R * C > 8){
				c = "GABRIEL";
			}
			else {
				c = "RICHARD";
			}
		}
		
		cout << "Case #" << i << ": " << c << endl;
	}
	return 0;
}

