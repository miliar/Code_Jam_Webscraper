//
//  main.cpp
//  CountingSheep
//
//  Created by Jake Sanders on 4/8/16.
//  Copyright © 2016 Jake Sanders. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

int main(int argc, const char * argv[]) {
    std::ifstream iF;
    iF.open("input.txt", std::fstream::in);
    std::ofstream oF;
    oF.open("output.txt", std::fstream::out);
    if (iF.is_open()) {
        int numberOfInputs;
        iF >> numberOfInputs;
        for (int caseNum = 0; caseNum < numberOfInputs; caseNum++) {
            std::string returnVal = "";
            std::vector<bool> digitsFound (0);
            for (int b = 0; b < 10; b++) {
                digitsFound.push_back(false);
            }
            long n;
            iF >> n;
            bool notDone = true;
            for (int b = 1; notDone; b++) {
                long result = n * b;
                returnVal = std::to_string(result);
                std::string resultStr = std::to_string(result);
                for (int c = 0; c < resultStr.size(); c++) {
                    digitsFound[resultStr[c] - 48] = true;
                }
                notDone = false;
                for (int c = 0; c < digitsFound.size(); c++) {
                    if (digitsFound[c] == false) {
                        notDone = true;
                    }
                    if (b > 100) {
                        returnVal = "INSOMNIA";
                        notDone = false;
                        break;
                    }
                }
            }
            oF << "\nCase #" << caseNum + 1 << ": " << returnVal;
        }
    }
    else {
        std::cout << "error";
    }
    iF.close();
    oF.close();
    
    return 0;
}
