#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

double getTime(double X, double F, int cookies){
	return X / (2 + F*cookies);
}

double getResult(double C, double F, double X){
	int cookies = 0;
	double result = 0, temp, temp1, temp2;
	while (true){

		temp1 = result + getTime(X, F, cookies);
		temp2 = result + getTime(C, F, cookies) + getTime(X, F, cookies + 1);
		if (temp1 < temp2){
			return temp1;
		}
		result = result + getTime(C, F, cookies++);
	}
	return result;
}


int main(){
	ifstream cin("B-large.in");
	ofstream cout("out.ou");
	int t;
	cin >> t;
	double C, F, X;
	for (int i = 1; i <= t; i++){
		cin >> C >> F >> X;
		cout << "Case #" << i << ": " << fixed<< setprecision(7) << getResult(C, F, X) << endl;
	}

	return 0;
}
