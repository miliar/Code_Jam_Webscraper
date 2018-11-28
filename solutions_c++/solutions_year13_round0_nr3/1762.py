/* 
 * File:   main.cpp
 * Author: mfatihuslu
 *
 * Created on April 13, 2013, 8:23 AM
 */

#include <iostream>
#include <cstdlib>
#include <fstream>
#include <cmath>
using namespace std;
#define AND &&
#define OR ||

fstream inputFile, outputFile, logFile;
long long int caseNumber;
long long int A,B;

int findFairSquare(){
    
    /*
    for(int basamak=1;basamak<4;basamak++){
        
        for(int i=0;i<basamak/2;i++){
            
            int palindrom = 
        }
    }
    //*/
    return 1;
}

int main(int argc, char** argv) {

    inputFile.open("input",ios::in);
    outputFile.open("output",ios::out);
    logFile.open("log",ios::out);
    
    inputFile >> caseNumber;
    
    for(long long int i=1; i<=caseNumber; i++) {
        
        inputFile >> A >> B;
        
        long long int start = -1;
        long long int finish = -1;
        
        long long int plist[39] = {1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004};
        
        for(int j=0;j<39;j++){
            
            if (plist[j] >= A and start == -1)
                start = j;
            
            
            if (plist[j] > B and finish == -1)
                finish = j;
        }
        if(finish == -1)
            finish = 39;
        
        outputFile << "Case #"<<i<<": "<<finish-start;
        
        outputFile << endl;
    }
    
    return 0;
}

