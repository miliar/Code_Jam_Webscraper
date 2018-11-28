#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <sstream>
#include <stdlib.h>
#include <stdio.h>
#include <iomanip>
using namespace std;
int main(int argc, char* argv[])
{
  string filename= argv[1];
  ifstream file(filename.c_str());
	file.precision(6);
	int numTests;
	int testCount=0;
	file>>numTests;
  while (file) {
		long double C,F,X;
  	string line;
		getline (file, line);
    if(!line.empty()){
       string buf;
       stringstream ss(line);
        vector <long double> nodes;
        while (ss >> buf) {
          long double num;
					num = atof(buf.c_str());
					//sscanf (buf.c_str(), "%lf", &num);
          nodes.push_back(num);
        }
				++testCount;
				C=nodes[0]; F=nodes[1]; X=nodes[2];
				double rate =2;
				double sum=0;
				while (X/rate > (C/rate + X/(rate+F))) { 
					sum += (C/rate);
					rate+=F;
				}
				sum+= X/rate;
				cout<<"Case #"<<testCount<<": "<<std::setprecision(12)<<sum<<endl;
				//cout<<std::setprecision(6)<<testCount<<" "<<std::setprecision(6)<<C<<" "<<std::setprecision(6)<<F<<" "<<std::setprecision(6)<<X<<endl;
			}
	}
  file.close();
}
