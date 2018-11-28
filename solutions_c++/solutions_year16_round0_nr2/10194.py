/* 
 * File:   pancakes.cpp
 * Author: Celia
 *
 * Created on 9 de abril de 2016, 19:29
 */

#include <iostream>
#include <string>
#include <istream>
#include <stdio.h>
using namespace std;
 
int fun (int N, string S){
    int cont, i = 0;
    char ant = S[i];
    if(ant == '-' & N == 1) cont++;

    while(i < N-1){
        i++;
        if(S[i] != ant){
            cont++; ant = S[i];
        }
    }
    
    if(((cont%2== 0) && (S[0] == '-')) || ((cont%2 == 1) && (S[0] == '+')))
            cont++;
    //depende del numero de movimientos
    return cont;
}


int main() {
    
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int T; string S;
    
    cin >> T;
    int i=0, j;
    while(i < T){
        cin >> S;    
        cout << "Case #" << i+1 << ": " << fun(S.size(), S) << endl;     
        i++;
    }

    return 0;
}

