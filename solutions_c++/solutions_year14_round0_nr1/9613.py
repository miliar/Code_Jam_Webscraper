//
//  main.cpp
//  LFS
//
//  Created by Moko on 2/23/14.
//  Copyright (c) 2014 Moko Tech. All rights reserved.
//



#include <iostream>
#include <fstream>

using namespace std;


int main(int argc, const char * argv[])
{
    int totalCases;
    int input1;
    int input2;
    int matrix1[4][4];
    int matrix2[4][4];
    
    
    ifstream fin;
    fin.open("/Development/OS Assigment/1_13030020_13030022/A-small-attempt3.in");
    fin >> totalCases;
   // cout << totalCases;
    ofstream fout;
    fout.open("/Development/OS Assigment/1_13030020_13030022/outfile.txt");
    for (int caseNumber = 1; caseNumber <= totalCases; caseNumber++) {
        
        // input 1
        fin >> input1;
        input1--;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                fin >> matrix1[i][j];
            }
        }
        // inout 2
        fin >> input2;
        input2--;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                fin >> matrix2[i][j];
            }
        }
       
        
        int commanCount = 0;
        int commonCol = 0;
        // compare rows in input1 and input 2
        for (int i = 0; i < 4; i++) { // for input 1
            for (int j = 0; j < 4; j++) {// for input 2
                if (matrix1[input1][i] == matrix2[input2][j]) {
                    commanCount++;
                    commonCol = i;
                }
            }
        }
        fout <<"Case #"<<caseNumber<<": ";
        if (commanCount == 1) {
            fout << matrix1[input1][commonCol];
        }else if (commanCount == 0)
        {
            fout << "Volunteer cheated!";
        }else
        {
            fout << "Bad magician!";
        }
        fout << endl;
        
    }
    
    
    return 0;
}




