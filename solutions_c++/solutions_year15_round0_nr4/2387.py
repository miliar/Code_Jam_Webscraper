
#include <stdlib.h>
#include <iostream>
#include <math.h>



using namespace std;

int max_width_length(int X){
	if (X <= 2){
		return 1;
	}
	return ceil(sqrt(X));
}

bool play(int X, int R, int C){ // true if Richard, false if Gabriel
	if (X >= 7 || (C*R)%X != 0){
		return true;
	}
	if (max_width_length(X) > R || max_width_length(X) > C){
		return true;
	}
	if (X >= 4 && (max_width_length(X) == R || max_width_length(X) == C)){
		return true;
	}
	return false;
}

int main(){
	int test_cases;
	cin >> test_cases;
	for (int i = 1; i <= test_cases; i++){
		int X, R, C;
		cin >> X;
		cin >> R;
		cin >> C;
		bool richard = play(X, R, C);
		if (richard){
			cout << "Case #" << i << ": " << "RICHARD" << endl;
		}
		else {
			cout << "Case #" << i << ": " << "GABRIEL" << endl;
		}

	}


	return 0;
}