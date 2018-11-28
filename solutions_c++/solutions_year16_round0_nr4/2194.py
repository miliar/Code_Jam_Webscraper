/* 
 * File:   main.cpp
 * Author: mehmetfatihuslu
 *
 * Created on April 12, 2014, 4:56 PM
 */

#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <iomanip>

using namespace std;


int main(int argc, char** argv) {

    fstream inputFile, outputFile, logFile;
    int T,K,C,S;   
    
    inputFile.open("input",ios::in);
    outputFile.open("output",ios::out);       
    logFile.open("log",ios::out);       
    
    inputFile >> T;
            
    for(int dongu=1; dongu<=T; dongu++) {
        
        inputFile >> K >> C >> S ;
        outputFile << "Case #" <<dongu <<": ";
        if(true){
                        
            for(int i=1;i<=K;i++)
                outputFile << i<<" ";
        }
            
        outputFile << endl;
                
    }
    
    return 0;
}

