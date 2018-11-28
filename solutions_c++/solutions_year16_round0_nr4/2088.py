#include <fstream>
#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <set>
#include <math.h>
#include <bitset>
using namespace std;

void solve();

typedef unsigned long long int ll;

ifstream ifs( "data.txt" );
ofstream ofs("result.txt");

int main( void ) {


	int T;
	ifs >> T;
	for( int i = 0; i < T; i++ ) {
		ofs << "Case #" << i+1 << ":";
		solve();
	}

	return 0;
}


void solve() {
	int K, C, S;
	ifs >> K >> C >> S;
	for( int i = 0; i < S; i++ )
		ofs << " " << i+1;
	ofs << endl;
}