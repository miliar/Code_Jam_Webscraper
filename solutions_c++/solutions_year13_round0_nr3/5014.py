/*
 * main.cpp
 *
 *  Created on: 2013-04-13
 *      Author: ronanrmo
 */

#include <iostream>
#include <fstream>
#include <string.h>
#include <map>
#include <vector>
#include <cmath>
#include <list>
#include <string>
#include <sstream>


using namespace std;

typedef unsigned long long ui64;

bool ispalindrome(ui64 n){
	stringstream x;
    x << n;
	string p = x.str();

	int i = 0;
	int e = p.length()-1;

	while(i <= e){
		if(p[i] != p[e])
			return false;
		i++;
		e--;
	}
	return true;
}

int fair_square(ui64 ii, ui64 ee){
	ui64 i = ceil(sqrt(ii));
	ui64 e = sqrt(ee);
	int count = 0;
	while(i<=e){
		if(ispalindrome(i*i) && ispalindrome(i)) count++;
		i++;
	}
	return count;
}



int main(int argc, char **argv)
{
	istream &in  = (argc>1)?*(new ifstream(argv[1])):cin;
	ostream &out = (argc>2)?*(new ofstream(argv[2])):cout;

	int T;
	in >> T;

	for(int t=0; t<T; t++){
		ui64 i, e;

		in >> i >> e;

		int count = fair_square(i,e);

		out << "Case #" << t+1 << ": " << count << endl;
	}

	return 0;
}



