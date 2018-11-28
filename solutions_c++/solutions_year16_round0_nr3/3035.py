//
//  model.cpp
//  
//
//  Created by Luca Arnaboldi on 13/04/15.
//
//

#include <stdio.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <math.h>
#include <map>
#include <string>
#include <vector>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

long long int toBase(long long int N,int B) {
    long long int R=0;
    for(int i=0;N!=0;i++) {
        R+=(N%10)*pow(B,i);
        N/=10;
    }
    return R;
}

long long int isPrime(long long int N) {
    for (int i=2; i<sqrt(N)+1; i++) {
        if (N%i==0) return i;
    }
    return 0;
}

/*
string toString(long long int K) {
    string temp;
    for (int i=15; i>=0; i--) {
        if(K>pow(2,i)) {
            temp.push('1');
            K-=pow(2,i);
        } else {
            temp.push('0');
        }
    }
    return temp;
}
 */

map <long long int,bool> used;
vector <int> result;

int main() {
    fout<<"Case #1:"<<endl;
    for (int i=0; i<50; i++) {
        cout<<"Running: "<<i<<endl;
        
        long long int K=1000000000000001;
        for (int j=1; j<15; j++) K+=(rand()%2)*pow(10,j);
        //cout<<"K: "<<K<<endl;
        
        if (used[K]) {
            i--;
            continue;
        } else used[K]=1;
        
        result.clear();
        
        for(int j=2;j<=10;j++) {
            int y=isPrime(toBase(K,j));
            //cout<<y<<endl;
            if(y==0) {
                cout<<"Prime!"<<endl;
                i--;
                break;
            }
            result.push_back(y);
        }
        
        //cout<<"Printing!"<<endl;
        
        if(result.size()==9) {
            fout<<K;
            for(int j=0;j<9;j++) fout<<' '<<result[j];
            fout<<endl;
        }
    }
}






