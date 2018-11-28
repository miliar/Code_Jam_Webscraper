#include <iostream>
using namespace std;

int main(){

	int T;
	int X, R, C;

	int richwin = 0;
	int bigger;
	int smaller;

	cin >> T;
	for (int i = 1; i <= T; i++){
		richwin = 0;
		cin >> X >> R >> C;

		if (X >= 7) richwin = 1;

		bigger = R;
		if (R < C){ 
			bigger = C;
			smaller = R;
		}
		else{
			smaller = C;
		}

		if (X >= smaller + 2) richwin = 1;
		if (X >= bigger + 1) richwin = 1;
		if ((R*C) % X != 0) richwin = 1;
		
		cout << "Case #" << i << ": ";
		if (richwin == 1) cout << "RICHARD";
		else cout << "GABRIEL";
		cout << endl;
	}


	return 0;
}