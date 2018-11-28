/*
 * coinjam.cc
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
#include <math.h>

using namespace std;

long long is_prime(long long x){
	for(long long i = 2; i <= sqrt(x); i++)
		if (x % i == 0)
			return i;
	return -1;
}

string converttobin(long long x){
	string s, newstring;

	while(x > 0){
		if (x % 2)
			s.append("1");
		else
			s.append("0");
		x = x >> 1;
	}
	for(int i = s.length()-1; i >= 0; i--)
		newstring.append(s.substr(i,1));

	return newstring;
}

long long calc(string s, int base){
	long long x = 0;

	for(int i = 0; i < s.length(); i++){
		if (s.at(i) == '1')
			x = x*base + 1;
		else
			x = x*base;
	}

	return x;
}

int main(int argc,char *argv[]){

	long long T;
	long long N, J;
	string s;
	string number;
	long long value, div;
	long long divs[11];
	int count;
	bool jam;
	ifstream fs(argv[1]);

	getline(fs, s);
	istringstream(s) >> T;
	getline(fs,s);
	istringstream(s) >> N >> J;
	count = 0;

		cout << "Case #1: " << endl;
		for (long long i = (pow(2,N-1) + 1); i < pow(2,N); i++){
			if (i % 2 == 0) continue;
			number = converttobin(i);
			jam = true;
			for(int j = 2; j <= 10; j++){
				value = calc(number, j);
				div = is_prime(value);
				if (div == -1){
					jam = false;
					break;
				}else{
					divs[j] = div;
				}
			}
			if (jam){
				count++;
				cout << number << " ";
				for(int j = 2; j <= 10; j++)
					cout << divs[j] << " ";
				cout << endl;
			}
			if (count == J) break;
		}
}
