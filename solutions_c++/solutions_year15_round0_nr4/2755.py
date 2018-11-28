#include <iostream>
using namespace std;

constexpr int min (int a, int b){ return (a < b ? a : b) ;}
int getint(void){int m; cin >>m; return m; }

bool answer(void){
	const int X = getint();
	const int R = getint();
	const int C = getint();
	if (R*C % X != 0) return true;
	if (X == 1) return false;
	if (X == 2) return false;
	if (R == 1 or C == 1) return true;
	if (X == 4 and (R == 2 or C == 2)) return true;
	return false;
	}

int main(void){
	const int t = getint();
	for (int q = 0; q < t; ++q) 
		cout << "Case #" << q+1 << ": " << (answer() ? "RICHARD": "GABRIEL") << endl;
}
