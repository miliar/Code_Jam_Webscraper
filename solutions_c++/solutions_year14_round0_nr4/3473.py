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
	string prefix = "D-large";
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
		int n;
		infile>>n;
		vector<double> x,y;
		for(int j=0;j<n;j++) {
			double w;
			infile>>w;
			x.push_back(w);
		}
		for(int j=0;j<n;j++) {
			double w;
			infile>>w;
			y.push_back(w);
		}
		sort(x.begin(),x.end());
		sort(y.begin(),y.end());
		int ret1=0,ret2=0,idx=0;
		for(int j=0;j<n;j++) {
			if(x[j]>y[idx]) {
				ret1++;
				idx++;
			}
		}
		idx=0;
		for(int j=0;j<n;j++) {
			while(idx<n&&y[idx]<x[j]) idx++;
			if(idx>=n) ret2++;
			idx++;
		}
		outfile << "Case #" << (i+1) << ": " << ret1 << " " << ret2<< endl; 
	}
	cout<<"DONE"<<endl;
	string zzz;
	cin>>zzz;
	outfile.close();
	return 0;
}