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
int check(int * m1,int * m2, int s,int &re){
    int count=0;
    for(int i=0;i<s;i++){
        for(int j=0;j<s;j++){
            if(m1[i]==m2[j]){
                count++;
                re=m1[i];
            }
        }
    }
    //cout<<count;
    return count;
}

int * ReadMatrix(ifstream *in,int s,int n){
    int * m=(int *)malloc(sizeof(int)*s);
    int tmp;
    for(int i=0;i<s;i++){
        if(i==n-1){
            for(int j=0;j<s;j++)(*in)>>m[j];
        }else{
            for(int j=0;j<s;j++)(*in)>>tmp;
        }
    }
    return m;
}

void PrintResult(int r,int i,int re){
    if(r==0)cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
    if(r==1)cout<<"Case #"<<i+1<<": "<<re<<endl;
    if(r>1)cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
}

int main(int argc, const char * argv[])
{
    ifstream fin("data.txt");
    int NumberOfTricks,n1,n2,re;
    int * m1;
    int * m2;
    int m=4;  //Size of the matrix
    fin>>NumberOfTricks;
    for(int i;i<NumberOfTricks;i++){
        fin>>n1;
        m1=ReadMatrix(&fin, m, n1);
        fin>>n2;
        m2=ReadMatrix(&fin, m, n2);
        PrintResult(check(m1,m2,m,re),i,re);
        //cout<<n1<<" "<<n2<<endl;
    }
    // insert code here...
    return 0;
}

