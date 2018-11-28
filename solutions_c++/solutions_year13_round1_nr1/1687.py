#include <iostream>
#include <sstream>
#include <fstream>
#include <string>

using namespace std;

int func(int k, int r){
	int result = 0;
	for (int i=1; i<=k; i++){
		result += 2*r+4*i-3;
	}
	return result;
}

void solve(int r, int t, ofstream& output, int casenum){
	cout<<"r="<<r<<", t="<<t<<endl;
	int k=2;
	for (; k<=t; k++){
		if (func(k, r)>t)
			break;
	}
	k--;
	output<<"Case #"<<casenum<<": "<<k<<endl;
}

int main(){
	ifstream input("input.txt");
	ofstream output;
	output.open("output.txt");
	if (input.is_open()){
		int numcases = -1;
		int casenum = 1;
		
		while (input.good()){
			string line;
			getline(input, line);
			if (numcases == -1){
				istringstream iss(line);
				iss>>numcases;
				continue;
			}
			
			//cout<<"line: "<<line<<endl;
			
			if (line.size()==0){
				continue;
			}
			
			int r, t;
			istringstream iss(line);
			iss>>r;
			iss>>t;
			solve(r,t,output,casenum++);
			
		}
	}
	input.close();
	output.close();
	return 0;
}

