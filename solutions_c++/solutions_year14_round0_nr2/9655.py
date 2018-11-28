// GCJ1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cstdlib>
#include <cstdio>
#define BUFFER_SIZE 512
#define C params[0]
#define F params[1]
#define X params[2]
#define MIN(X,Y) ((X) < (Y) ? (X) : (Y))

using namespace std;

double solver(double, double, double, double, double);

int _tmain(int argc, _TCHAR* argv[])
{
	FILE *f;
	char buffer[512];
	unsigned int T;
	double params[3];
	fopen_s(&f, "a.txt", "r");
	fgets(buffer, 512, f);
	T = atoi(buffer);
	//printf("%d\n", T); 
	for (unsigned int g = 0; g < T; g++){
		fgets(buffer, 512, f);
		unsigned int k = 0, l = 0;
		char *temp;
		temp = buffer;
		while (l<3){
			if (buffer[k] == ' ' || buffer[k] == '\0'){
				buffer[k] = '\0';
				params[l] = atof(temp);
				temp = buffer + k + 1;
				//printf("%f \n", params[l]);
				l++;
			}
			k++;
		}
		double t = 0;
		t=solver(C, F, X, 2.0, 0.0);
		printf("Case #%u: %.7f\n", g + 1, t);
	}
	fclose(f);
	return 0;
}



double solver(double c, double f, double x, double r, double balance){
	double time = -1;
	double buy, wait;
	if (x/r<(x+c)/(r+f)){
		return x / r;
	}
	else{
		//printf("%f | %f | %f |%f | %f \n", c, f, x, r, x/r);
		buy = solver(c, f, x, r + f, 0) + c / r;
		wait = x/r;
		return MIN(wait, buy);
	}
}