#include <stdio.h>
#include <iostream>
#include<fstream>

  using namespace std;


int main(int argc, char* argv[])
{
	ifstream fin;
	ofstream fout;
	fin.open(argv[1]);
	fout.open("magician.out");
	int num_tests, row1, row2 ;
	int row1_num[4], row2_num[4], tmp_num[4] ;
	fin>> num_tests ;
   
    for ( int test_i =0 ; test_i < num_tests ; test_i++) {
		fin>> row1 ;
		for ( int i =0 ; i < row1; i++) {
			fin>> row1_num[0] >>  row1_num[1] >>  row1_num[2] >>  row1_num[3] ;
		}
		
		for ( int i =0 ; i < 4 - row1; i++) {
			fin>> tmp_num[0] >>  tmp_num[1] >>  tmp_num[2] >>  tmp_num[3] ;
		}

		fin>> row2 ;
		for ( int i =0 ; i < row2; i++) {
			fin>> row2_num[0] >>  row2_num[1] >>  row2_num[2] >>  row2_num[3] ;
		}
		
		for ( int i =0 ; i < 4 - row2; i++) {
			fin>> tmp_num[0] >>  tmp_num[1] >>  tmp_num[2] >>  tmp_num[3] ;
		}
		
		int flag = 0, magic_num ;
		for (int i = 0 ; i < 4 ; i++ ) {
			for (int j = 0 ; j < 4 ; j++ ) {
				if  ( row1_num[i]  == row2_num[j] ) {
					flag ++ ;
					magic_num = row1_num[i] ;
				}
			}
		}
	   
		if (flag ==0) {
			fout << "Case #" << test_i+1 << ": " << "Volunteer cheated!" <<endl ;
		} else if (flag ==1) {
			fout << "Case #" << test_i+1 << ": " << magic_num <<endl ;
		} else {
			fout << "Case #" << test_i+1 << ": " << "Bad magician!" <<endl ;
		}

    //printf("%d  %d  %d\n%d %d  %d  %d \n%d %d  %d  %d \n%d \n", num_tests, row1, row2, row1_num[0], row1_num[1], row1_num[2], row1_num[3],row2_num[0], row2_num[1], row2_num[2], row2_num[3], magic_num );
		
    }
   
 
	fin.close();
	fout.close();
	
	return 0;
}