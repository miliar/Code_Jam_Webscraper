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

using namespace std;

int main()
{
	ifstream infile;
	string prefix = "A-small-attempt1";
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
		int row1,row2;
		infile>>row1;
		int b1[4][4],b2[4][4];
		for(int j=0;j<4;j++) for(int k=0;k<4;k++) { infile>>b1[j][k]; }
		infile>>row2;
		for(int j=0;j<4;j++) for(int k=0;k<4;k++) { infile>>b2[j][k]; }
		row1--;
		row2--;
		bool found=false;
		for(int j=0;j<4;j++) for(int k=0;k<4;k++) if(b1[row1][j]==b2[row2][k]) found=true;
		if(!found) {
			outfile << "Case #" << (i+1) << ": " << "Volunteer cheated!" << endl; 
			continue;
		}
		string ret="";
		vector<int> possible;
		for(int col1=0;col1<4;col1++) for(int col2=0;col2<4;col2++) {
			if(b1[row1][col1]==b2[row2][col2]) possible.push_back(b1[row1][col1]);
		}
		if(possible.size()==0) ret="Volunteer cheated!";
		else if(possible.size()>1) ret="Bad magician!";
		else {
			ostringstream oss;
			oss << possible[0];
			ret=oss.str();
		}
		outfile << "Case #" << (i+1) << ": " << ret << endl; 
	}
	cout<<"DONE"<<endl;
	string zzz;
	cin>>zzz;
	outfile.close();
	return 0;
}