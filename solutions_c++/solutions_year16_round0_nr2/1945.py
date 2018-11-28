#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>

using namespace std;

int flip( string input ){
	int flips = 0;
	//cout << input << endl;
	while( input.find('-') != string::npos ){
		
		if( input[0] == '-' ){
			size_t lastMinus = input.find_last_of('-');
			//cout << "last minus : " << lastMinus << endl; 
			reverse(input.begin(), input.begin()+lastMinus+1);
			for( size_t i = 0; i <= lastMinus; i++ ){
				if( input[i] == '+' ) input[i] = '-';
				else input[i] = '+';
			}
			flips++;
		}
		
		else {
			size_t firstMinus = input.find('-');
			reverse(input.begin(), input.begin()+firstMinus-1);
			//cout << "first minus : " << firstMinus << endl;
			for( size_t i = 0; i < firstMinus; i++){
				if( input[i] == '+' ) input[i] = '-';
				else input[i] = '+';
			}
			flips++;
		}
		//cout << input << endl;
	}
	return flips;
}

int main(){
	int cases; cin >> cases;
	string pancakes;
	for(int i=1; i <= cases; i++ ){
		cin >> pancakes;
		printf("Case #%i: %i\n", i, flip(pancakes));
	}
	return 0;
}
