#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

int main(){
	ifstream input("B-large.in");
	ofstream output("B-large.out");
	
	int t, cs = 1;
	input >> t;
	
	while(t--){
		double C, F, X;
		input >> C >> F >> X;
		
		double n = 0.0, t_farm = 0.0;
		
		while(((C / (2.0 + F*n)) + (X / (2.0 + F*(n + 1.0)))) < ((X / (2.0 + F*n)))){
			t_farm += (C / (2.0 + F*n));
			n += 1.0;
		}
		
		output << "Case #" << cs << ": ";
		output << fixed << setprecision(7) << t_farm + (X / (2 + F*n)) << endl;
		cs++;
	}
	
	return 0;
}
