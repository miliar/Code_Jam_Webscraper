/*
 * lastword.cc
 *
 *  Created on: Apr 16, 2016
 *      Author: maciek
 */

#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <set>
#include <iostream>
#include <list>


using namespace std;


int main(int argc,char *argv[]){

	long long T;
	string s;
	ifstream fs(argv[1]);
	list<char> word;

	getline(fs, s);
	istringstream(s) >> T;
	for(int i = 0; i < T; i++){
		getline(fs,s);
		word.clear();
		word.push_back(s.at(0));
		for(int a = 1; a< s.length(); a++){
			if (s.at(a) >= word.front())
				word.push_front(s.at(a));
			else
				word.push_back(s.at(a));
		}
		cout << "Case #" << i+1 << ": ";
		list<char>::iterator it;
		for(it = word.begin(); it != word.end(); it++)
			cout << *it;
		cout << endl;
	}
}

