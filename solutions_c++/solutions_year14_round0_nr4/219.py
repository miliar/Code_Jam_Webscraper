//
//  main.cpp
//  MagicTrick
//
//  Created by frank on 4/11/14.
//  Copyright (c) 2014 frank. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;
static int compare (const void * a, const void * b)
{
    if (*(double*)a > *(double*)b) return 1;
    else if (*(double*)a < *(double*)b) return -1;
    else return 0;
}



int calculateWar(double *A,double *B,int round){
    int re=0;
    int j=0;
    //double * tmp=(double *)malloc(sizeof(double));
    for(int i=0;i<round;i++){
        for(;j<round;j++){
            if(A[i]<B[j]){
                re++;
                j++;
                break;
            }
        }
    }
    return re;
}
int main(int argc, const char * argv[])
{
    ifstream fin("data4.txt");
    int NumberOfTricks;
    int n;
    int re;
    int dre;
    fin>>NumberOfTricks;
    for(int i;i<NumberOfTricks;i++){
        fin>>n;
        double *m1=(double *)malloc(sizeof(double)*n);
        double *m2=(double *)malloc(sizeof(double)*n);
        for(int i=0;i<n;i++){
            fin>>m1[i];
        }
        for(int i=0;i<n;i++){
            fin>>m2[i];
        }
        qsort(m1, n, sizeof(double), compare);
        qsort(m2, n, sizeof(double), compare);
        re=calculateWar(m1,m2,n);
        dre=calculateWar(m2,m1,n);
        cout<<"Case #"<<i+1<<": "<<fixed<<dre<<" "<<n-re<<endl;
    }
    // insert code here...
    return 0;
}

