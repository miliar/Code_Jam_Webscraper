//============================================================================
// Name        : .cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <cmath>
#include <sstream>
using namespace std;

bool isPal(long long num){
	int sz;
	string tmp;
	stringstream ss;
	ss << num;
	ss >> tmp;
	sz = tmp.size();
	for(int i=0; i<sz/2; i++){
		if(tmp[i]!=tmp[sz-1-i])
			return false;
	}
	return true;
}

int fu(long long A, long long B){
	long long tmpA = sqrt((double)A);
	long long tmpB = sqrt((double)B);
	int cntr = 0;
	for(long long i = tmpA; i<=tmpB; i++){
		if((i*i)>=A && (i*i)<=B && isPal(i))
			cntr += isPal(i*i);
	}
	return cntr;
}

int main() {

#ifndef ONLINE_JUDGE
	freopen("C-small-attempt0.in","rt",stdin);
	freopen("out.txt","wt",stdout);
#endif

	int T;
	long long A,B;

	cin >> T;
	for(int t=1; t<=T; t++){
		cin >> A >> B;
		cout << "Case #" << t << ": ";
		cout << fu(A,B) << endl;
	}

	return 0;
}
