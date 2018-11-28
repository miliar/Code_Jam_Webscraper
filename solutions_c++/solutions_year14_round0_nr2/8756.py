
#include <iostream>
#include <fstream>
#include <stack>
#include <vector>
#include <stdlib.h>
#include <iomanip>
using namespace std;
ifstream my("B-large.in");
ofstream of("a.txt");
int main() {
	int all;
	my>>all;
	for(int a = 1; a <= all; a++){
		of<<"Case #"<<a<<": ";
		double c;
		double f;
		double x;
		double income = 2;
		double time = 0;
		my>>c>>f>>x;
		if(x < c)
			of<<x/2<<"\n";
		else{
			while((x - c) / income > x / (f + income)){
				time += c / income;
				income += f;
			}
			time += x / income;
			of<<std::fixed<<std::setprecision(7)<<time<<"\n";
		}


	}
	return 0;
}
