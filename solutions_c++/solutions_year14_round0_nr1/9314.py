//
//  main.cpp
//  Magic_Trick
//
//  Created by kuaijianghua on 4/11/14.
//  Copyright (c) 2014 rampageworks. All rights reserved.
//

#include <iostream>
#include <unordered_map>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <iterator>

using namespace std;

class Magic {
    
public:
    int grid[4][4];
    int chosenRow;
    
    Magic(int chosenRow){
        this->chosenRow = chosenRow;
    }
    
    //-1:Bad magician!
    //-2:Volunteer cheated!
    //Other: the card number
    int getAnswer(Magic secondMagic){
        //check the duplicate number
        unordered_map<int, int> duplicateMap;
        
        //First grid
        for (int i = 0; i < 4; i++) {
            //Get number
            int number = this->grid[chosenRow-1][i];
            
            auto got = duplicateMap.find(number);
            
            if (got == duplicateMap.end()) {
                duplicateMap[number] = 1;
            }else{
                duplicateMap[number] = duplicateMap[number] + 1;
            }
        }
        
        //Second grid
        for (int i = 0; i < 4; i++) {
            //Get number
            int number = secondMagic.grid[secondMagic.chosenRow-1][i];
            
            auto got = duplicateMap.find(number);
            
            if (got == duplicateMap.end()) {
                duplicateMap[number] = 1;
            }else{
                duplicateMap[number] = duplicateMap[number] + 1;
            }
        }
        
        int duplicateNumber = 0;
        int cardNumber = -1;
        for (auto it = duplicateMap.begin(); it != duplicateMap.end(); it++) {
            if (it->second > 1) {
                duplicateNumber ++;
                cardNumber = it->first;
            }
        }
        
        switch (duplicateNumber) {
            case 1:
                return cardNumber;
                break;
                
            case 0:
                return -2;
                break;
                
            default:
                return -1;
                break;
        }
    }
};

vector<Magic> firstGridVector;
vector<Magic> secondGridVecotr;
int testCaseNumber = 0;

void setMagics(bool isFirst, ifstream &infile)
{
    string lineString;
    //first Grid
    getline(infile, lineString);
    Magic grid(atoi(lineString.c_str()));
    for (int j = 0; j < 4; j++) {
        getline(infile, lineString);
        
        istringstream iss(lineString);
        vector<string> cardNumbers;
        copy(istream_iterator<string>(iss),
             istream_iterator<string>(),
             back_inserter<vector<string> >(cardNumbers));
        
        for (int k = 0; k < 4; k++) {
            grid.grid[j][k] = atoi(cardNumbers[k].c_str());
        }
    }
    
    if(isFirst){
        firstGridVector.push_back(grid);
    }else{
        secondGridVecotr.push_back(grid);
    }
}

void readInputFile(string fileName)
{
    ifstream infile(fileName.c_str());
    
    //Get test case number
    string lineString;
    getline(infile, lineString);
    testCaseNumber = atoi(lineString.c_str());
    
    for (int i = 0; i < testCaseNumber; i++) {
        setMagics(true, infile);
        setMagics(false, infile);
    }
}

void writeOutPutFile(string outputFileName)
{
    ofstream outputFile(outputFileName.c_str());

    for (int i = 0; i < testCaseNumber; i++) {
        outputFile<<"Case #" << i+1 <<": ";
        
        //Get result
        int result = firstGridVector[i].getAnswer(secondGridVecotr[i]);
        
        switch (result) {
            case -1:
                outputFile << "Bad magician!\n";
                break;
                
            case -2:
                outputFile << "Volunteer cheated!\n";
                break;
                
            default:
                outputFile << result <<"\n";
                break;
        }
    }
    
    outputFile.close();
}

int main(int argc, const char * argv[])
{
    readInputFile("inputFile");
    writeOutPutFile("outputFile");
    return 0;
}

