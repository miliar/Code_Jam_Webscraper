#include <fstream>
#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

int main() {
	
	int t;
	double x, f, c;
	
	string filename;
	cin >> filename;

	ifstream infile (filename);

	ofstream outfile ("output.txt");

	infile >> t;
	
	for (int a = 0; a < t; ++a) {
		double cps = 2.0f;
		
		infile >> c >> f >> x;
		
		double curTime = x / cps;
		double ttf = c / cps;
		double newTime = x / (cps + f);		
		double timesofar = 0.0f;
		double nextRd = timesofar + newTime + ttf;
		//outfile << "cur = " << curTime << " ttf = " << ttf << " next = " << nextRd << " newTime = " << newTime << "\n";
		//int ctr = 0;
		while (curTime > nextRd) {			
			//outfile << "cur = " << curTime << " ttf = " << ttf << " next = " << nextRd << " newTime = " << newTime << "\n";
			cps += f;
			curTime = nextRd;
			timesofar = timesofar + ttf;
			ttf = c / cps;
			newTime = x / (cps + f);
			nextRd = timesofar + newTime + ttf;
		} 
		//outfile << "cur = " << curTime << " ttf = " << ttf << " next = " << nextRd << " newTime = " << newTime << "\n";
		//outfile << ctr << "\n";
		outfile << "Case #" << a + 1 << ": " << fixed <<  setprecision(7) << curTime << "\n";
	}
}