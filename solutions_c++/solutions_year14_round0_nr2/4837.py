#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <set>
#include <iterator>
#include <cstring>
#include <climits>
#include <cstdlib>
#include <cstdio>

using namespace std;

double EPS = 1E-8;
double C, F, X;
double totalTime;

string inFile = "B-small-attempt0.in";
string outFile = "B-small-attempt0.out";
FILE* in = NULL;
FILE* out = NULL;

// numFarms stands for the #farms currently
void calcTime(int numFarms, double numCookies)
{
	double ability = 2.0 + F*numFarms;
	double newAbility = ability+F;
	double timeNotBuy = (X-numCookies)/ability;
	double timeToBuy = (C-numCookies)/ability + X/newAbility;
	if( timeNotBuy < timeToBuy ){
		totalTime += timeNotBuy;
		return;
	}
	else{
		numFarms++;
		numCookies = 0;
		totalTime += (C-numCookies)/ability;
		calcTime(numFarms, numCookies);
	}
}

int main()
{
	if( !( in = fopen(inFile.c_str(), "r") ) )
		exit(-1);
	if( !( out= fopen(outFile.c_str(), "w") ) ){
		fclose(in);
		exit(-1);
	}

    int T;
	fscanf(in, "%d", &T);
	for(int t=0; t<T; t++)
	{
		fscanf(in, "%lf", &C);
		fscanf(in, "%lf", &F);
		fscanf(in, "%lf", &X);
		totalTime = 0;
		calcTime(0, 0);

		fprintf(out, "Case #%d: %.7lf\n", t+1, totalTime);
	}

	fclose(in);
	fclose(out);
	return 0;
}
