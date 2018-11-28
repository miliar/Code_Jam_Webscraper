#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

void main(){
	ifstream in;
	in.open("B-large.in");
	ofstream out; 
	out.open("out1.txt");

	int T;
	double C, F, X;
	double minTime = 0.0;
	double rate = 2.0;
	in >> T;
	for (int i = 0; i < T; i++) {
		minTime = 0.0;
		rate = 2.0;
		in >> C >> F >> X;
		while(true) {
			if ((minTime + (X/rate)) < (minTime + C/rate + X/(rate+F))) {
				minTime += X/rate;
				break;
			}
			minTime += C/rate;
			rate += F;
		}
		out << "Case #" << i+1 << ": " << fixed << setprecision(12) << minTime << endl;
	}
	in.close();
	out.close();

}