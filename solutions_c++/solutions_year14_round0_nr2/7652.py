//============================================================================
// Name        : googlejam.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

#include <iostream>
#include <fstream>
#include <iomanip>      // std::setprecision

using namespace std;
double farm(double C, double F,double X, double R) {
    double ttime = 0;

	while (X / R - C / R > X / (R+F)) {
		if(X / R < C / R) {
			return X / R;
		}
		double ntime = X / (R+F);
		if(X / R - C / R < ntime) {
			return X / R;
		}
		ttime += C / R;
		R = R+F;
	}
	ttime += X / R;

    return ttime;
}


int main()
{
    ifstream myReadFile;
    myReadFile.open("input.txt");

    int length = 0;
    myReadFile >> length;

    int caseNum = 0;
    while(!myReadFile.eof() && caseNum < length) {
        caseNum++;

        double C;
        double F;
        double X;
        myReadFile >> C;
        myReadFile >> F;
        myReadFile >> X;

        cout << "Case #" << caseNum << ": ";
        cout << std::setprecision(10)  << farm(C,F,X,2.0) << endl;
    }

    return 0;
}
