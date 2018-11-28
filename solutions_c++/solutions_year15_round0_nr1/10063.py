#include <iostream>
#include <fstream>
#include <cstdlib>
using namespace std;

int main(int argc, char** argv) { 
	//printf ("Hello\n");	
	ifstream fin;   
	string filename;
 	filename = argv[1];

	fin.open(filename.c_str());  // Convert to C-string and open it.

	int test_num, s_max;	
	string s_level ;
	int s_i,total_stand, num_need ;
	
	
	fin >> test_num ;
	
	
	
	 ofstream myfile;
	 myfile.open ("test.out");


	
	for (int test_i = 0; test_i<test_num;  test_i++ )  {
	
		fin >> s_max;
		fin >> s_level;
		
		s_i =0 ;
		total_stand  = 0 ;
		num_need = 0 ;
		for ( int i=0; i < (s_max+1); i++ )  {
			s_i = (s_level[i]-'0') ;	
			
			if ( i <= total_stand ) {
				total_stand += s_i ;			
			} else {
				if (s_i!=0) {
					num_need += 	(i - total_stand) ;		
					total_stand += s_i+num_need ;
				}
			}
			//cout <<  num_need << s_i << i << total_stand << "xx" ;
		}
		
		//cout <<  num_need << endl ;
		myfile << "Case #" << (test_i+1) << ": " << num_need<< endl;

		
	}
	
	myfile.close();
	
	return EXIT_SUCCESS ;
}

