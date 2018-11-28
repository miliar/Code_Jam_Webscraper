//
//  main.cpp
//  Google Code Jam 2014 qualification round number 1
//
//  Created by David Yang on 4/12/14.
//  Copyright (c) 2014 David Yang. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;


ifstream fin("A-small-attempt3.in");
ofstream fout("A-small-attempt3.out");


void Checker(int a[], int b[]){
    
    int temp = 0;
    int temp1 = 0;
    
    for (int i=0; i<4; i++){
        for (int j=0; j<4; j++){
            
            if (a[i] == b[j]){
                temp = a[i];
                temp1 = temp1 + 1;
                
            }
            
            
        }
        
       
    }
    
    if (temp1 == 0){
        fout << "Volunteer cheated!" << endl;
    }
    
    if (temp1 == 1){
        fout << temp << endl;
    }
    
    if (temp1 > 1){
        fout << "Bad magician!" << endl;
    }
    
    
}


int main(int argc, const char * argv[])
{

    int TestNumbers;
    fin >> TestNumbers;
    
    for (int i=0; i< TestNumbers; i++) {
        
        int FirstAnswer;
        fin >> FirstAnswer;
        
        int FirstArray[4];
        int garbagecan;
        for (int k=0; k<4; k++){
            for (int s=0; s<4; s++){
                if (k == FirstAnswer - 1){
                    fin >> FirstArray[s];
                }
                else{
                    fin >> garbagecan;
                }
            }
        }
        
        int SecondAnswer;
        fin >> SecondAnswer;
        
        int SecondArray[4];
        for (int k=0; k<4; k++){
            for (int s=0; s<4; s++){
                if (k == SecondAnswer - 1){
                    fin >> SecondArray[s];
                }
                else{
                    fin >> garbagecan;
                }
            }
        }

        
        fout << "Case #" << i+1 << ": ";
        Checker(FirstArray, SecondArray);

    }
    
    
    fout.close();
    
    
    return 0;
}

