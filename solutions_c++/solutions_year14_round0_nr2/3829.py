#include <stdio.h>
#include <iostream>
#include <fstream>
#include<iomanip>

using namespace std;

int main()
{
	double T, C, F, X, x = 2, t = 0;
	ifstream input;
	ofstream output;
	input.open("input.in");
	output.open("output.txt");
	input>>T;

    for(int l = 1;l<=T;l++) {
        input>>C;
        input>>F;
        input>>X;


            while(t+X/x > t+(X/(x+F)+C/x)) {
                t = t + C/x;
                x = x + F;
            }

            t = t + X/x;

            output<<"Case #"<<l<<": "<<fixed<<setprecision(7)<<t<<"\n";


        t  = 0;
        x = 2;

    }

	input.close();
	output.close();
	return 0;
}

