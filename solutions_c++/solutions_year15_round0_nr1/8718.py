#include <iostream>
#include <stdlib.h>
#include <cstring>
#include <string>
#include <fstream>
using namespace std;

int main() {
	ifstream inputfile("A-large.in");
	if(inputfile.is_open()){
	string linenum;
	getline(inputfile, linenum);
	int num = strtol(linenum.c_str(), NULL, 10);
	//cout << num;	
	for (int i=0; i < num; i++) {
		int need = 0; int sum = 0;
		string line;
		getline(inputfile, line);
		char * cline = new char[line.length()+1];
		strcpy (cline, line.c_str());
		char * nlevel = strtok(cline, " ");
		char * audiance = strtok(NULL, " ");
		//cout << nlevel << ": " << audiance <<endl;
		sum = audiance[0] - '0';
		int nnlevel = strtol(nlevel, NULL, 10);
		for (int ii = 1; ii <= nnlevel; ii++){
			if (sum >= ii ) sum += (audiance[ii]-'0');
			else {	
				int need1 = ii -sum;
				need += need1;
				sum += ( (audiance[ii]-'0') + need1 );	
			}		
		}
		cout << "Case #" << (i+1) << ": " << need << endl;
	}
	}
	return 0;	
}
