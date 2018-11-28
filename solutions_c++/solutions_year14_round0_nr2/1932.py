#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;

int main() {
	ifstream in("B-large.in");
	ofstream out("Output.txt");
	int T;
	in >> T;
	for (int n=0; n<T; ++n) {
		double C, F, X;
		in >> C >> F >> X;
		double rate = 2;
		if (X <= C) {
			out<<"Case #"<<n+1<<": "<<setprecision(7)<<fixed<<X/rate<<endl;
			continue;
		}
		double sec = C / rate;
		while ((X-C)/rate > X/(rate+F)) {
			rate += F;
			sec += C / rate;
		}
		sec += (X-C) / rate;
		out<<"Case #"<<n+1<<": "<<setprecision(7)<<fixed<<sec<<endl;
	}
	return 0;
}