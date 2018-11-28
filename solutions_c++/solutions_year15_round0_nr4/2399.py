#include <iostream>
using namespace std;

string n[2] = {"GABRIEL", "RICHARD"};

int doit(){
	int X, R, C;
	cin >> X >> R >> C;
	if(X == 1) return 0;
	if(X == 2){
		if(R%2 == 0 || C%2 == 0) return 0;
		else return 1;
	}
	if(X==3){
		if((R%3 == 0 || C%3 == 0) && (R > 1 && C > 1)) return 0;
		else return 1;
	}
	if(X == 4){
		if(R*C%4 == 0 && (R > 2 && C > 2)) return 0;
		else return 1;
	}
	
}

int main() {
	int L;
	cin >> L;
	for(int i = 1; i <= L; i++){
		cout << "CASE #" << i << ": " << n[doit()] << endl;
	}
}