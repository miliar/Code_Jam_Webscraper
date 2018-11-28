//
//  main.cpp
//  codejam
//
//  Created by Deshmukh  on 11/04/15.
//  Copyright (c) 2015 Deshmukh . All rights reserved.
//

#include <iostream>
#include<fstream>
#include<string>
using namespace std;
int main(int argc, const char * argv[]) {
    ifstream ip;
    ofstream op;
    ip.open("/Users/deshmukh/Desktop/c/Udit/codejam/sample.txt");
    op.open("/Users/deshmukh/Desktop/c/Udit/codejam/output.txt");
    
    
    int t,t1;
    ip>>t;
    for(t1=1;t1<=t;t1++){
        int smax,clapped,req=0,i;
        string str;
        ip>>smax;
        ip>>str;
        clapped=str[0]-'0';
        for(i=1;i<str.length();i++){
            if(clapped<i){
                req+=i-clapped;
                clapped+=i-clapped;
            }
            clapped+=str[i]-'0';
        }
        op<<"Case #"<<t1<<": "<<req<<endl;
        
    }
    
    
    return 0;
}
