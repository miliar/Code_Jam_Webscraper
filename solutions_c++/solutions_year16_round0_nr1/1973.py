/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   uno.cpp
 * Author: Salvador Daniel Pelayo
 *
 * Created on 8 de abril de 2016, 09:08 PM
 */

#include <iostream>
#include <math.h>

using namespace std;

int digits[10];
int l;

void resetCount(){
    for(int i=0; i<10; i++){
        digits[i] = 0;
    }
    l=0;
}

int* getDigits(int N){
    
    int* d;
    int r = N;
    int count = 0;
    
    do{
        r = (int)r/10;
        count ++;
    }while(r>0);
    
    l = count;
    d = new int[count];
    
    for(int i=0, j=count-1; i<count; i++, j--){
        d[i] = (int)N/(pow(10, j));
        N = N - d[i]*pow(10, j);
    }
    
    return d;
}

int getResult(int N){
    if(N==0) return -1;
    int n = N;
    bool end = false;
    int it = 1;
    while(!end){
        int * d = getDigits(n);
        for(int i=0; i<l; i++){
            digits[d[i]]++; 
        }
        int c = 0;
        for(int i=0; i<10; i++){
            if(digits[i]>0){
                c++;
            }
        }
        if(c==10){
            end = true;
            return n;
        }
        it++;
        n = n + N;
        if(it>10000){
            return -1;
        }
    }
}

int main() {
    int t, N, result;
    cin >> t;
    for (int i = 1; i <= t; ++i){
        cin >> N;
        resetCount();
        result = getResult(N);
        if(result>0)
            cout << "Case #" << i << ": " << result << endl;
        else
            cout << "Case #" << i << ": INSOMNIA" << endl;
    }
}