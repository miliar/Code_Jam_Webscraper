#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <fstream>
#include <set>
#include <iomanip>

using namespace std;

int main(){
	ifstream ifile("B-small-attempt0.in");
	string casesStr;
	getline(ifile, casesStr);
	stringstream cases_ss(casesStr);
	int numCases;
	cases_ss >> numCases;
	for(int i = 0;i<numCases;i++){
		cout << "Case #" << (i+1) << ": ";
		string paramString;
		getline(ifile, paramString);
		stringstream param_ss(paramString);
		double c, f, x;
		param_ss >> c;
		param_ss >> f;
		param_ss >> x;
		double currentRate = 2;
		double seconds = 0;
		double cookies = 0;
		while(true){
			if((x-c)/currentRate <= x/(f+currentRate)){
				seconds += x/currentRate;
				break;
			}
			else {
				seconds += c/currentRate;
				currentRate += f;
			}
		}
		cout << fixed;
    	cout << setprecision(7);
		cout << seconds << endl;
	}
}