#include <iostream>
#include <fstream>
using namespace std ;

int main() {
	ifstream din("A-large.in") ;
	ofstream dout("ol1.txt") ;
	int t ;
	din >> t ;
	for(int i = 1 ; i <= t ; i ++) {
		int n , arr[10] = {0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0} ;
		din >> n ;
		if(n == 0) {
			dout << "Case #" << i << ": " << "INSOMNIA\n" ;
			continue ;
		}
		int fac = n ;
		while(1) {
			int temp = n ;
			while(temp != 0) {
				arr[temp % 10] = 1 ;
				temp /= 10 ;
			}
			int j = 0 ;
			for( ; j < 10 ; j ++) {
				if(arr[j] == 0)
					break ;
			}
			if(j == 10) {
				dout << "Case #" << i << ": " << n << endl ;
				break ; 
			}
			n = n + fac ;
		}
		
	}
	return 0 ;
}
