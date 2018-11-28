//#include "stdafx.h"

#include <iostream>
#include <cstring>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;


vector <long long int> v;
vector<long long int>::iterator low, up;

bool isPalind( long long int n ) {

	/*stringstream ss;
	string str;
	ss << n;
	ss >> str;*/
	string str = "";
	while( n > 0 ) {
		str += (n%10)+'0';
		n /= 10;
	}
	for( int i = 0; i < str.length() / 2; i++ ) {
		if( str[i] != str[str.length()-i-1] ) return false;
	}
	return true;
}

int main() {

	//cout <<"hello problem 3.5" << endl;
	long long int t, a, b;
	for(long long int i = 1; i < 10000001; i++ ) {
		if( isPalind(i) && isPalind(i*i) ) {
			v.push_back(i*i);

		}
	}
	
	cin >> t;
	

	for( int k = 0; k < t; k++ ) {
		cin >> a >> b;
		low = lower_bound( v.begin(), v.end(), a ); 
		up = upper_bound( v.begin(), v.end(), b ); 
		cout << "Case #" << k+1 << ": "<< up-low << endl;
	}
		


	return 0;
}
