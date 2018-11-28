/* 
 * File:   main.cpp
 * Author: mehmetfatihuslu
 *
 * Created on April 12, 2014, 4:56 PM
 */

#include <cstdlib>
#include <iostream>
#include <fstream>
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
    
    for(int dongu=1; dongu<=T; dongu++) {
        
        int N;        
        inputFile >>N;
        int digits[10];
        
        for(int i=0;i<10;i++)
            digits[i]=0;
        
        int lastdigit = -1;
        int tempN = N;

        if(N==0)
            outputFile << "Case #" <<dongu <<": INSOMNIA";
        else{
            
            for(int say=1;true;say++){
            
                int sayi = N*say;                          
                
                do {
                    int digit = sayi % 10;

                    digits[digit]=1;
                    lastdigit = digit;
                    sayi /= 10;

                } while (sayi > 0);
                
                int toplam=0;
                
                for(int i=0;i<10;i++){
                
                    toplam+=digits[i];
                }
                
                if(toplam==10){
                
                    outputFile << "Case #" <<dongu <<": "<<N*say;
                    break;
                }         
                else{
                                        
                }
            }
            
        }
        
        //fprintf("\n");
        outputFile << endl;
    }
    
    return 0;
}

