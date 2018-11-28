//
//  main.cpp
//  Magic Tirck
//
//  Created by Zhe Zhang on 4/11/14.
//  Copyright (c) 2014 Zhe Zhang. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

void check_magic_trick(int placement_1[][4], int placement_2[][4], int row_1, int row_2, int case_index){
    
    int candidate_num = 0;
    string result;
    int card_num = 0;
    
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (placement_1[row_1][i] == placement_2[row_2][j]) {
                card_num = placement_1[row_1][i];
                candidate_num ++;
                break;
            }
        }
    }
    
    if (candidate_num == 0) {
        cout << "Case #" << case_index << ": Volunteer cheated!" << endl;
    }
    else if (candidate_num > 1){
        cout << "Case #" << case_index << ": Bad magician!" << endl;
    }
    else if (candidate_num == 1){
        cout << "Case #" << case_index << ": " << card_num << endl;
    }
    
}

int main(int argc, const char * argv[])
{

    // read the input file
    string line;
    ifstream input_file("A-small-attempt0.in.txt");
    int test_case_num = 0;
    
    // first get the number of test cases
    getline(input_file, line);
    stringstream sstream(line);
    sstream >> test_case_num;
    
    int row_1;
    int row_2;
    int placement_1[4][4];
    int placement_2[4][4];
    // for each test case, read in the input
    for (int i = 0; i < test_case_num; i++) {
        
        getline(input_file, line);
        stringstream answer_1(line);
        answer_1 >> row_1;
        
        for (int j = 0; j < 4; j++) {
            getline(input_file, line);
            stringstream row_str(line);
            int n;
            int index = 0;
            while (row_str >> n) {
                placement_1[j][index] = n;
                index ++;
            }
        }
        
        
        getline(input_file, line);
        stringstream answer_2(line);
        answer_2 >> row_2;
        
        for (int j = 0; j < 4; j++) {
            getline(input_file, line);
            stringstream row_str(line);
            int n;
            int index = 0;
            while (row_str >> n) {
                placement_2[j][index] = n;
                index ++;
            }
        }
        
        check_magic_trick(placement_1, placement_2, row_1-1, row_2-1, i+1);
    }
    
    return 0;
}

