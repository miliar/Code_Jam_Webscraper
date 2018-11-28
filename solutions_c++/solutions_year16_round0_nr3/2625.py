//
//  main.cpp
//  test
//
//  Created by Hui Xu on 3/22/16.
//  Copyright © 2016 Hui Xu. All rights reserved.
//
/*
 
 */

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

typedef unsigned long long int LLI;

#define _Test_

// determine whether targetNum in powBase is a prime,
// if not return one of targetNum non-trivial divisor
// else return 0
int NonTrivialDiv(int powBase, string targetNum){
    LLI powBNum=0;
    string strNum;
    for (int i=targetNum.length()-1; i>=0; i--) {
        if (targetNum[i]=='1') {
            powBNum+=pow(powBase,targetNum.length()-1-i);
        }
    }
    // is prime?
    if (powBNum==2) {
        return 0;
    }
    if (powBNum%2==0) {
        return 2;
    }
    for (int i=3; i<sqrt(powBNum); i++) {
        if (powBNum%i==0) {
            return i;
        }
    }
    return 0;
}

int main(int argc, const char * argv[]) {
#ifdef _Test_
    freopen("/Users/huixu/Desktop/APACTEST/test/test/C-small-attempt0.in", "r", stdin);
    freopen("/Users/huixu/Desktop/APACTEST/test/test/C-small-attempt0.out", "w", stdout);
#endif
    int T;
    int N,J;
    cin>>T;
    for (int t=0; t<T; t++) {
        cin>>N>>J;
        string targetNumStr(N,'0');
        targetNumStr[0]='1';
        targetNumStr[N-1]='1';// initial
        
        //= 1 + (1<<(N-1));
        cout<<"Case #"<<t+1<<": "<<endl;
        int count=0;
        for (int i=1; i<=pow(2, N-2),count<J; i++) {
            int twoBase=NonTrivialDiv(2,targetNumStr);
            int thrBase=NonTrivialDiv(3,targetNumStr);
            int fouBase=NonTrivialDiv(4,targetNumStr);
            int fiveBase=NonTrivialDiv(5,targetNumStr);
            int sixBase=NonTrivialDiv(6,targetNumStr);
            int sevBase=NonTrivialDiv(7,targetNumStr);
            int eigBase=NonTrivialDiv(8,targetNumStr);
            int ninBase=NonTrivialDiv(9,targetNumStr);
            int tenBase=NonTrivialDiv(10,targetNumStr);
            if(twoBase && thrBase && fouBase && fiveBase && sixBase && sevBase && eigBase && ninBase && tenBase){
                count++;
                cout<<targetNumStr<<' '<<twoBase <<' '<< thrBase<<' ' << fouBase<<' ' << fiveBase<<' ' << sixBase<<' ' << sevBase<<' ' << eigBase<<' ' <<ninBase<<' ' << tenBase<<endl;
                //targetNum += (1<<i);
                
            }
            
            // multiple strings
            int tempi = i;
            for (int k=N-2; k>0; k--) {
                int num = tempi %2;
                if (num==1) {
                    targetNumStr[k]='1';
                }
                else
                    targetNumStr[k]='0';
                tempi/=2;
            }
        }
    }
    return 0;
}
