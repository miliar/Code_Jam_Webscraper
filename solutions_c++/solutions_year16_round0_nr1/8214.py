//
//  main.cpp
//  codejam
//
//  Created by 안재우 on 2016. 4. 9..
//  Copyright © 2016년 안재우. All rights reserved.
//
#include<fstream>
#include<iostream>
#include<cstring>
using namespace std;
int n=1;
bool checkDigit(bool digit[]);
char inputString[10];
int main(int argc, const char * argv[]) {
    ofstream outFile("output.in");
    ifstream inFile("A-large.in");
    inFile.getline(inputString, 10);
    int T=stoi(inputString);
    bool digit[10];
    while(!inFile.eof()&&T--){
        memset(digit,false,sizeof(digit));
        inFile.getline(inputString,10);
        int N=stoi(inputString);
        if(N==0){
            outFile<<"Case #"<<n<<": INSOMNIA"<<endl;
            n++;
            continue;
        }
        int cnt=1;
        while(!checkDigit(digit)){
            int tmp=N*cnt;
            while(tmp!=0){
                int lastDigit = tmp%10;
                digit[lastDigit] = true;
                tmp/=10;
            }
            cnt++;
        }
        outFile<<"Case #"<<n<<": "<<N*(cnt-1)<<endl;
        n++;
    }
    inFile.close();
}

bool checkDigit(bool digit[]){
    for(int i=0;i<10;i++){
        if(digit[i]==false) return false;
    }
    return true;
}