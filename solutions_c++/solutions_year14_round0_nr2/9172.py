#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <iomanip>

using namespace std;

int main(){
	ifstream inData("input2.txt");
	ofstream outData("output2.txt");
	int num;
	inData >> num;
	for(int i = 0; i < num; i++){
		double ttime = 0;
		double ncook = 0;
		double rate = 2;
		double C, F, X;
		inData >> C >> F >> X;

		while(ncook != X){
			if(X/rate > C/rate + X/(rate+F)){
				ttime += C/rate;
				rate+=F;
			}
			else{
				ttime += X/rate;
				ncook = X;
			}
		}
		outData << fixed << setprecision(7) << showpoint;
		outData << "Case #" << i+1 << ": " << ttime << endl;
	}

	return 0;
}