#include <iostream>
using namespace std;


int T;
void win(int t){
	if(t+1 == T)
		cout << "Case #" <<t+1 << ": GABRIEL";
	else
		cout << "Case #" <<t+1 << ": GABRIEL" << endl;
}
void fail(int t){
	if(t+1 == T)
		cout << "Case #" <<t+1 << ": RICHARD";
	else
		cout << "Case #" <<t+1 << ": RICHARD" << endl;
}

int main(){


	cin >> T;
	for(int t = 0 ; t < T; t++){
		int X,R,C;
		cin >> X >> R >> C;
		if(X == 1)
			win(t);
		else if(X == 2 && R*C % 2 == 0)
			win(t);
		else if(X == 3 && R*C % 3 == 0 && (R > 1 && C > 1))
			win(t);
		else if(X == 4 && (R == 4 && C == 4 || R == 3 && C == 4 || R == 4 && C == 3))
			win(t);
		else
			fail(t);
	}
}