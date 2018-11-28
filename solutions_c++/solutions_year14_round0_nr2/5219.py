/******************************************************************************************
*           .--.																		  *
* ::\`--._,'.::.`._.--'/::			@author Ana M. Mihut	@course GCJ					  *
* ::::. `  __::__ ' .:::::			@alias  LT-Kerrigan		@date   12.04.2014			  *
* ::::::-:.`'..`'.:-::::::			@link   https://code.google.com/codejam/		      *
* ::::::::\ `--' /::::::::			@detail	Cookie Clicker							  *
*																						  *
*******************************************************************************************/

#include <fstream>
#include <vector>
#include <iostream>
#include <limits>
#include <string>

double TimeToX(double x, double r, int nf, double f){
	return (x / (r + nf*f));
}

double TimeToFarm(double c, double r, int nf, double f){
	return (c / (r+ nf*f));
}

int main(){
	FILE *in = freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);

	int T,numFarms = 0;
	double C, F, X, n = 0.0, rate = 2.0;
	float tC, tF, tX;

	fscanf(in,"%i", &T);
	
	for (int i = 0; i < T; i++){
		printf("Case #%d: ", i + 1);
		fscanf(in, "%f %f %f", &tC, &tF, &tX);
		C = tC;
		F = tF;
		X = tX;
		
		double time = 0;
		bool done = false;
		numFarms = 0;
		while (done == false){
			
			double ttx = TimeToX(X, rate, numFarms, F);
			double ttf = TimeToFarm(C, rate, numFarms, F);
			double ttxn = TimeToX(X, rate, numFarms+1, F);

			if (ttx < ttxn+ttf){
				time += TimeToX(X, rate, numFarms, F);
				std::cout.precision(15);
				std::cout << time;
				printf("\n");
				done = true;
			}

			else{
				time += TimeToFarm(C, rate, numFarms, F);
				numFarms++;
			}
		}
	}
	
	return 0;
}
