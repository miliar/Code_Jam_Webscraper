#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
using namespace std;

ifstream inputFile;
ofstream outputFile;
string s;

void work(int p) {
	
	double c, f, x;
	double winTime;
	double buyTime;
	double actualTime = 0;
	double bestTime = 100000;
	double cps;
	int tomek = 1;
	const char *ss;
	getline(inputFile, s);
	ss = s.c_str();
	sscanf(ss,"%lf %lf %lf",&c, &f, &x);

	cps = 2;
	winTime = x/cps;
	while(tomek == 1)
	{
		winTime = x/cps;
		buyTime = c/cps;
		if(bestTime>actualTime+winTime)
		{
			bestTime = actualTime+winTime;
		}

		if(winTime > buyTime)
		{
			cps+=f;
			actualTime+=buyTime;
		}else{
			actualTime+=winTime;
			tomek = 0;
		}
		if(actualTime>bestTime) tomek = 0;
	}
	outputFile << std::fixed << std::setprecision(7) << "Case #" << p <<": " << bestTime << "\n";

    return;
}

int main() {
    int t; 
	int c = 1;
	inputFile.open("c:\\example.in",ios::in);
	outputFile.open("c:\\example.out", ios::out);
	getline(inputFile, s);
	const char *ss = s.c_str();
	sscanf(ss,"%d",&t);
    while(t--) {
        work(c);
		c++;
    }
    return 0;
}

