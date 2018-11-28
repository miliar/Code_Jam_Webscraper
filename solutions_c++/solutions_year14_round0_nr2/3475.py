#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
	
	int t;
	double C,F,X,cPSec, secAcum;
	cin >> t;
	cout.precision(8);
	cout.setf( ios::fixed, ios::floatfield );
	cin.precision(6);
	for(int i = 1; i <= t; ++i){
		cout << "Case #" << i << ": ";
		cin >> C;
		cin >> F;
		cin >> X;
		cPSec = 2;
		secAcum = 0;
		while((X/cPSec - C/cPSec) > (X / (cPSec + F))){
			secAcum += C/cPSec;
			cPSec += F;
		}
		secAcum += X / cPSec;
		cout << secAcum << endl;
	}
	return 0;
}