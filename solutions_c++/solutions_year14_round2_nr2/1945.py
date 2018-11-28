//============================================================================
// Name        : q2.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <sstream>
#include <vector>
#include <stack>
#include <map>
#include <bitset>

using namespace std;

int main() {

	ifstream input("/home/user/workspace_cpp/q2/src/B-small-attempt0.in");
	ofstream output("/home/user/workspace_cpp/q2/src/output.txt");

	string line;
	int casenum;
	input >> casenum;
	int a=0;
	int b=0;
	int k=0;

	for (int i=0;i<casenum;i++){

		input >>a;
		input >>b;
		input >>k;

		int res=0;
		for (int ii=0;ii<a;ii++){
			for (int jj=0;jj<b;jj++){
				int cc = ii&jj;

				if (cc <k){
					res++;
				}
			}
		}


		output << "Case #" << i+1 << ": " << res << endl;
		//cout<< "Case #" << i+1 << ": " << res << endl;
	}

	input.close();
	output.close();

	return 0;
}
