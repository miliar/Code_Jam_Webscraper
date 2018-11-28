#include <iostream>
#include <fstream>
#include <vector>

#include <iomanip>

int main() {
	std::ifstream f("B-large.in");	// open the file to read in data
	if (!f) {
		std::cerr << "Error: Failed to open." << std::endl;
		return -1;
	}

	std::ofstream myfile;
  	myfile.open ("output.txt");
  	//myfile.precision(15);

	int nCase; // number of cases
	f >> nCase;
	int i;

	for (i = 0; i < nCase ; i++) {
		double C;
		f >> C;
		double F;
		f >> F;
		double X;
		f >> X;
		double gainSpeed = 2.0;
		double totalTime = 0.0;
		std::vector<double> timeLine;

		while(X/gainSpeed > (C/gainSpeed + X/(gainSpeed + F))) {
			timeLine.push_back(C/gainSpeed);
			gainSpeed += F;
		}

		unsigned int j;
		for(j = 0 ; j < timeLine.size(); j++) totalTime += timeLine[j];

		totalTime = totalTime + X/gainSpeed;

		myfile << "Case #" << i+1 << ": " << std::fixed << std::setprecision(7) 
			<<	totalTime << std::endl;
	}
	myfile.close();
	return 0;

}