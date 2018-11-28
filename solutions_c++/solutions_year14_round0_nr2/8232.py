#include <stdio.h>
#include <iostream>
#include<fstream>
#include <math.h>  
#include<stdlib.h>
#include <iomanip>

  using namespace std;


int main(int argc, char* argv[])
{
	ifstream fin;
	ofstream fout;
	fin.open(argv[1]);
	fout.open("cookie.out");
	int num_tests ;
	int num_farms ;
	
	double C, F, X ;
	double total_t;
	
	fin>> num_tests ;
	for ( int test_i =0 ; test_i < num_tests ; test_i++) {
		total_t = 0 ;

		fin>> C >> F >> X ;
		num_farms = (int) ( ceil ( (max((double)0.0, ( (X-C)*F/C - 2 ))) / F ) );
		
		for (int i= 0; i< num_farms; i++) {
			total_t += C / ( 2+i*F ) ;
			//printf( "Data %d :%f, %d  %f\n", test_i, C, i, total_t) ;
		}		
		total_t += X/(num_farms * F+2);
		fout << "Case #" << test_i+1 << ": " << setiosflags(ios::fixed)<<setprecision(7)<< total_t <<endl ;
		//printf ("%f  %f  %f %d    %f\n", C, F, X, num_farms, total_t);
	
	}
	fin.close();
	fout.close();
	
	return 0;
}