#ifndef _HELPER_FUNCS_H_
#define _HELPER_FUNCS_H_

// === standard lib includes

//C libs
#include <cstdio>
#include <cstdlib>
#include <ctime>

//I/O
#include <cstdio>
#include <iostream>
#include <fstream>

//STL
#include <algorithm>
#include <bitset>
#include <set>
#include <list>
#include <stack>
#include <map>
#include <vector>

using namespace std;

//GMP bignum
//#include <gmp.h>

// === STL displaying helpers
template <class T>
ostream& operator << ( ostream &os, const vector<T> &vec )
{
	cout << '[\n';
	for( int i=0; i<vec.size(); i++ ) {
		cout << vec[i] << '\n';
	}
	cout << ']\n';
	return os;
}

float randreal()
{
	return (float)rand()/RAND_MAX;
}

//check if a integer is power of 2
template <typename T>
bool bIs2N( T n )
{
	if( !n ) return false;
	return ~( (bool)(n & (n-1)) );
}

template <typename T>
T& Min( T& a, T& b )
{
	return a>b? b : a;
}

template <typename T>
T& Max( T& a, T& b )
{
	return a>b? a : b;
}

// === defines

typedef unsigned int uint;
typedef char byte;
typedef unsigned char ubyte;

#endif