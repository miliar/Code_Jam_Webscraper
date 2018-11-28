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
#include <vector>
#include <string.h>
#include<cstdlib>
#include<string>
using namespace std;

int main(){
	ofstream outfile;
	outfile.open("output.txt");
	ifstream infile;
	infile.open("A-small-attempt0.in", ifstream::in);

	if(!infile.is_open()) {		// Exit with return code 1, if file open is error.
			cout << "\n The file cannot be opened" << endl;
			return 1;
		}

	string line;
	int c,s,t,a;
	getline(infile,line);
	c = atoi(line.c_str());
	//cout<<"Cases =" <<c<<endl;
	for(int i=1;i<=c;++i){
		t=0;
		a=0;
		getline(infile,line);
		//cout<<"line "<<line<<endl;
		s=line[0]-'0';
		//cout<<"s="<<s<<endl;
		int* info=new int[s+1];
		for(int j=0;j<=s;++j){
			info[j]=line[j+2]-'0';
			//cout<<info[j]<<endl; //test
			if(t<j){
				//cout<<"add"<<endl;//test
				a+=j-t;
				t=j;
			}
			t+=info[j];
		}
		cout<<"Case #"<<i<<": "<<a<<endl; //test
		outfile<<"Case #"<<i<<": "<<a<<endl;

	}

		outfile.close();
		return 0;
}


