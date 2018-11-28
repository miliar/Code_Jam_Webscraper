//
//  QualProblemA.cpp
//  CodeJam2014
//
//  Created by Ryan Wilson on 2014-04-11.
//  Copyright (c) 2014 Ryan Wilson. All rights reserved.
//

#include <iostream>
#include <fstream>

const std::string inFileName = "/Users/ryanwilson/Desktop/CodeJam/A-small-attempt0.in";
const std::string outFileName = "/Users/ryanwilson/Desktop/CodeJam/output.txt";

int* getImportantRow(int rowNum, std::ifstream &file){
    int *row = new int[4];
    int tmp;
    for (int i = 1; i < 5; ++i){
        if (i == rowNum){
            file >> row[0] >> row[1] >> row[2] >> row[3];
        }
        else {
            file >> tmp >> tmp >> tmp >> tmp;
        }
    }
    
    return row;
}

int main(int argc, const char * argv[]){
    std::ifstream file(inFileName);
    std::ofstream output(outFileName);
    if (!file.is_open() || !output.is_open()){
        std::cout << "Cannot read file, or generate output\n";
        return -1;
    }
    
    int numCases;
    file >> numCases;
    
    for (int i = 0; i < numCases && !file.eof(); ++i){
        int selectedRow;
        file >> selectedRow;
        int *firstRow = getImportantRow(selectedRow, file);

        // Grab the answer again, this time for the second round
        file >> selectedRow;
        int *secondRow = getImportantRow(selectedRow, file);
        
        int match = 0, answer = 0;
        for (int j = 0; j < 4; ++j){
            for (int k = 0; k < 4; ++k){
                if (firstRow[j] == secondRow[k]){
                    ++match;
                    answer = firstRow[j];
                }
            }
        }
        
        // Now we check and output
        output << "Case #" << i+1 << ": ";
        if (match == 0){
            output << "Volunteer cheated!";
        }
        else if (match == 1){
            output << answer;
        }
        else {
            output << "Bad magician!";
        }
        
        if (i != (numCases - 1)){
            output << "\n";
        }
    }
    
    file.close();
    output.close();

    return 0;
}