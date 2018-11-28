/*
 * StandingOvation.cpp
 *
 *  Created on: Apr 10, 2015
 *      Author: Rachel
 */

#include<iostream>
#include <fstream>
#include <string>
#include <sstream>
#include<cstdlib>
#include<string>
#include <sstream>
using namespace std;

int main(){
	ofstream outfile;
	outfile.open("out.txt");
	ifstream infile;
	infile.open("A-large.in", ifstream::in);

	if(!infile.is_open()) {		// Exit with return code 1, if file open is error.
			cout << "\n The file cannot be opened" << endl;
			return 1;
		}


	string line,temp;
	int c,s,t,a;
	getline(infile,line);
	c = atoi(line.c_str());
	for(int i=1;i<=c;++i){
		t=0;
		a=0;
		getline(infile,line);
		istringstream iss(line);
		iss>>temp;
		s=atoi(temp.c_str());
		iss>>temp;
		int* info=new int[s+1];
		for(int j=0;j<=s;++j){
			info[j]=temp[j]-'0';
			if(t<j){
				a+=j-t;
				t=j;
			}
			t+=info[j];
		}
		outfile<<"Case #"<<i<<": "<<a<<endl;
	}
		outfile.close();
		return 0;
}


