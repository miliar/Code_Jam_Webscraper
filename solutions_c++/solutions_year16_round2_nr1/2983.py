/*
 * phone.cc
 *
 *  Created on: Apr 30, 2016
 *      Author: maciek
 */

#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <set>
#include <iostream>
#include <list>
#include <map>


using namespace std;


int main(int argc,char *argv[]){

	long long T, N;
	string s;
	ifstream fs(argv[1]);
	int index, min, a;
	map<char,int> chars;
	int digits[10];
	char c;

	getline(fs, s);
	istringstream(s) >> T;
	for(int i = 0; i < T; i++){
		chars.clear();
		getline(fs,s);
		for(int j = 0; j <10; j++) digits[j] = 0;
 		for(int j = 0; j < s.length(); j++){
 			c = s.at(j);
 			if(c == 'Z') digits[0]++;
			if(c == 'U') digits[4]++;
			if(c == 'G') digits[8]++;
			if(c == 'X') digits[6]++;
			if(c == 'W') digits[2]++;
			chars[c]++;
 		}

 			chars['E']-=chars['Z'];
 			chars['R']-=chars['Z'];
 			chars['O']-=chars['Z'];

 			chars['F']-=chars['U'];
 			chars['O']-=chars['U'];
 			chars['R']-=chars['U'];

 			chars['E']-=chars['G'];
 			chars['I']-=chars['G'];
 			chars['H']-=chars['G'];
 			chars['T']-=chars['G'];

 			chars['S']-=chars['X'];
 			chars['I']-=chars['X'];

 			chars['T']-=chars['W'];
 			chars['O']-=chars['W'];

 			digits[1] = chars['O'];
 			digits[3] = chars['T'];
 			digits[5] = chars['F'];
 			digits[7] = chars['S'];

 			chars['N']-=chars['O'];
 			chars['N']-=chars['S'];

 			digits[9] = chars['N']/2;


 			cout << "case #" << i+1 << ": ";
 			for(int j = 0; j < 10; j++)
 				for(int k = 0; k < digits[j]; k++) cout << j;
 			cout << endl;
	}

}
