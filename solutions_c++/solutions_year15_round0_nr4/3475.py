#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;



bool eval(int X, int R, int C){
	if(X >= 7) return false;
	if(X == 1) return true;
	if(X == 2) return R*C%X == 0;
	if(X == 3) return (R > 1) && (C > 1) && R*C%X == 0;
	if(X == 4) return (R > 2) && (C > 2) && R*C%X == 0;
	if(R*C%X != 0) return false;

	return true; //Return true if gabriel can win
}

int main(){
	ifstream fin ("ominous.in");
	ofstream fout ("ominous.out");

	int T; fin >> T;
	
	for(int t = 0; t < T; t++){
		int X; fin >> X;
		int R; fin >> R;
		int C; fin >> C;

		string s = eval(X, R, C) ? "GABRIEL" : "RICHARD";

		fout << "Case #" << t+1 << ": " << s << endl;
	}

	return 0;
}