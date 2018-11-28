#ifndef FAIR_SQUARE_H
#define FAIR_SQUARE_H

#include <fstream>
#include <cstring>
#include <math.h>
using namespace std;

ifstream fs_input;
ofstream fs_output;
int fs_num_cases;

int is_fair_small(int num){
    char num_char[5];
    sprintf(num_char, "%d", num);
    int length = strlen(num_char);
    char* beg = num_char;
    char* end = num_char + length - 1;
    while(beg <= end){
        if(*beg != *end){
            return 0;
        }
        beg++;
        end--;
    }
    return 1;
}

void fair_square_small(){
    fs_input.open("C-small-attempt0.in");
    fs_output.open("fs_output");
    fs_input >> fs_num_cases;
    int small_end, big_end;
    for(int case_id = 1; case_id <= fs_num_cases; case_id++){
        int num_fs = 0;
        fs_input >> small_end >> big_end;
        int from = sqrt(small_end);
        int square = from * from;
        while(square <= big_end){
            if(square >= small_end && is_fair_small(from) && is_fair_small(square)){
                num_fs++;
            }
            from++;
            square = from * from;
        }
        fs_output << "Case #" << case_id << ": " << num_fs << endl;
    }
}
#endif
