//
//  main.cpp
//  GJamTemplate
//
//  Created by Lyamani Moulay Abdellatif on 13/04/13.
//  Copyright (c) 2013 Lyamani Moulay Abdellatif. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <string>
#include <cstring>
#include <algorithm>
#include <math.h>

using namespace std;
#define LINESZ 1024


bool isSymetricNbr(const int nbr) {
    
    int num = nbr;
    vector<int> digits;
    int sum = 0;
    while(num > 0)
    {
        digits.push_back(num % 10);
        num = num / 10;
    }
    long i = digits.size()-1;
    int coef = 1;
    while (i >= 0) {
        sum += digits.at(i)*coef;
        coef = coef*10;
        i=i-1;
    }
    return sum==nbr;
}

bool isFairAndSquare(const int nbr){
    if(!isSymetricNbr(nbr))
        return false;
    else{
        double x = sqrt(nbr);
        double floorx = floor(x);
        bool validInteger = (x==floorx);
        
        if(validInteger && isSymetricNbr(x))
            return true;
        else
            return false;
    }
}

int cptNbrSym(const int A, const int B)
{
    int res = 0;
    for (int x = A; x<=B; x++) {
        if(isFairAndSquare(x))
            res++ ;
    }
    return res;
}

int main(int argc, const char * argv[])
{
    freopen("/Users/lyamanimoulay/Project Dev/Google Jam/GJamTemplate/GJamTemplate/output.in","w", stdout);
    FILE* IN = freopen("/Users/lyamanimoulay/Project Dev/Google Jam/GJamTemplate/GJamTemplate/input.in","r", stdin);
     int test,cases, A, B;
    
    char str[LINESZ] ;

    cases=0;
    scanf("%d",&test);
    fgets (str, LINESZ, IN) ;
    while (test){
        test--;
        cases++;
        scanf("%d",&A);
        scanf("%d",&B);
        
        int res = cptNbrSym(A, B);
        
        cout<<"Case #"<<cases<<": "<< res << endl;
        
    }
    return 0;
}

