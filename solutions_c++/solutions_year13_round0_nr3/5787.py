// Codejam_3.xcpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fstream>
#include <iostream>
	
	using namespace std;

bool check(long a) {
	long b=0,temp=a; 
	while(a>0) { 
		b*=10;
		b+=a%10;
		a/=10; 
	}		
	return b==temp;
}
	
int main(int argc, char **argv)
{
	int num_test, i, j ;
	int count ;
	int min, max, sqrt_min, sqrt_max ;
	
	ifstream fin;
    fin.open("test.in");
    if (!fin.good()) throw "I/O error";
	
	ofstream fout ;
	fout.open("test.out");
	if (!fout.good()) throw "I/O error";
	
	fin >> num_test ;
	//printf("Number of test is %d\n", num_test);

	for (i=0; i<num_test; i++) {
		count = 0 ;
		fin >> min >> max ;
		//printf("range is %d %d \n", min, max);
		
		sqrt_min = (int) ceil( sqrt(min*1.0f) ) ;
		sqrt_max = (int) floor( sqrt(max*1.0f) ) ;
		//printf("range is %d %d \n", sqrt_min, sqrt_max);
	    
		for ( j = sqrt_min ; j <= sqrt_max ;  j++ ) {
			if ( check(j) && check (j*j) ) {
				count ++ ;
			}
		}
		//printf("%d\n", count);
		fout << "Case #" << i+1 <<": " << count << endl;
	}
	
	return 0;
	
}
