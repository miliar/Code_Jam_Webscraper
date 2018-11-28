#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>

#define Nmax 100

using namespace std;


int f(int A,int X[Nmax],int N){
    if(N==1){
        if(A>X[0])return 0;
        else return 1;
    }
    if(N<1)return 0;
    if(A==1){
        return N;
    }
    if(A>100000000){
        return N;
    }
    long long ans=0;
    while(1){
        int o=0;
        for(int i=0;i<N;i++){
            if(A>X[i]){
                A=A+X[i];
                for(int j=i;j<N-1;j++){
                    X[j]=X[j+1];
                }
                N--;
                o=1;
                if(N==1){
                    if(A>X[0])return 0;
                    else return 1;
                }
            }
        }
        if(o==0)break;
    }
    sort(X,X+N);
    ans=min(f(A,X,N-1)+1,f(A*2-1,X,N)+1);
    return ans;
}

int main()
{
    ifstream fin("A-small-attempt0.in");
    ofstream fout("A-small-attempt0.out");
    int T;
    fin>>T;
    for(int Ti=1;Ti<=T;Ti++){
        int A,N;
        fin>>A>>N;
        int X[Nmax];
        for(int i=0;i<N;i++){
            fin>>X[i];
        }
        fout<<"Case #"<<Ti<<": "<<f(A,X,N)<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}
