#include <iostream>
#include <string>
#include <sstream>
#include <algorithm> 

using namespace std;

int main(){
	int T;
	cin >> T;
	for(int t = 1; t < T + 1; t++){
		int X,R,C;
		cin >> X >> R >> C;
		string solution = "RICHARD";
		if(X == 1) solution = "GABRIEL";
		if(X == 2 && (R % 2 == 0 || C % 2 == 0)) solution = "GABRIEL";
		if(X == 3 && R != 1 && C != 1 && (R == 3 || C == 3)) solution = "GABRIEL";
		if(X == 4 && R != 1 && C != 1 && R != 2 && C != 2 && (R == 4 || C == 4)) solution = "GABRIEL";
		cout << "Case #" << t << ": " << solution << "\n";
	}
}
