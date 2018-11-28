#include <iostream>
#include <vector>
#include <string>
#include <string.h>
#include <stdio.h>
#include <sstream>
#include <algorithm>
#include <stdlib.h>
#include <iomanip>
#include <math.h>

using namespace std;

int main(){
	string num_tests;
	int inum_tests;
	string input="";
	getline(cin,num_tests);
	inum_tests=atoi(num_tests.c_str());
	for(int i = 0; i<inum_tests;i++)
	{
		cout << "Case #" << i+1 << ": ";
		getline(cin,input);
		istringstream s1(input);
		string sC,sF,sX;
		double C,F,X;
		getline(s1,sC,' ');
		getline(s1,sF,' ');
		getline(s1,sX,' ');
		C=atof(sC.c_str());
		F=atof(sF.c_str());
		X=atof(sX.c_str());
		double rate=2.0;
		double prev_time=X/rate;
		double farm_costs=0.0;
		while(true){
			double time_taken=C/rate+farm_costs;
			double new_rate=rate+F;
			double new_time=time_taken+X/new_rate;
			if(prev_time<new_time){
				//It can only get worse from here,
				//abort and print
				break;
			} else {
				//otherwise set the new values and
				//try with the next set
				rate=new_rate;
				prev_time=new_time;
				farm_costs=time_taken;
			}
		}
		//double round = floorf(prev_time * 10000000 +0.5) / 10000000;
		cout << fixed << setprecision(10) << prev_time << endl;
	}
}
