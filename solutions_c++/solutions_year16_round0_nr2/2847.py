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
    int T;   
    
    inputFile.open("input",ios::in);
    //FILE *out = fopen ("output","w");
    outputFile.open("output",ios::out);       
    logFile.open("log",ios::out);       
    
    inputFile >> T;
    string line;
    getline(inputFile,line);    
    
    for(int dongu=1; dongu<=T; dongu++) {
        
        getline(inputFile,line);       
        
        int group = 1;
        for(int i=0;i<line.length()-1;i++){
            
            if(line[i]!=line[i+1])
                group++;
        }
        
        if(line[line.length()-1]=='+')
            group--;
                
        outputFile << "Case #" <<dongu <<": "<<group;
              
        outputFile << endl;
    }
    
    return 0;
}

