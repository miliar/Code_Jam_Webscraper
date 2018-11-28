/*
 * pancake_revange.cc
 *
 *  Created on: Apr 9, 2016
 *      Author: maciek
 */

#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <set>
#include <iostream>

using namespace std;

string reverse(string s){
	string newstr;

	for(int i = s.length()-1; i >= 0; i--)
		if (s.at(i) == '+')
			newstr.append("-");
		else
			newstr.append("+");

	return newstr;
}

string handlehead(string s){

	string newstr;

	int i = 0;
	while(s.at(i) == '+') i++;
	for(int j = 0; j < i ; j++)
		newstr.append("-");
	for(int j = i; j < s.length(); j++)
		newstr.append(s.substr(j,1));

	return newstr;
}

long flips(string s){

	string newstr;

	if(s.find('-',0) == string::npos)
		return 0;
	else if(s.find('+',0) == string::npos)
		return 1;
	else if (s.at(s.length()-1) == '+')
		return flips(s.substr(0,s.length()-1));
	else if (s.at(0) == '-')
		return 1 + flips(reverse(s));
	else if (s.at(0) == '+')
		return 1 + flips(handlehead(s));

	return 0;

}

int main(int argc,char *argv[]){

	long long T;
	string s;
	ifstream fs(argv[1]);

	getline(fs, s);
	istringstream(s) >> T;
	for(int i = 0; i < T; i++){
		getline(fs,s);
		cout << "Case #" << i+1 << ": " << flips(s) << endl;
	}
}
