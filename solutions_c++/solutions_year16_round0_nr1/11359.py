//
//  main.cpp
//  ProblemA
//
//  Created by Zain Sheikh on 4/9/16.
//  Copyright © 2016 Zain sheikh. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <fstream>
#include <sstream>
using namespace std;

#define forA(a) for(int i=0;i<a;i++)

void update(long long a, int b[]){
    long long temp;
    while (a) {
        temp=a%10;
        if (b[temp]==0) {
            b[temp]=1;
        }
        a/=10;
    }
}
bool chk(int a[]){
    forA(10){
        if (a[i]==0) {
            return false;
        }
    }
    return true;
}

int main() {
    ifstream fin("p1small.in");
    ofstream fout("p1small.out");
    int tt;
    fin>>tt;
    
    int cases=1;
    while (tt--) {
        int a[10]={0,0,0,0,0,0,0,0,0,0};
        long long n;
        long long temp=0;
        fin>>n;
        if (n==0) {
            fout<<"Case #"<<cases<<": "<<"INSOMNIA"<<endl;
        }
        else{
            forA(10000){
                    if (chk(a)==true) {
                    fout<<"Case #"<<cases<<": "<<temp<<endl;
                    break;
                }
                temp=n*i;
                update(temp, a);
            }
        }
        cases++;
      
    }
    
    
    
    return 0;
}
