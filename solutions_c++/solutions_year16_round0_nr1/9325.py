//
//  sh.cpp
//
//
//  Created by Pedro Abraham Moreno Vazquez on 09/04/16.
//
//

#include <stdio.h>
#include<iostream>


using namespace std;

unsigned int ndigit(int n){
    int div=1;
    int m=0;
    while (n/div!=0) {
        div=div*10;
        m++;
    }
    return m;
}

bool buscarN(int ar[],int n){
    int k=0,j=0;
    while (k<10) {
        if (ar[k]!=n) {
            j++;
        }
        k++;
        
        
    }
    if (j==10) {
        return true;
    }
    else return false;
}

int pot(int n,int potencia){
    int m=1;
    for (int i=1; i<=potencia; i++) {
        m=m*n;
    }
    return m;
}

bool arFull(int ar[]){
    return true;
}


int main(){
    
    int t=0;
    cin>>t;
    if (t<1 || t>100) {
        return 0;
    }
    int arT[t];
    int i;
    for ( i = 0; i < t; i++) {
        std::cin >> arT[i];
    }
    
    
    
    for ( i = 0; i < t; i++) {
        int j=0;
        int arNum[10]={-2,-2,-2,-2,-2,-2,-2,-2,-2,-2};
        int N=arT[i];
        if (N<0 || N>1000000) {
            continue;
        }
        
        if (N==0) {
            
            cout <<"Case #"<<i+1<<": INSOMNIA"<< std::endl;
        }
        else{
            int count=1;
            bool boole=true;
            while (boole) {
                int m=N*count;
                int n=m;
                int digitoprin=ndigit(m);
                
                
                while (digitoprin>0 && boole) {
                    int div=pot(10,ndigit(n)-1);
                    
                    if (buscarN(arNum,n/div)) {
                        arNum[j]=n/div;
                        j++;
                    }
                    n=n%div;
                    
                    if (j==10) {
                        cout <<"Case #"<<i+1<<": "<< m << std::endl;
                        boole=false;
                        
                    }
                    digitoprin--;
                }
                count++;
            }}
        
        
        
    }
    return 0;
    
    
}