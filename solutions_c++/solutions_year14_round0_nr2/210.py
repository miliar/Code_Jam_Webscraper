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

void PrintResult(int i,double re){

    cout.precision(7);
    cout<<"Case #"<<i+1<<": "<<fixed<<re<<endl;

}

double calculate(double C,double F,double X){
    double re=0;
    double speed=2;
    while(((X-C)/speed)>(X/(speed+F))){
        re+=C/speed;
        speed+=F;
    }
    return X/speed+re;
}
int main(int argc, const char * argv[])
{
    ifstream fin("data2.txt");
    int NumberOfTricks;
    double C,F,X,re=0;
    fin>>NumberOfTricks;
    for(int i;i<NumberOfTricks;i++){
        fin>>C>>F>>X;
        re=calculate(C,F,X);
        PrintResult(i,re);
        //cout<<n1<<" "<<n2<<endl;
    }
    // insert code here...
    return 0;
}

