//
//  p1.cpp
//  GoogleCodeJam
//
//  Created by zhaoxm on 14-4-12.
//  Copyright (c) 2014年 zhaoxm. All rights reserved.
//

#include "p1.h"
#include <iostream>
#include <fstream>
#include <set>

using namespace std;

string helper(int row1, int row2, int numbers1[4][4], int numbers2[4][4]){
    
    bool isMulti = false;
    set<int> candidates;
    
    for(int i = 0; i < 4; i++){
        candidates.insert(numbers1[row1 -1][i]);
    }
    int count  = 0;
    int num = 0;
    for(int i = 0; i < 4; i++){
        if(candidates.count(numbers2[row2 - 1][i]) == 1){
            num = numbers2[row2 - 1][i];
            count++;
        }
    }
    if(count > 1)
        return "Bad magician!";
    if(count == 0)
        return "Volunteer cheated!";
    
     char temp[64];
    sprintf(temp, "%d", num);
    return temp;
}



int main(int argc, const char * argv[])
{
    ifstream in("/Users/zhaoxm/Study/interview/GoogleCodeJam/test.txt");
    if(! in.is_open()){
        cout << "Error opening file";
        exit(1);
    }
    while(! in.eof()){
        int count = 0;
        in >> count;
        for(int i = 1; i <= count; i++){
            int row1;
            int row2;
            int numbers[4][4];
            int numbers2[4][4];
            
            in >> row1;
            for(int j = 0; j < 4; j++){
                for(int k = 0; k < 4; k++){
                    in >> numbers[j][k];
                }
            }
            
            in >> row2;
            for(int j = 0; j < 4; j++){
                for(int k = 0; k < 4; k++){
                    in >> numbers2[j][k];
                }
            }
            cout << "Case #"<< i <<": " << helper(row1, row2, numbers,numbers2) << endl;
        }
    }
    return 0;
}