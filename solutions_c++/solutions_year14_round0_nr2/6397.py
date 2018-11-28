//
//  main.cpp
//  codejam2014_Problem B. Cookie Clicker Alpha
//
//  Created by kimtaeyang on 2014. 4. 12..
//  Copyright (c) 2014년 kimtaeyang. All rights reserved.
//

#include <stdio.h>

struct X{
    int integer;
    double decimal;
    X(){
        integer=decimal=0;
    }
    bool operator<(X A){
        if(integer!=A.integer) return integer<A.integer;
        return decimal<A.decimal;
    }
    bool operator>(X A){
        if(integer!=A.integer) return integer>A.integer;
        return decimal>A.decimal;
    }
    void input(){
        scanf("%d%lf",&integer,&decimal);
    }
    void operator=(double A){
        integer=A;
        decimal=A-integer;
    }
    X operator/(X A){
        X imsi; double x,y;
        x = integer+decimal;
        y = A.integer+A.decimal;
        imsi = x/y;
        return imsi;
    }
    X operator+(X A){
        X imsi;
        imsi.integer=integer+A.integer;
        imsi.decimal=decimal+A.decimal;
        if(imsi.decimal>=1.0) imsi.integer+=1, imsi.decimal-=1;
        return imsi;
    }
    void output(){
        printf("%lf\n",(double)integer+decimal);
    }
};
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    int T,I;
    X C, F, X, time, min, V;
    
    scanf("%d",&T);
    for(I=1;I<=T;I++){
        C.input(); F.input(); X.input();
        V=2; time=0; min=X/V;
        while(time < min){
            if(min > time + X/V) min = time + X/V;
            time = time + C/V;
            V = V + F;
        }
        printf("Case #%d: %.8lf\n",I,(double)min.integer+min.decimal);
    }
    
    
}