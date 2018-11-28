#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>
#include <iterator>
#include <list>
#include <map>
#include <math.h>

using namespace std;

int check_row (int **lawn, int row_num, int cols)
{
	for (int i = 0; i < cols; i++) {
		if (lawn[row_num][i] == 2) {
		    return 0;
		}
	}
	return 1;
}


int check_col (int **lawn, int rows, int col_num)
{

	for (int i = 0; i < rows; i++) {
		if (lawn[i][col_num] == 2) {
		    return 0;
		}
	}
	return 1;
}


const char *
process_lawn (int **lawn, int rows, int cols)
{
   for (int i = 0; i < rows; i++) {
	   for (int j = 0; j < cols; j++) {
		   if (lawn[i][j] == 1) {
			  // Check if the whole column is 1s
			  if (!check_col(lawn, rows, j)) {
			      // Check if the whole row is 1s
				 if (!check_row(lawn, i, cols)) {
					return "NO";
				 } else {
					break;
				 }
			  }
		   }
	   }
   }
   return "YES";
}


int main(int argc, char **argv) {
	int case_num = 1;
	string str;
	bool first = 0;
	int total_cases;
	unsigned int TC_num = 1;
	unsigned int line = 0;
	int val;
	int row = 0;
	int **board;
	int rows, cols;
	int read_rows_cols = 1;
	
	ifstream read_file (argv[1]);

	if (read_file.is_open()) {
	    while (getline(read_file, str)) {
			 if (!first) {
				 total_cases = atoi(str.c_str());
				 first = 1;
				 line = 1;
			 } else {
				 stringstream ss(str);
				 if (read_rows_cols) {
				     ss >> rows >> cols;	
					row  = 0;
					read_rows_cols = 0;
	                    board = (int **)malloc(rows * sizeof(int *));
	                    for (int i = 0; i < rows ; i++) {
		                    board[i] = (int *)malloc(sizeof(int)*cols);
	                    }
				 } else {
					line++;
					for (int j=0; j < cols; j++) {
						ss >> val;
						board[row][j] = val;
					}
					row++;

					if (row == rows) {
					   /* last line of the matrix */
					   read_rows_cols = 1;
				        cout << "Case #" << TC_num++ << ": " << process_lawn(board, rows, cols) << endl;
                            for (int i = 0; i < rows; i++) {
		                       free(board[i]);
	                       }
	                       free(board);
					}
				 }
			 }
	    }
	    read_file.close();
	}
}
