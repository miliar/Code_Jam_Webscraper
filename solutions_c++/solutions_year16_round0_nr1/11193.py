//
//  main.cpp
//  Sheep
//
//  Created by 葛 on 4/8/16.
//  Copyright © 2016 葛. All rights reserved.
//

#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
#include <stdlib.h>
using namespace std;
string counting(string s){
    
    int m = 0;
    int n;
    int a [10];
    for(int i=0; i<10; i++) {
        a[i] = 0;
    }
    bool flag = 1;
    int base = atoi(s.c_str());

    while (flag) {
        flag = false;
        n = s.length();
        for (int i = 0; i < n; i++) {
            a[s[i] - '0'] = 1;
        }

        
        
        for (int j = 0; j < 10; j++) {
            if(a[j] == 0){
                flag = true;
                m += base;
                s = to_string(m);
                break;
            }
        }
    }
    
    return s;
}
    

int main(){
    ifstream f ("A-large.in.txt");
    ofstream out("output.txt");
    int n,i=1;
    f>>n;
 
    string sheep;
    while(f>>sheep){
    
        if (sheep == "0"){
            out<< "case #"<< i++ <<": INSOMNIA"<<endl;
        }
        else{
            out<< "case #"<< i++ << ": ";
            out<<counting(sheep)<<endl;
        }
    }
    
   
}
