#include <stdio.h>
#include <fstream>
#include <vector>
#include <set>
#include <iostream>

using namespace std;

int main(){
	ifstream file("in");
	int testcase;
	file >> testcase;
	
	for(int i = 0; i < testcase; i++){
		printf("Case #%d: ", i+1);
		file>>c>>f>>x;
		double c, f, x;
		double currentTime = 0.0;
		double rate = 2.0;
		double timeToX = x/rate;
		double timeToNextX = x/(rate+f);
		double timeToC = c/rate;

		while(currentTime+timeToC+timeToNextX < currentTime+timeToX){
			currentTime = currentTime + timeToC;
			rate = rate + f;
			timeToC = c/rate;
			timeToX = x/rate;
			timeToNextX = x/(rate+f);
		}

		currentTime = currentTime + timeToX;
		printf("%.7f\n", currentTime);
	}

	return 0; 
}
