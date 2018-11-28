/*
 * fractiles.cc
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


long long pow(long long x, long long y){
	long long m = 1;
	for(long long i = 1; i <= y; i++)
		m*=x;
	return m;
}

int main(int argc,char *argv[]){

	long long T,C,K,S;
	string s;
	ifstream fs(argv[1]);
	long long pos[1000];

	getline(fs, s);
	istringstream(s) >> T;
	for(int i = 0; i < T; i++){
		getline(fs,s);
		istringstream(s) >> K >> C >> S;
		for(long long j = 1; j <= K; j++)
			pos[j] = j;
		for(long long l = 2; l <= C; l++)
			for(long long j = 1; j <= K; j++)
				pos[j] = (j-1)*pow(K,l-1) + pos[j];

		cout << "Case #" << i+1 << ": ";
		for(long long j = 1; j <= K; j++)
			cout << pos[j] << " ";
		cout << endl;

	}

}
