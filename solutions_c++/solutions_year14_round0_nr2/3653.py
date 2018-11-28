#include "stdafx.h"
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <math.h>
#include <map>
#include <set>
#include <algorithm>
#include <iomanip> 

using namespace std;

int main()
{
	ifstream infile;
	string prefix = "B-large";
	//string prefix = "practice";
	infile.open(prefix + ".in");
	ofstream outfile(prefix + ".out");
	int cases;
	if (infile.is_open()) {
		infile>>cases;
	}
	else {
		return 0;
	}
	for(int i=0;i<cases;i++) {
		double C,F,X;
		infile>>C>>F>>X;
		double ret=X/2;
		double t=0.0;
		double farms=0;
		for(;;) {
			t+=C/(2.0+farms*F);
			farms++;
			if(t+X/(2.0+farms*F)<ret) {
				ret=t+X/(2.0+farms*F);
			}
			else break;
		}
		outfile << "Case #" << (i+1) << ": " << setprecision(20) << ret << endl; 
	}
	cout<<"DONE"<<endl;
	string zzz;
	cin>>zzz;
	outfile.close();
	return 0;
}