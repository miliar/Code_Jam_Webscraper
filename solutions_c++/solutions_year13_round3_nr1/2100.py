/* 
 * File:   main.cpp
 * Author: mfatihuslu
 *
 * Created on May 12, 2013, 11:53 AM
 */

#include <cstdlib>
#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#define AND &&
#define OR ||

using namespace std;

fstream inputFile, outputFile, logFile;
int T,n;

/*
 * 
 */

bool consonant(char letter){
    
    if(letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u')
        return false;
    
    return true;
}

int solve(string word, int n){
    
    int result = 0, coFlag=0, subStr=0;
    int *strIndex = new int[word.length()];
    
    for(int i=0;i < word.length();i++){
        
        
        //logFile << "length: "<< i << " result:" << result << endl;
        
        for(int j=0;j<subStr;j++){
            
                    result+=strIndex[j];
                    logFile << strIndex[j]<<endl;
        }
        
        if(consonant(word[i])){
            
            coFlag++;
            if(coFlag >= n){
                
                //logFile << "result before: "<<result<<endl;
                //logFile << "new str index: "<<i+2-n-subStr << " substr: "<< subStr <<" i: "<< i <<" n: "<< n <<  endl;
                
                int subStrDecNum = 0;
                
                for(int j=0;j<subStr;j++){
            
                    subStrDecNum+=strIndex[j];
                    
                }
                
                strIndex[subStr]=i+2-n-subStrDecNum;
                //logFile << "new add: "<<i<<"+2-"<<n<<"-"<<subStr<<"="<<strIndex[subStr]<<endl;
                result = result + strIndex[subStr];
                //logFile << "result now: "<<result<<endl;
                subStr++;                
            }
            else {
                
                
            }
        }
        else{
            
            coFlag=0;         
        }
        
        //logFile << "length: "<< i << " result:" << result << endl;
    }
    
    return result;
}

int main(int argc, char** argv) {

    inputFile.open("input",ios::in);
    outputFile.open("output",ios::out);
    logFile.open("log",ios::out);
    
    inputFile >> T;
    
    for(int i=0; i<T; i++) {

        string word;
        inputFile >> word;
        inputFile >> n;
        
        outputFile << "Case #" << i+1 << ": " << solve(word,n) << endl; 
        
    }
    
    //outputFile <<"";
    return 0;
}

