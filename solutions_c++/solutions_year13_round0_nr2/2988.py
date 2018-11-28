#ifndef LAWNMOWER_H
#define LAWNMOVER_H

#include <fstream>
using namespace std;

ifstream lawn_input;
ofstream lawn_output;
int lawn_num_cases;

void lawnwover(){
    lawn_input >> lawn_num_cases;
    int num_rows, num_cols;
    int* lawn_matrix;
    int* row_max, *col_max;
    for(int case_id = 1; case_id <= lawn_num_cases; case_id++){
        lawn_input >> num_rows >> num_cols;
        lawn_matrix = new int[num_rows * num_cols];
        row_max = new int[num_rows];
        col_max = new int[num_cols];
        for(int i = 0; i < num_rows; i++){
            for(int j = 0; j < num_cols; j++){
                lawn_input >> lawn_matrix[i * num_cols + j];
            }
        }
        
        //find max in each row and each col
        for(int i = 0; i < num_rows; i++){
            int* start = lawn_matrix + i * num_cols;
            int max_tmp = *start;
            for(int j = 0; j < num_cols; j++){
                if(*start > max_tmp){
                    max_tmp = *start;
                }
                start++;
            }
            row_max[i] = max_tmp;
        }
        for(int i = 0; i < num_cols; i++){
            int* start = lawn_matrix + i;
            int max_tmp = *start;
            for(int j = 0; j < num_rows; j++){
                if(*start > max_tmp){
                    max_tmp = *start;
                }
                start += num_cols;
            }
            col_max[i] = max_tmp;
        }

        //check whether current pattern can do
        int can_do = 1;
        for(int i = 0; i < num_rows; i++){
            for(int j = 0; j < num_cols; j++){
                if(lawn_matrix[i * num_cols + j] < row_max[i] &&
                        lawn_matrix[i * num_cols + j] < col_max[j]){
                    can_do = 0;
                    break;
                }
            }
            if(!can_do){
                break;
            }
        }
        if(can_do){
            lawn_output << "Case #" << case_id << ": YES" << endl;
        }else{
            lawn_output << "Case #" << case_id << ": NO" << endl;
        }
    }
}

void test_lawnwover(){
    lawn_input.open("B-small-attempt0.in");
    lawn_output.open("lawn_output");
    lawnwover();
}

#endif
