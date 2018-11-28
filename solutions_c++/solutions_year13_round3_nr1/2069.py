//
//  main.cpp
//  1C1
//
//  Created by Zulkarnine Mahmud on 5/12/13.
//  Copyright (c) 2013 Zulkarnine Mahmud. All rights reserved.
//

#include <iostream>
#include <cstdlib>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <deque>
#include <list>

using namespace std;

#define nl cout<<endl

const string tester="aeiou";

bool notVowel(char c){

    for (unsigned long i =0; i<5; i++) {
        if (c==tester[i]) {
            return false;
        }
    }
    return true;
}

unsigned long solvecase(string G,unsigned long n){
    string X=G;
    
    unsigned long val=0;
    if (n==1) {
        for (unsigned long i=(X.length()); i>=n; i--) {
            unsigned long len=i;
            for (unsigned long j=0; j<=(X.length()-len); j++) {
                string XN=X.substr(j,len);
                unsigned long counter=0;
                unsigned long lastCount=0;
                for (unsigned long k=0; k<XN.length(); k++) {
                    if (notVowel(XN[k])) {
                                val++;
                                break;
                    }
                    
                }
            }
            
        }
    }else{
        for (unsigned long i=(X.length()); i>=n; i--) {
            unsigned long len=i;
            for (unsigned long j=0; j<=(X.length()-len); j++) {
                string XN=X.substr(j,len);
                unsigned long counter=0;
                unsigned long lastCount=0;
                for (unsigned long k=0; k<XN.length(); k++) {
                    if (notVowel(XN[k])) {
                        if (lastCount==k-1) {
                            lastCount=k;
                            counter++;
                            if (counter==n) {
                                val++;
                                break;
                            }
                        }else{
                            lastCount=k;
                            counter=1;
                        }
                        
                    }else{
                        lastCount=0;
                        counter=0;
                    }
                }
            }
            
        }
    
    }
    
    return val;
}


int main(int argc, const char * argv[])
{
    unsigned long T,cas=1;
    //test
    freopen("/Users/rezan_mahmud/Desktop/A-small-attempt1.in", "r", stdin);
    freopen("/Users/rezan_mahmud/Desktop/test.out", "w", stdout);
    
    //    //small input
    //    freopen("small.in", "r", stdin);
    //    freopen("small.out", "w", stdout);
    //
    //    //large input
    //    freopen("large.in", "r", stdin);
    //    freopen("large.out", "w", stdout);
    
    cin>>T;
    while (T--) {
        //variables
        string s;
        unsigned long n;
        cin>>s>>n;
        
        
        //output
        cout<<"Case #"<<cas++<<": "<<solvecase(s,n)<<endl;
        
        
    }
    
    
    return 0;
}

