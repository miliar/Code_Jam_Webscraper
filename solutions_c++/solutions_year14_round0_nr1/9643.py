#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <fstream>
#include <set>

using namespace std;

int main(){
	ifstream ifile("A-small-attempt2.in");
	string casesStr;
	getline(ifile, casesStr);
	stringstream cases_ss(casesStr);
	int numCases;
	cases_ss >> numCases;
	for(int i = 0;i<numCases;i++){
		cout << "Case #" << (i+1) << ": ";
		string rowNumStr1;
		getline(ifile, rowNumStr1);
		stringstream rn1_ss(rowNumStr1);
		int rowNum1;
		rn1_ss >> rowNum1;
		string row1Str;
		for(int j = 0;j<rowNum1;j++){
			getline(ifile, row1Str);
		}
		stringstream r1str_ss(row1Str);
		set<int> s1;
		for(int j = 0;j<4;j++){
			int g;
			r1str_ss >> g;
			s1.insert(g);
		}
		for(int j = rowNum1;j<4;j++){
			getline(ifile, row1Str);
		}
		string rowNumStr2;
		getline(ifile, rowNumStr2);
		stringstream rn2_ss(rowNumStr2);
		int rowNum2;
		rn2_ss >> rowNum2;
		string row2Str;
		for(int j = 0;j<rowNum2;j++){
			getline(ifile, row2Str);
		}
		stringstream r2str_ss(row2Str);
		int count = 0;
		int possibility = 0;
		for(int j = 0;j<4;j++){
			int g;
			r2str_ss >> g;
			if(!(s1.insert(g).second)){
				possibility = g;
				// cout << possibility << endl;
				count++;
			}
		}
		for(int j = rowNum2; j < 4;j++){
			getline(ifile, row2Str);
		}
		if(count == 0) cout << "Volunteer cheated!" << endl;
		else if(count > 1) cout << "Bad magician!" << endl;
		else cout << possibility << endl;
	}
}