//============================================================================
// Name        : A.cpp
// Author      : Yul Obraz
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <istream>
#include <fstream>
#include <string>
#include <cstdio>
#include <deque>
using namespace std;

string calc(string target){
	deque<char> sorted;

	for(std::string::iterator it = target.begin(); it != target.end(); ++it){
		if(sorted.begin()[0]<=it[0]){
			sorted.push_front(it[0]);
		}else{
			sorted.push_back(it[0]);
		}
	}
	std::string output_string(sorted.begin(), sorted.end());
	return output_string;
}
int main(int argc,char *argv[]) {
	freopen(argv[1],"r",stdin);
	freopen(argv[2],"w",stdout);
	int tests;
	cin >> tests;
	for(int i=0; i<tests; i++){
		string target;
		cin>>target;
		string result = calc(target);
		cout << "Case #"<< (i+1)<<": "<<result<< endl;
	}
	return 0;
}
