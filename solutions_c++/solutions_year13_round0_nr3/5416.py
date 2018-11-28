/*
 * =====================================================================================
 *
 *       Filename:  a.cc
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  04/12/2013 05:22:10 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Martin Cai (MC), mrtncai@gmail.com
 *   Organization:  
 *
 * =====================================================================================
 */


#include	<stdlib.h>
#include <iostream>
#include <sstream>

using namespace std;

bool palindrome(const string &str){
	for ( unsigned int i = 0; i < str.length() / 2; i ++ ) {
		if(str[i] != str[str.length() - 1 - i])
			return false;
	}
	return true;
}

/* 
 * ===  FUNCTION  ======================================================================
 *         Name:  main
 *  Description:  
 * =====================================================================================
 */
	int
main ( int argc, char *argv[] )
{
	// precomputation
	int results[18]; 
	int count = 0;
	// 1 digit
	for ( int i = 1; i <= 9; i ++ ) {
		stringstream ss;
		ss << i * i;
		if(palindrome(ss.str()))
				results[count++] = i * i;
	}
	for ( int i = 11; i <= 99; i += 11 ) {
		stringstream ss;
		ss << i * i;
		if(palindrome(ss.str()))
				results[count++] = i * i;
	}

//	for ( int i = 0; i < count; i ++ ) {
//		cout << results[i] << " ";
//	}

	// take input
	int T;
	cin >> T;
	for ( int i = 0; i < T; i ++ ) {
		cout << "Case #" << (i+1) << ": ";
		int a, b;
		cin >> a >> b;

		int j, k, l = 0 ;
		for ( j = 0; j < count; j ++ ) {
			if(a <= results[j]) {
//				if(a == results[j]) l = 1;
				break;
			}
		}
//		cout << "j " << j ;
		for ( k = j; k < count; k ++ ) {
			if(b <= results[k]){
				if(b == results[k]) l = 1;
				break;
			}	
		}
//		cout << ", k " << k << endl;

		cout << (k - j + l) << endl;
	}
	return EXIT_SUCCESS;
}				/* ----------  end of function main  ---------- */
