#include <stdio.h>
#include <iostream>
#include<fstream>
#include<algorithm>
#include <math.h>
#include <vector>
#include <string.h>

  using namespace std;


int main(int argc, char* argv[])
{
	ifstream fin;
	ofstream fout;
	fin.open(argv[1]);
	fout.open("test.out");
	int num_tests;
	fin>> num_tests ;

	
	long int A, B, K ;
    for ( int test_i =0 ; test_i < num_tests ; test_i++) {
		fin >> A >> B >> K  ;
		//int num  ;
		//num = 2&3 ;
		
		long int tmp_num ;
		long int count=0 ;
		
		for (long int i = 0 ; i< A; i++) {
			for (long int j = 0 ; j< B; j++) {
				if ( (i&j) < K ) {
					count++;
				}			
			}
		}
		fout << "Case #" << test_i+1 << ": " << count <<endl ;
		//cout << A <<" " << B<< "  "<< "  "<< K << " " << count << endl ;
    }
   
 
	fin.close();
	fout.close();
	
	return 0;
}