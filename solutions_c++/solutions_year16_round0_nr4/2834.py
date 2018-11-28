#include <iostream>
#include <fstream>

using namespace std ;

int main() {
	
	ifstream cin("input4.txt") ;
	ofstream cout("output4.txt") ;
	long long int T;
	
	cin >> T  ;
	
	for(int k = 1 ; k <= T ; k ++) {
		int g , c , s ;
		cin >> g >> c >> s ;
		cout << "Case #" << k << ":" ;
		for(int j = 1 ; j <= g ; j ++){
		
			cout << " " << j ; 
		}
		cout << endl ;
	}
	
	
	
}

