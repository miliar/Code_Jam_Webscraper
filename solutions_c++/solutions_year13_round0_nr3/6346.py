#include <vector>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <memory.h>
#include <ctime>
#include <string>
#include <list>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <fstream>


using namespace std ;

bool Palindrom (long long) ;

int main ()
{
	ifstream inSt ("C-small-attempt0.in") ;
	try {
		if (inSt.fail ()) throw -1 ;
	}
	catch (int) {
		cerr << "Input file opeing failed." << endl ;
		exit (1) ;
	}
	ofstream outSt ("output.txt") ;
	try {
		if (outSt.fail ()) throw -1 ;
	}
	catch (int) {
		cerr << "Output file opeing failed." << endl ;
		exit (1) ;
	}

	int numT ;
	inSt >> numT ;

	long long A, B ;
	for (int i =0 ; i < numT ; i++) {
		inSt >> A >> B ;
		
		long long cnt =0 ;
		long double temp ;
		for (long long j =A ; j <= B ; j++) {
			if (!Palindrom (j)) continue ;
			
			temp =sqrt ((long double)j) ;
			if (temp > floor (temp)) continue ;

			if (!Palindrom ((long long)temp)) continue ;
			cnt++ ;
		}
		outSt << "Case #" << i+1 << ": " << cnt << endl ;
	}
	return 0 ;
}

bool Palindrom (long long x)
{
	int temp ;

	if (x < 10) return true ;
	else {
		bool TF =true ;
		vector <int> arr ;

		while (x) {
			temp =x %10 ;
			x /= 10 ;
			arr.push_back (temp) ;
		}

		for (int i =0 ; i < arr.size () /2 ; i++) 
			if (arr.at (i) != arr.at ((arr.size ()-1) -i)) {
				TF =!TF ;
				break ;
			}
		return (TF) ? true : false ;
	}
}