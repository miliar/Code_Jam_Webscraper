#include<iostream>

using namespace std;

int main(void){

	int T;
	int X;
	int R;
	int C;

	cin >> T;
	for(int t=1;t<=T;t++){
		cin >> X >> R >> C;
		cout << "Case #" << t << ": ";
		switch(X){
		case 1:
			cout << "GABRIEL"<< endl;
			break;
		case 2:
			if(R*C % X == 0) cout << "GABRIEL" << endl;
			else cout << "RICHARD" << endl;
			break;
		case 3:
			if(R <= X-2 || C <= X-2) cout << "RICHARD" << endl;
			else if(R*C % X != 0) cout << "RICHARD" << endl;
			else cout << "GABRIEL" << endl;
			break;
		case 4:
			if(R <= X-2 || C <= X-2) cout << "RICHARD" << endl;
			else if(R*C % X != 0) cout << "RICHARD" << endl;
			else cout << "GABRIEL" << endl;
			break;
		case 5:
		case 6:
		default:
			break;
		}	
	}
	return 0;
}
