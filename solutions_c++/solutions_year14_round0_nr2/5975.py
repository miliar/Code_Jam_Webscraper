#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

int main(int argc, char* argv[]){
	ifstream data(argv[1]);
	if(!data){cerr << "Couldn't open file." << endl; return -1;}

	ofstream output("problemB.out");

	int cases;
	data >> cases;

	for(int ca = 1; ca <= cases; ca++){
		double time = 0.0;
		double c, f, x;
		double cps = 2.0;

		data >> c;
		data >> f;
		data >> x;

		
		while(true){
			double curTime, farmTime;
			
			curTime = x/cps;
			farmTime = (c/cps) + (x/(cps+f));

			if(curTime < farmTime){
				time += curTime;
				break;
			}
			else{
				time += c/cps;
				cps += f;
			}
		}

		output << fixed;
		output << setprecision(7);

		output << "Case #" << ca << ": " << time << endl;
	}
	
	data.close();
	output.close();
}
