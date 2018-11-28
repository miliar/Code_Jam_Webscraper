#include <iostream>
#include <fstream>
using namespace std ;

int main() {
	ifstream din("B-large.in") ;
	ofstream dout("ol2.txt") ;
	int t ;
	din >> t ;
	for(int i = 1 ; i <= t ; i ++) {
		char str[101] ;
		din >> str ;
		int pos , count = 0 ;
		up : 
		pos = -1 ;
		for(int j = 0 ; str[j] != '\0' ; j ++) {
			if(str[j] == '-') {
				pos = j ;
			}
		}
		if(pos == -1) {
			dout << "Case #" << i << ": " << count << endl ;
			goto down ;
		}
		else {
			count ++ ;
			for(int j = 0 ; j <= pos ; j ++) {
				if(str[j] == '+')
					str[j] = '-' ;
				else
					str[j] = '+' ;
			}
		}
		goto up ;
		down : {
		}
	}
	return 0 ;
}
