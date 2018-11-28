#include <iostream>
#include <fstream>
using namespace std;
int number[10];
int let[26];
int main(){ 
    ofstream fout("A.out"); 
	int n;
	cin >> n;
	string input;
	for ( int i = 0 ; i < n ; i ++ ){
		cin >> input;
		for ( int j = 0 ;  j < 10 ; j ++ )
			number[j] = 0;
		for ( int j = 0 ;  j < 26 ; j ++ )
			let[j] = 0;
		for ( int j =  0 ; j < input.length() ; j ++ ){
			let[input[j] - 65] ++;
		}
		number[0] += let[25];
		let[4] -= let[25];
		let[17] -= let[25];
		let[14] -=let[25];
		let[25] = 0;
		number[2] = let[22];
		let[19] -= let[22];
		let[14] -= let[22];
		let[22] = 0;
		number[4] += let[20];
		let[5] -= let[20];
		let[14] -= let[20];
		let[17] -= let[20];
		let[20] = 0;
		number[6] += let[23];
		let[18] -= let[23];
		let[8] -= let[23];
		let[23] = 0;
		number[8] += let[6];
		let[4] -= let[6];
		let[8] -= let[6];
		let[7] -= let[6];
		let[19] -= let[6];
		let[6] = 0;
		number[1] = let[14];
		let[13] -= let[14];
		let[4] -= let[14];
		let[14] = 0;
		number[3] = let[7];
		let[19] -= let[7];
		let[17] -= let[7];
		let[4] -= 2*let[7];
		let[7] = 0;
		number[5] = let[5];
		let[21] -= let[5];
		number[7] = let[21];
		let[13] -= let[21];
		number[9] = let[13] / 2;
		

		fout << "Case #" << i + 1 <<": " ;
		for ( int j = 0 ; j < 10 ; j ++ )
			for (int k = 0 ; k < number[j] ; k ++ )fout << j;
		fout << endl;
	

	}
	
	return 0;
}
