#include<iostream>
#include<cstdlib>
#include<fstream>
#include<stdio.h>
#include<string.h>

using namespace std;
char ptr_x[2] = "X";
char ptr_o[2] = "O";
char ptr_t[2] = "T";
char ptr_dot[2] = ".";

int decision_function(char rr[][4]) {
  int end_decision;
  int i,j,e;
  int some_one_won=0;
  int marker_i_j_x[4][4] ,marker_i_j_o[4][4];
  int x_v_stat=0,o_v_stat=0,x_h_stat=0,o_h_stat=0,x_rc_stat=0,o_rc_stat=0,x_lc_stat=0,o_lc_stat=0;
  int draw_test_sum=0;
  cout << ptr_t[0] << ptr_x[0] << ptr_o[0] << ptr_dot[0] << endl;
  for (i=0;i<4;i++) {
    for (j=0;j<4;j++) {
      if (rr[i][j] - ptr_x[0] == 0 || rr[i][j] - ptr_t[0] == 0) {
	marker_i_j_x[i][j] = 0; draw_test_sum++;
      }
      else  
	marker_i_j_x[i][j] = 1;
      
      if (rr[i][j] - ptr_o[0] == 0 || rr[i][j] - ptr_t[0] == 0) {
	marker_i_j_o[i][j] = 0; draw_test_sum++;
      }
      else 
	marker_i_j_o[i][j] = 1;      
    }
  }
  for (i=0;i<4;i++) {
    x_h_stat=0; o_h_stat=0;
    for (j=0;j<4;j++) {
      if (marker_i_j_x[i][j] == 0)
	x_h_stat++;
      if (marker_i_j_o[i][j] == 0)
	o_h_stat++;
    }
    if (o_h_stat == 4 || x_h_stat == 4 )
      break;
  }
  for (j=0;j<4;j++) {
    x_v_stat=0; o_v_stat=0;
    for (i=0;i<4;i++) {
      if (marker_i_j_x[i][j] == 0)
	x_v_stat++;
      if (marker_i_j_o[i][j] == 0)
	o_v_stat++; 
    }
    if (o_v_stat == 4 || x_v_stat == 4 )
      break;
  }  
  for (e=0;e<4;e++) {
    if (marker_i_j_x[e][e] == 0)
      x_lc_stat++;
    if (marker_i_j_o[e][e] == 0)
      o_lc_stat++;
  }
  for (e=0;e<4;e++) {
    if (marker_i_j_x[e][3-e] == 0)
      x_rc_stat++;
    if (marker_i_j_o[e][3-e] == 0)
      o_rc_stat++;
  }
  if (x_h_stat == 4 || x_v_stat == 4 || x_lc_stat == 4 || x_rc_stat == 4) {
    end_decision = 0;
    some_one_won++;
  }
  else if (o_h_stat == 4 || o_v_stat == 4 || o_lc_stat == 4 || o_rc_stat == 4) {
    end_decision = 1;
    some_one_won++;
  }
  else if (some_one_won == 0 && (draw_test_sum == 17|| draw_test_sum ==16))
    end_decision = 2;
  else 
    end_decision = 3 ;

  cout << draw_test_sum << endl; 

  return end_decision;

}

int main () {
  if (remove("output.txt")!=0) {
    cout << "OLD output is not deleted ! " << endl;
    exit(0);
  }
  ofstream outputFile;
  outputFile.open("output.txt",ios::app);
  char read[4][4]; 
  int rr=0;
  int z;
  int test_cases;
  ifstream inputFile;
  inputFile.open("A-small-attempt1.in");
  if (!inputFile) {
    cout << "No input file found !! " << endl;
    exit (1);
  }
  int line_count=0;   int index=0;
  while (!inputFile.eof() && !index == test_cases ) {
    if (line_count == 0) {
      inputFile >> test_cases;
      cout << test_cases << endl;
      line_count++;
    }
  
    for (;index<test_cases;) {
      inputFile >> read[rr];
      rr++;
      if (rr == 4) {
	z = decision_function(read); cout << "CALLED" << endl;
	if (z==0)
	  outputFile << "Case #" << index+1 << ":" << " X won" << endl;
	else if (z==1)
	  outputFile << "Case #" << index+1 << ":" << " O won" << endl;
	else if (z==2)
	  outputFile << "Case #" << index+1 << ":" << " Draw" << endl;
	else if (z==3)
	  outputFile << "Case #" << index+1 << ":" << " Game has not completed" << endl;
	else 
	  cout << "Failed to code it right !!" << endl;
	rr = 0;  index++;
      }     
    }
  }
  return 0;
}
