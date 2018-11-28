 //============================================================================
// Name    	: google.cpp
// Author  	: Maciej Michalak
// Version 	:
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <list>
using namespace std;

double timeCost(double forNow, double cost, double income, double C, double F, double X){
	double houseCost=C/income;
	double fullCost =X/(income+F)+houseCost+forNow;
	if(cost<fullCost) return cost;
	else return timeCost(forNow+houseCost, fullCost, income+F, C, F, X);	
}

int main() {

    ifstream f;
    ofstream ff;
    
    f.open("test.in");
    ff.open("test.out");
    
    int num;
    f>>num;
    
    ff.precision(7);
    for(int i=0; i<num; i++){
    	double C, F, X;
    	f>>C;
    	f>>F;
    	f>>X;
    	ff<<"Case #"<<i+1<<": "<<timeCost(0,X/2.0, 2.0, C, F, X)<<endl;
    }
    return 0;
}



