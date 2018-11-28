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
using namespace std;

typedef unsigned long long int LLI;

#define _Test_

int main(int argc, const char * argv[]) {
#ifdef _Test_
    freopen("/Users/huixu/Desktop/APACTEST/test/test/B-large.in", "r", stdin);
    freopen("/Users/huixu/Desktop/APACTEST/test/test/B-large.out", "w", stdout);
#endif
    int T;
    string s;
    
    cin>>T;
    for (int t=0; t<T; t++) {
        cin>>s;
        int count=0;
        bool flagAllplus=false;
        //for (int i=0; i<s.length(); i++) { //change to binary
        //    if(s[i]=='+'){
        //        sti += 1<<(s.length()-1);
        //    }
        //}
        while (flagAllplus==false) {
            int pluscount=0;
            for (int i=s.length()-1; i>=0; i--) {
                if(s[i]=='-'){
                    for (int j=i; j>=0; j--) {
                        if(s[j]=='+'){
                            s[j]='-';
                        }else
                            s[j]='+';
                    }
                    count++;
                }
                else{
                    pluscount++;
                }
                
            }
            if (pluscount==s.length()) {
                flagAllplus=true;
            }
        }
        
        cout<<"Case #"<<t+1<<": "<<count<<endl;
    }
    return 0;
}
