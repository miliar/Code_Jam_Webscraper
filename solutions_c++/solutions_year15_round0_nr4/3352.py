#include <iostream>

using namespace std;

int main(){
	int T, X, R, C;
	cin >> T;
	for(int i=0; i<T; i++){
		cin >> X >> R >> C;
		if(X == 1){
			cout << "Case #" << i+1 << ": GABRIEL\n";
		} else if(X == 2){
			if((R*C)%2 != 0)
				cout << "Case #" << i+1 << ": RICHARD\n";
			else
				cout << "Case #" << i+1 << ": GABRIEL\n";	
		} else if(X == 3){
			if((R*C)%3 != 0){
				cout << "Case #" << i+1 << ": RICHARD\n";
			} else if(R*C >= 6){ 
				// only %3's: 3, 6, 9
				cout << "Case #" << i+1 << ": GABRIEL\n";
			} else{
				cout << "Case #" << i+1 << ": RICHARD\n";
			}
		} else{
			if((R*C)%4 != 0){
				cout << "Case #" << i+1 << ": RICHARD\n";
			} else if(R*C >= 12){
				// only %4's: 4, 8, 12, 16
				cout << "Case #" << i+1 << ": GABRIEL\n";
			} else{
				cout << "Case #" << i+1 << ": RICHARD\n";
			}
		}
	}
	return 0;
}

