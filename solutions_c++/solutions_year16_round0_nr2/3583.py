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
#include <string>
#include <vector>

using namespace std;

ifstream fin("B-large.in.txt");
ofstream fout("output.txt");

string temp;
vector <bool> pila;
int T,C;

void flip(int K) {
    if(K>pila.size()) {
        cerr<<"K to large: "<<K<<' '<<pila.size()<<endl;
        exit(1);
    }
    
    vector <bool> toFlip;
    
    for (int i=0; i<K; i++) {
        toFlip.push_back(!pila[pila.size()-1]);
        pila.pop_back();
    }
    
    for (int i=0; i<K; i++) pila.push_back(toFlip[i]);
    ++C;
}

int main() {
    fin>>T;
    for (int i=1; i<=T; i++) {
        cout<<"Running "<<i<<endl;
        fout<<"Case #"<<i<<": ";
        
        pila.clear();
        C=0;
        fin>>temp;
        for (int j=temp.size()-1; j>=0; j--) {
            if (temp[j]=='+') pila.push_back(1);
            else if(temp[j]=='-') pila.push_back(0);
            else {
                cerr<<"Not Valid Char: "<<temp<<endl;
                exit(1);
            }
        }
        
        for (int j=0; j<pila.size(); j++) {
            if (!pila[j]) {
                if (pila[pila.size()-1]) {
                    int m=1;
                    while(pila[pila.size()-m]) m++;
                    flip(m-1);
                }
                flip(pila.size()-j);
            }
        }
        fout<<C<<endl;
    }
}












