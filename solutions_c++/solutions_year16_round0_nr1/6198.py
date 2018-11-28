#include <iostream>
#include <fstream>
using namespace std;
bool digits[10];
int main(){ 
    ofstream fout("A.out"); 
	int n;
	cin >> n;
	long long input;
	for ( int i = 0 ; i < n ; i ++ ){
		cin >> input;
		for ( int j = 0 ; j < 10 ;j ++)
			digits[j] = false;
		if ( input == 0 ) {
			fout << "Case #" << i + 1 <<": INSOMNIA" << endl;
			continue;
		}
		bool shadiao = false;
		long long  ori = input;
		while ( !shadiao ){
			long long  module = input;
			while ( module > 0 ){
				int temp = module % 10;
				digits[temp] = true;
				module /= 10;
			}
			bool out = true;
			for ( int j = 0 ; j < 10 ;j ++)
				out = out && digits[j];
			if ( out ){
				fout << "Case #" << i + 1 <<": " << input << endl;
				shadiao = true;
			}
			input += ori;
		}
	}
	
	return 0;
}
