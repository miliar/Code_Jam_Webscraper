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
    string line;
    
    inputFile.open("input",ios::in);
    outputFile.open("output",ios::out);       
    logFile.open("log",ios::out);       
    
    inputFile >> T;
    getline(inputFile, line);
    char temp;
    int tmpint;
    
    int* dizi = new int[91];    // 65 - 90 arasi
    int * sayi = new int[10];       
    
    for(int dongu=1; dongu<=T; dongu++) {   
        
        for(int i=0;i<91;i++)
                dizi[i]=0;
        for(int i=0;i<10;i++)
                sayi[i]=0;
        
        getline(inputFile, line);
        int length = line.length();
        
        for(int i=0;i<length;i++){
           
            tmpint = (int)line[i];
            dizi[tmpint] ++;            
        }
        
        cout<<line<<endl;
        
        for(int i=65;i<91;i++)
            cout<<dizi[i];               
        
        cout <<endl;
        
        sayi[0] = dizi[90];
        dizi[90]-=sayi[0];
        dizi[82]-=sayi[0];
        dizi[79]-=sayi[0];
        dizi[69]-=sayi[0];
        
        sayi[2] = dizi[87];
        dizi[87]-=sayi[2];
        dizi[84]-=sayi[2];
        dizi[79]-=sayi[2];
        
        sayi[4] = dizi[85];
        dizi[85]-=sayi[4];
        dizi[82]-=sayi[4];
        dizi[79]-=sayi[4];
        dizi[70]-=sayi[4];
        
        sayi[6] = dizi[88];
        dizi[88]-=sayi[6];
        dizi[73]-=sayi[6];
        dizi[83]-=sayi[6];
        
        sayi[8] = dizi[71];
        dizi[71]-=sayi[8];
        dizi[84]-=sayi[8];
        dizi[73]-=sayi[8];
        dizi[72]-=sayi[8];
        dizi[69]-=sayi[8];
        
        sayi[1] = dizi[79];
        dizi[79]-=sayi[1];
        dizi[78]-=sayi[1];
        dizi[69]-=sayi[1];
        
        sayi[3] = dizi[84];
        dizi[84]-=sayi[3];
        dizi[72]-=sayi[3];
        dizi[82]-=sayi[3];
        dizi[69]-=(sayi[3]*2);
        
        sayi[5] = dizi[70];
        dizi[70]-=sayi[5];
        dizi[73]-=sayi[5];
        dizi[86]-=sayi[5];
        dizi[69]-=sayi[5];
        
        sayi[7] = dizi[83];
        dizi[83]-=sayi[7];
        dizi[69]-=(sayi[7]*2);
        dizi[86]-=sayi[7];
        dizi[78]-=sayi[7];
        
        sayi[9] = dizi[73];
        
        outputFile << "Case #" <<dongu <<": ";
        
        for(int i=0;i<10;i++){
            for(int j=0;j<sayi[i];j++)
                outputFile<<i;
        }
        
                
        //
        //cout<<line<<endl;
        //for(int i=0;i<line);        
            
        outputFile << endl;
                
    }
    
    return 0;
}

