#include <iostream>
#include <fstream>

using namespace std;

double min_time(double C, double F, double X, double rate)
{
	double buy_farm, not_buy;
	not_buy = X/rate;
	buy_farm = C/rate + X/(rate + F);
	
	if (not_buy < buy_farm) {
		return X/rate;	
	} else {
		return C/rate + min_time(C, F, X, rate + F);
	}
}

int main(int argc, char* argv[])
{
	ifstream input;
	ofstream output;
	
	output.precision(10);
	//cout.precision(10);
	
	input.open(argv[1]);
	output.open("output.out");
	
	int cases;
	input >> cases;
	
	for (int c = 1; c <= cases; c++) {
		double C, F, X;
		
		input >> C >> F >> X;

		output << "Case #" << c << ": ";
		output << min_time(C, F, X, 2);
		//cout << min_time(C, F, X, 2) << endl;
		
		if (c != cases) {
			output << endl;
		}
	}
	
	input.close();
	output.close();
}
