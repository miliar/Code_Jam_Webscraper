/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   main.cpp
 * Author: juan
 *
 * Created on 8 de abril de 2016, 21:23
 */

#include <cstdlib>
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <math.h>
using namespace std;
/*
 *
 */
int ndigitos (double n){
     int ndigitos = 0;
    int div = n;
    while(div!=0){
        div = div/10;
        ndigitos++;
    }
    return ndigitos;
}

int * digitos(double n,int ndigitos){
    int *digit = new int[ndigitos];
    int piv = n;
    for(int i=0;i<ndigitos;i++){
        digit[i] = piv%10;
        piv = (int)piv/10;
        //cout<<"digito:"<<digit[i]<<endl;
    }
    return digit;
}
bool termina(int * todos){
    int sum = 0;
    for(int i=0;i<10;i++){
        sum = sum+todos[i];
    }
    if(sum==10){
        return true;
    }
    else{
        return false;
    }
}

double ultimo(double n){
    int *todos = new int[10];
    for(int i=0;i<10;i++){
        todos[i]=0;
    }
    int N = 0;
    while(N<1000){
        N++;
        int num = ndigitos(N*n);
        int * digit = new int[num];
        digit = digitos(N*n,num);
        for(int i=0;i<num;i++){
            todos[digit[i]] = 1;
        }
        if(termina(todos)){
            break;
        }
    }
    return N*n;
}

int main(int argc, char** argv) {
    int t, n;
    double final;
    cin >> t;
    for (int i = 1; i <= t; i ++) {
        cin >> n ; 
        final = ultimo(n);
        if(n!=0){
            cout << "Case #" << i << ": " << final << endl;
        }
        else{
            cout << "Case #" << i << ": " << "INSOMNIA" << endl;
        }
    }
    return 0;
}

