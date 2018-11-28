// Codejam_1.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fstream>
#include <iostream>
	
	using namespace std;


int main(int argc, char **argv)
{
	int num_test, i, j, diff, won_ctr;
	int datatest[16];
	char tmp_data;
	int x_num, o_num, t_num, dot_num ;
	
	ifstream fin;
    fin.open("test.in");
    if (!fin.good()) throw "I/O error";
	
	ofstream fout ;
	fout.open("test.out");
	if (!fout.good()) throw "I/O error";
	
	fin >> num_test ;
	//printf("Number of test is %d\n", num_test);
	
	//loop for num_test
	//printf("\n");
	
	int x_flag , o_flag ,  draw_flag ,  incomplete_flag ;
	
	for (int test_i=0; test_i<num_test; test_i++) {
		x_flag = 0 ;
		o_flag = 0 ;
		draw_flag = 1 ;
		incomplete_flag = 0 ;
		
		for (i=0; i<16; i++) {
			fin >>  tmp_data ;
			datatest[i] = tmp_data - '.' ;
			//printf("%d ", datatest[i] );
	    }
	
		for (i=0; i<4; i++) {
			x_num =0 ;
			o_num =0 ;
			t_num =0 ;
			dot_num = 0 ;
			
			for (j=0; j<4; j++) {
				if (datatest[i*4+j]==42) {
					x_num ++ ;
				} 
				if (datatest[i*4+j]==38) {
					t_num ++ ;
				}
				if (datatest[i*4+j]==33) {
					o_num ++ ;
				} 
				if (datatest[i*4+j]==0) {
					incomplete_flag = 1 ;
				}
     				
			}			
			
			//printf ("x_num=%d, o_num=%d, t_num=%d \n", x_num, o_num, t_num ) ;
			
			if ( ( x_num==4 ) || ((x_num==3)&&(t_num==1)) )  {
				x_flag = 1 ;
			}
			if ( ( o_num==4 ) || ((o_num==3)&&(t_num==1)) )  {
				o_flag = 1 ;
			}
			
		}

		if ( (x_flag==0)&&(o_flag==0) ) {
			for (i=0; i<4; i++) {
				x_num =0 ;
				o_num =0 ;
				t_num =0 ;
				dot_num = 0 ;
				for (j=0; j<4; j++) {
					switch (datatest[i+j*4]) {
					  case 42:
						x_num ++ ;
						break;
					  case 33:
						o_num ++ ;
						break;
					  case 38:
						t_num ++ ;
						break;
					  default:
						incomplete_flag = 1 ;
					} 			
				}	
				//printf ("x_num=%d, o_num=%d, t_num=%d \n", x_num, o_num, t_num ) ;
				
				if ( ( x_num==4 ) || ((x_num==3)&&(t_num==1)) )  {
					x_flag = 1 ;
					break ;
				}
				if ( ( o_num==4 ) || ((o_num==3)&&(t_num==1)) )  {
					o_flag = 1 ;	
					break ;
				}
				
			}    
		
		}
		
		if ( (x_flag==0)&&(o_flag==0) ) {			
				x_num =0 ;
				o_num =0 ;
				t_num =0 ;
				dot_num = 0 ;
				i=0 ;
				j=0 ;
				for (int diag_i=0; diag_i<4; diag_i++) {
					switch (datatest[i+j*4]) {
					  case 42:
						x_num ++ ;
						break;
					  case 33:
						o_num ++ ;
						break;
					  case 38:
						t_num ++ ;
						break;
					  default:
						incomplete_flag = 1 ;
					} 			
					i++ ;
					j++ ;
				}	
				//printf ("x_num=%d, o_num=%d, t_num=%d \n", x_num, o_num, t_num ) ;
				
				if ( ( x_num==4 ) || ((x_num==3)&&(t_num==1)) )  {
					x_flag = 1 ;
					//break ;
				}
				if ( ( o_num==4 ) || ((o_num==3)&&(t_num==1)) )  {
					o_flag = 1 ;	
					//break ;
				}
	    }

		if ( (x_flag==0)&&(o_flag==0) ) {			
				x_num =0 ;
				o_num =0 ;
				t_num =0 ;
				dot_num = 0 ;
				i=3 ;
				j=0 ;
				for (int diag_i=0; diag_i<4; diag_i++) {
					switch (datatest[i+j*4]) {
					  case 42:
						x_num ++ ;
						break;
					  case 33:
						o_num ++ ;
						break;
					  case 38:
						t_num ++ ;
						break;
					  default:
						incomplete_flag = 1 ;
					} 			
					i-- ;
					j++ ;
				}	
				//printf ("x_num=%d, o_num=%d, t_num=%d \n", x_num, o_num, t_num ) ;
				
				if ( ( x_num==4 ) || ((x_num==3)&&(t_num==1)) )  {
					x_flag = 1 ;
					//break ;
				}
				if ( ( o_num==4 ) || ((o_num==3)&&(t_num==1)) )  {
					o_flag = 1 ;	
					//break ;
				}
	    }		
 

		if (x_flag==1) 
			fout << "Case #" << test_i+1 <<": X won" << endl ;
			//printf("X won\n") ;	
		if (o_flag==1) 
			fout << "Case #" << test_i+1 <<": O won" << endl ;
			//printf("O won\n") ;		
        if ( (x_flag==0)&&(o_flag==0) ) {
			if (incomplete_flag == 1) 
			    fout << "Case #" << test_i+1 <<": Game has not completed" << endl ;
				//printf("Game has not completed\n") ;	
			else 
			    fout << "Case #" << test_i+1 <<": Draw" << endl ;
				//printf("Draw\n") ;
				
		}
 			
    }		
	return 0;
}

