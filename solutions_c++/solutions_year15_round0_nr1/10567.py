/* 
 * File:   main.cpp
 * Author: Mustafa Gomaa
 *
 * Created on April 11, 2015, 4:22 PM
 */

#include <cstdlib>

using namespace std;

/*
 * 
 */
#include <fstream>  
#include <iostream>
#include <string>
  using namespace std;
void readInput(ifstream &infile, int &minNum) ;
void output(const int testCase, const int &minNum);
int main() {
        int T,minNum(0);
        ifstream infile;
        infile.open("A-small-attempt1 (1).in");
        infile >> T;
        for(int i = 0; i < T; i++){
            minNum = 0;
            readInput(infile,minNum);
            output(i + 1, minNum);
        }
        return 0;
    }

void readInput(ifstream &infile,int &minNum){
    int Smax, temp(0);
    char *SmaxStr;
    int *SmaxArr;
    minNum = 0;
    infile >> Smax;
    SmaxStr = new char[Smax + 1];
    SmaxArr = new int[Smax + 1];
    infile >> SmaxStr;
    for(int i = 0; i < Smax + 1; i++){
        SmaxArr[i] = int(SmaxStr[i]) - '0';
    }
    for(int i = 1; i < Smax + 1; i++){
         temp += SmaxArr[i-1];
        if(SmaxArr[i] != 0 && (temp < i)){
            minNum += i - temp;
            temp += minNum; 
        }
    }
}

void output(const int testCase, const int &minNum){
    ofstream outfile;
    outfile.open("out.txt",ios::out | ios::app);
    outfile << "Case #" << testCase << ": " << minNum << endl;
}
    
 
