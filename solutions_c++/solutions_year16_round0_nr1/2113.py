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

ifstream ifs( "data.txt" );
ofstream ofs("result.txt");
int main( void ) {


	int T;
	cin >> T;
	for( int i = 0; i < T; i++ ) {
		ofs << "Case #" << i+1 << ":";
		solve();
	}

	return 0;
}


void solve() {

	int N;
	bitset<10> flag(0);
	cin >> N;


	if( N == 0 ) {
		ofs << "INSOMNIA" << endl;
		return;
	}

	for(int i = 1;;i++ ) {
		stringstream ss;
		ss << i*N;
		for(int j=0; j<ss.str().length(); j++ ) {
			flag.set(ss.str()[j]-'0');
		}
		if( flag.count() == 10 ) {
			ofs << i*N << endl;
			break;
		}
	}

	


}