#include <iostream>
using namespace std;

int main(){
	int T, X, R, C;
	cin >> T;
	for(int caso=1; caso<T+1; caso++){
		cin >> X >> R >> C;
		cout << "Case #" << caso <<": ";
		if(X==1){
			cout << "GABRIEL" << endl;
			continue;
		}

		if(X>R && X>C){
			cout << "RICHARD" << endl;
			continue;
		}
		if(C*R%X!=0){
			cout << "RICHARD" << endl;
			continue;
		}
		int h1 = (X+(X%2))/2, h2=X-h1+1;
		if((R<h1 || C<h2) && (R<h2 || C<h1)){
			cout << "RICHARD" << endl;
			continue;
		}
		if(X==4 && ((R==4 && C==2) || (C==4 && R==2))){
			cout << "RICHARD" << endl;
			continue;
		}

		cout << "GABRIEL" << endl;
	}
}