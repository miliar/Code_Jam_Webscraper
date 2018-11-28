#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
using namespace std;

double recurse (double c, double f, double x, double time, double rate) {
//	cout << x << "||" << rate << "||" << f << "\n";
//	cout << time << " > " << c/rate << "|" << x/(rate+f) << "\n";
	if (time > c/rate + x/(rate + f)) {
		return c/rate + recurse(c,f,x,x/(rate+f),rate+f);
	} else {
		return time;
	}
}

int main() {
	ifstream input( "B.in" );
	ofstream output("B.out");
	string line;
	getline(input, line);
	int count = atoi(line.c_str());
	
	for (int k = 0; k < count; k++) {
		if (k != 0) {
			output << "\n";
		}
		
		double c, f, x;
		input >> c >> f >> x;
//		cout << c << "|" << f << "|" << x << "\n";
		double ans = recurse (c, f, x, x/2, 2);
//cout << "------------------------------\n";
		output.precision(10);
		output <<  "Case #" << k+1 << ": " << ans;
	}
	
	return 0;

}
