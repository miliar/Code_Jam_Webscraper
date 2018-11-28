#include <iostream>
#include <fstream>
#include <iomanip>
 
using namespace std;
 
int main() {

	fstream output("output2.txt", fstream::out);
	//outputFile << "writing to file";
	fstream input("input.txt", fstream::in);

	output.precision(7);

	int testcases = 0;
	long double cps = 2;
	long double time = 0.0;
	long double C = -1.0;
	long double F = -1.0;
	long double X = -1.0;

	input >> testcases;
    input.ignore(1, '\n');

	for(int i = 0; i < testcases; i++){
		//C,F,X
		input >> C;
		input >> F;
		input >> X;
		
		//cout << std::fixed << std::setprecision(5) << C << ", " << F << ", " << X << endl;
		time+=C/cps;
		while(true){
				//If seconds to finish is less than time it takes to buy and then finish.
				//cout << (X-C)/cps << " vs " << X/(cps+F) << endl;
				if((X-C)/cps > (X/(cps+F))){
					cps += F;
					time+=C/cps;
					//cout << "time: " << time << endl;
				}
				else{
					time += (X-C)/cps;
					break;
				}
		}

		output << "Case #" << i+1 << ": ";
		output << std::fixed << time;

		time = 0.0;
		cps = 2;

		if(i != testcases-1){
			output << endl;
		}
	}
	
	return 0;
}