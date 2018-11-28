#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <algorithm>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forn1(i, n) for (int i = 1; i <= (int)(n); i++)

int main() {

    ifstream fin ("input.txt");
    ofstream fout ("output.out");
    bool a[100];
    string b,c,gold,base;
    
    int i,j,k,t,T,B,N,out,K,C,p,S;
   
    fin >> T;
    
    forn1(t,T) {
    
    	fin >> K >> C >>S;
    
        fout<<"Case #"<<t<<": ";
        
        forn1(i,K) fout<<i<<' ';
        fout<<'\n';
    
    }
    
    fin.close();
    fout.close();
    return 0;
}
