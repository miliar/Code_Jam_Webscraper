/*
 * A.cpp
 *
 *  Created on: 11 Apr 2016
 *      Author: xing
 */


#include <string.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>

//#define DEBUG_SOLVE
using namespace std;

char buff[3000];

void solve(int index){

	int letterCount[26];
	vector<int> result;
	memset(letterCount, 0, sizeof(int)*26);

	gets(buff);
#ifdef DEBUG_SOLVE
	cout<<"buff "<<buff<<endl;
#endif
	for(int i = 0;buff[i];i++){
		letterCount[ buff[i] - 'A' ]++;
	}

#ifdef DEBUG_SOLVE
	for(int i = 0;i<26; i++)
		cout<<(char)('A'+i)<<" "<<letterCount[i]<<endl;
#endif
	//8 3 2 4 5 0 1 6 7 9
	int count[10];
	count[8] = letterCount['G' - 'A'];
	letterCount['E' - 'A'] -= count[8];
	letterCount['I' - 'A'] -= count[8];
	letterCount['G' - 'A'] -= count[8];
	letterCount['H' - 'A'] -= count[8];
	letterCount['T' - 'A'] -= count[8];

	count[3] = letterCount['H' - 'A'];
	letterCount['T' - 'A'] -= count[3];
	letterCount['H' - 'A'] -= count[3];
	letterCount['R' - 'A'] -= count[3];
	letterCount['E' - 'A'] -= 2*count[3];

	count[2] = letterCount['T' - 'A'];
	letterCount['T' - 'A'] -= count[2];
	letterCount['W' - 'A'] -= count[2];
	letterCount['O' - 'A'] -= count[2];

	count[4] = letterCount['U' - 'A'];
	letterCount['F' - 'A'] -= count[4];
	letterCount['O' - 'A'] -= count[4];
	letterCount['U' - 'A'] -= count[4];
	letterCount['R' - 'A'] -= count[4];

	count[5] = letterCount['F' - 'A'];
	letterCount['F' - 'A'] -= count[5];
	letterCount['I' - 'A'] -= count[5];
	letterCount['V' - 'A'] -= count[5];
	letterCount['E' - 'A'] -= count[5];

	count[0] = letterCount['R' - 'A'];
	letterCount['Z' - 'A'] -= count[0];
	letterCount['E' - 'A'] -= count[0];
	letterCount['R' - 'A'] -= count[0];
	letterCount['O' - 'A'] -= count[0];

	count[1] = letterCount['O' - 'A'];
	letterCount['O' - 'A'] -= count[1];
	letterCount['N' - 'A'] -= count[1];
	letterCount['E' - 'A'] -= count[1];

	count[6] = letterCount['X' - 'A'];
	letterCount['S' - 'A'] -= count[6];
	letterCount['I' - 'A'] -= count[6];
	letterCount['X' - 'A'] -= count[6];

	count[7] = letterCount['S' - 'A'];
	letterCount['S' - 'A'] -= count[7];
	letterCount['E' - 'A'] -= count[7];
	letterCount['V' - 'A'] -= count[7];
	letterCount['E' - 'A'] -= count[7];
	letterCount['N' - 'A'] -= count[7];

	count[9] = letterCount['I' - 'A'];
	letterCount['N' - 'A'] -= count[9];
	letterCount['I' - 'A'] -= count[9];
	letterCount['N' - 'A'] -= count[9];
	letterCount['E' - 'A'] -= count[9];


	cout<<"Case #"<<index<<": ";
	for(int i = 0;i<10;i++){
		for(int j = 0;j<count[i];j++){
			cout<<i;
		}
	}
	cout<<endl;

}

int main(){
	int T;

	cin>>T;
	gets(buff);
	for(int i = 0;i<T;i++){
		solve(i+1);
	}

}
