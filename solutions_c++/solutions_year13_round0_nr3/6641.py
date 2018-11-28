#include <stdio.h>
#include <math.h>
#include <iostream>
#include <algorithm>
#include <fstream>

#define forr(I, N) for(int I = 0; I < N; I++)
#define MAX 100

using namespace std;

int numDigitos(long long x){
    int acc = 1;
    while(x > 9 || x < -9){
        acc++;
        x /= 10;
    }
    return acc;
}

bool palindromo(long long x){
    long long aux = 0, aux2 = x;
    int num = numDigitos(x);
    forr(i, num){
        aux += (x%10) * pow(10, num-i-1);
        x /= 10;
    }
    if(aux == aux2) return true;
    else return false;
}

int main(){
    int n, acc;
    long long begin, end, aux;
    ifstream infile;
    ofstream outfile;
    outfile.open("output.txt");
    infile.open("C-small-attempt0.in");

    infile >> n;


    forr(i,n){
        acc = 0;
        infile >> begin >> end;
        aux = long(sqrt(begin));
        if(aux*aux < begin) aux++;
        for(int j = aux; j*j <= end; j++){
             if(palindromo(j) && palindromo(j*j)) acc++;
        }

        outfile << "Case #" << i+1 << ": " << acc << endl;
    }
    infile.close();
    outfile.close();
    return 1;
}

