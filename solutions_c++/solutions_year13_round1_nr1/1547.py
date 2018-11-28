/*
 * a.cpp
 *
 *  Created on: 26-04-2013
 *      Author: Ock
 */

#include <fstream>

using namespace std;

int T;
int r,t;
ifstream scanner;
ofstream out;
int test;

void solve(){
	int spent = 2*r+1;
	int a=1;
	int num=0;
	while(t>=spent){
		t=t-spent;
		num++;
		spent=2*r+4*a+1;
		a++;
	}

	out << "Case #" << test <<": " << num << endl;
}


int main(){
	scanner.open("A-small-attempt0.in");
	out.open("output.txt");

	scanner >> T;
	for (int i = 1; i <= T; ++i) {
		test=i;
		scanner >> r >> t;
		solve();
	}

	return 0;
}



