// 2014.cpp : Defines the entry point for the console application.
//


#include <iostream>
#include <sstream>
#include <iterator>
#include <string>
#include <vector>
#include <set>
#include <stdio.h>

using namespace std;

class Cookie {
private:
	double C, F, X;

public:
	void parseData() {
		string line;
		
		cin >> C >> F >> X;
		getline(cin, line);
	}

	double solve() {
		double t = X/2;
		int farmC = 0;
		double farmT = 0;
		double curP = 2;
		while (1) {
			double x = C/curP;
			farmT += x;
			++farmC;
			curP += F;
			double curTime = farmT + X/curP;
			if (curTime >=t) return t; else t = curTime;
		}
	}
};

int main(int argc, char* argv[])
{	
	string line;
	int count;

	cin >> count;
	getline(cin, line);

	for (int i = 1; i <= count; ++i) {
		Cookie ck;
		ck.parseData(); 
		cout.precision(7);
		cout.fixed;
		printf ("Case #%d: %.7f\n", i, ck.solve());
	}
	
	return 0;
}

