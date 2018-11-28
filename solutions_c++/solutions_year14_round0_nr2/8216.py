#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

int main()
{
	ifstream fin("B-large.in");
	ofstream fout("output.txt");
	
	int total;
	
	// get the total number of test cases
	fin >> total;
	if (total == 0 || total > 100) {
		cout << "Invalid Input parameter!" << endl;
		return -1;
	}

	double C, F, X;	
	for (int i = 0; i < total; i++) {
		// get the C, F and X
		fin >> C >> F >> X;
		
		double timeToBuy = 0.0d;
		double currentF = 2.0d;
		double currentCookie = 0.0d;
		double timeToGetX = 0.0d;
		double totalTime = 0.0d;

		while (1) {	
			timeToGetX = X / currentF;
			timeToBuy = C / currentF ;

			if (timeToGetX < timeToBuy + (X / (currentF + F))) {
				int s = (int)(log10(totalTime + timeToGetX) + 1);
				fout.setf(ios::showpoint);
				fout.precision(s + 7);
				fout << "Case #" << i + 1 << ": " << totalTime + timeToGetX << endl;
				break;
			}
			
			totalTime += timeToBuy;
			currentF += F;
		}	
	}
	
	return 0;
}