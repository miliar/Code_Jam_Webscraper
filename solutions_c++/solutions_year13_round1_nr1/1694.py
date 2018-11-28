//============================================================================
// Name        : Bullseye.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int main() {
	int T = 0;
	cin >> T;
	//cout << "cases=" << T << endl;
	for(int i = 1; i <= T; i++){
		int r, t;
		cin >> r;	//inner circle in cm
		cin >> t;	//total paint in ml
		int Rin = r;
		int Rout = r + 1;
		//cout << "r=" << r << ", t=" << t << endl;
		int remainedPaint = t;
		int blackRings = 0;
		while(remainedPaint > 0){
			//cout << "Rin=" << Rin << ", Rout=" << Rout << ", remainedPaint=" << remainedPaint << endl;
			remainedPaint -= (Rout*Rout - Rin*Rin);
			if(remainedPaint >= 0){
				blackRings++;
			}
			//cout << "Rin=" << Rin << ", Rout=" << Rout << ", remainedPaint=" << remainedPaint << endl;
			Rout += 2;
			Rin += 2;
		}
		cout << "Case #" << i << ": " << blackRings << endl;
	}
	return 0;
}
