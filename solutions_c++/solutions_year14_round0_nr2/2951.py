#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <cfloat>
#include <iomanip>

using namespace std;

int main(int argc, char *argv[]){
	int T;
	
	ifstream inputfile(argv[1]);
	ofstream outputfile("output.txt");

	inputfile >> T;
	
	for(int i=0; i<T; i++){
		double C,F,X;
		inputfile >> C >> F >> X;
		double speed=2.0;
		double delay=0.0;
		double time = X/speed;
		double newTime = DBL_MAX;
		while(delay < time){
			newTime = delay + C/speed + X/(speed + F);
			if(newTime < time) time = newTime;
			delay += C/speed;
			speed += F;
		}
		cout << "Case #" << i+1 << ": " << fixed << setprecision(7) << time << endl;
		outputfile << "Case #" << i+1 << ": "<< fixed << setprecision(7) << time<< endl;
	}
	return 0;
}