#include <iostream>
#include <iomanip>

using namespace std;

int main(){
	double T, C, F, X;
	cin >> T;

	double toX, newToX, toC;
	double rate;
	double time;
	bool finished;
	for(int t=1; t<=T; t++){
		cin >> C >> F >> X;
		cout << "Case #" << t << ": ";

		cout.precision(8);
		finished = false;
		time=0; 
		rate = 2;
		toX = X / rate;
		toC = C / rate;

		if(toX < toC){
			cout << fixed << toX << endl;
			continue;
		}

		while(!finished){
			rate += F; 

			newToX = X/rate;
			if(toC + newToX < toX){
				toX = newToX;
				time += toC;
			}
			else{
				time += toX; 
				finished = true;
			}
			toC = C/rate;

		}

		cout << fixed << time << endl;
	}
}
