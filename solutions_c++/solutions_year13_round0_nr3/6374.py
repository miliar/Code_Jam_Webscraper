#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <vector>
#include <algorithm>    // std::sort
#include<cmath>

using namespace std;

#define in_file "C-small-attempt0.in"
#define out_file "C-small-attempt0.out"

void split(const string& s, char c, vector<string>& v){ //string tokenizer
	string::size_type i = 0;
	string::size_type j = s.find(c);
	while(j != string::npos){
		v.push_back(s.substr(i, j-i));
		i = ++j;
		j = s.find(c, j);
		if (j == string::npos) v.push_back(s.substr(i, s.length()));
	}
}

bool isPalin(int val){
	if(val<10)
		return true;
	if(val==1000)
		return false;
	if(val<100)
		return val%10==(val/10)%10;
	else
		return val%10==(val/100)%10;
}

void compute(int A, int B, int round){
	ofstream fout;
	fout.open(out_file, ios::app);
	if(fout.fail()){
		cerr<<"Cannot open file "<<out_file<<endl;
		exit(1);
	};
	double sqt = 0;
	int count=0;
	for(int i=A; i<=B; ++i){
		sqt = sqrt(i*1.0);
		if(abs(sqt-int(sqt))<0.00001){
			//it's a square
			if(isPalin(i) && isPalin(int(sqt)))
				++count;
		}
	}
	fout<<"Case #"<<round<<": "<<count<<endl;
}

void main(){
	ifstream fin;
	fin.open(in_file);
	string line;
	
	vector<string> v;
	int N=0;      //the number of test cases
	if(fin.fail()){
		cerr<<"Cannot open file "<<in_file<<endl;
		exit(1);
	};
	getline(fin,line);   //to get N
	if(line == "")
		return;
	N = atoi(line.c_str());
	int round = 1;
	int A=0, B=0;
	for(int i=0; i<N; ++i){
		//convert strings to board
		getline(fin, line);      //for the empty line
		split(line, ' ', v);
		A = atoi(v[0].c_str());
		B = atoi(v[1].c_str());
		compute(A, B, round++);
		v.clear();
	}
}
