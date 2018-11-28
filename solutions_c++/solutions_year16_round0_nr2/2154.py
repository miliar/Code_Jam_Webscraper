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

typedef long long int ll;

ifstream ifs( "data.txt" );
ofstream ofs("result.txt");

int main( void ) {


	int T;
	ifs >> T;
	for( int i = 0; i < T; i++ ) {
		ofs << "Case #" << i+1 << ": ";
		solve();
	}

	return 0;
}


void solve() {

	string str;
	ifs >> str;

	int mcnt = 0, pcnt = 0;

	for( int i = 0; i + 1< str.length(); i++ ) {
		if( str[i] == '+' && str[i+1] == '-' )
			mcnt ++;
		if( str[i] == '-' && str[i+1] == '+' )
			pcnt ++;
	}


	if( str[0] == '+' )
		pcnt ++;
	else
		mcnt ++;

	if(str[str.length()-1] == '+' )
		pcnt --;

	ofs << mcnt + pcnt << endl;
}