#include <iostream>
#include <iomanip>
#include <cstdio>
using namespace std;



void JeMoeder(int caseNr){
	cout << "Case #" << (caseNr) << ": ";
	
	// read configuration
	double C,F,X;
	cin >> C >> F >> X;
	
	// starting values
	double R = 2;
	double time = (X / R);
	double now = 0;
	double newTime = 0;
	
	while(true){
		// buy cookie farm
		now += C / R;
		R += F;
		
		double newTime = now + (X / R);
		
		if(newTime < time){
			time = newTime;
		} else {
			printf("%.7f\n",time);
			break;
		}
	}
	
}

int main(){
	int runs; cin >> runs;
	for(int i = 1; i <= runs; i++){
		JeMoeder(i);
	}
}