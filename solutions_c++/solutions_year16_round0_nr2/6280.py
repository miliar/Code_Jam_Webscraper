#include <iostream>
#include <fstream>
using namespace std;
int main(){ 
    ofstream fout("B.out"); 
	int n;
	cin >> n;
	string input;
	for ( int i = 0 ; i < n ; i ++ ){
		cin >> input;
		int len = input.size();
		int sum = 0;
		bool flag = false;
		while ( !flag ){
			bool out = true;
			for ( int j = 0 ; j < len ; j ++ ){
				out = out && (input[j] == '+');
			}
			if ( out ) {
				fout << "Case #" << i + 1 <<": " << sum << endl;
				flag = true;
			}
			int j = 0;
			bool up;
			if ( input[0] == '+' ) up = true;
				else up = false;
			if ( up ){
				while(input[j] == '+'){
					j ++;
					if ( j == len ) break;
				}
				for ( int k = 0 ; k < j ; k ++ ){
					input[k] = '-';
				}
				sum ++;
			} else {
				while(input[j] == '-'){
					j ++;
					if ( j == len ) break;
				}
				for ( int k = 0 ; k < j ; k ++ ){
					input[k] = '+';
				}
				sum ++;
			}
		}
	}
	
	return 0;
}
