/*
Meredith Monticello
4/13/13
Code Jam 2013
Qualifications
Problem C
main.cpp
*/

#include <iostream>
#include <sstream>
#include <cstdlib>
#include <string>
#include <stdio.h>
#include <math.h>
using namespace std;

bool palin(long long cur);

int main(){
	int numLines;
	long long start;
	long long root;
	long long end;
	long cnt = 0;
	int line = 1;

	
	stringstream output;

	cin>>numLines;
		

	while(cin>>start){
		cin>>end;

		//calc all interval start to end
		for(start; start <= end; ++start){
			//find if palindrome
			if(palin(start)){
				//find if square root is palindrome
				//find square root of start
				root = (long long)sqrt((long double)start);

				if((root * root) == start && palin(root))
					cnt++; //add to cnt if both true			

			}		

		}

		output<<"Case #"<<line<<": "<<cnt<<"\n";
		line++;
		cnt = 0;
	}
	
	cout<<output.str();
	return 0;
}

bool palin(long long cur){
	string vic;
	ostringstream temp;

	temp<<cur;
	vic = temp.str();

	std::string::iterator it = vic.begin();
	std::string::iterator rit = vic.end();
	rit--;
	while(*it == *rit){
		++it;
		if(it == vic.end())
			return true;
		--rit;		
	}

	if(it == vic.end() || it == rit)
		return true;

	return false;
}