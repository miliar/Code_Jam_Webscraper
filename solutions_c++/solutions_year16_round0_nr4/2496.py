#include <iostream>
#include <fstream>
using namespace std ;

int main() {
	ifstream din("D-small-attempt0.in") ;
	ofstream dout("o4.txt") ;
	int t ;
	din >> t ;
	for(int i = 1 ; i <= t ; i ++) {
		int k , c , s ;
		din >> k >> c >> s ;
		dout << "Case #" << i << ":" ;
		for(int j = 1 ; j <= k ; j ++) 
			dout << " " << j ; 
		dout << endl ;
	}
	return 0 ;
}
