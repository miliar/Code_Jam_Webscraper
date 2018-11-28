//  Created by Lyamani Moulay Abdellatif on 11/04/2015.
//  Copyright (c) 2015 Lyamani Moulay Abdellatif. All rights reserved.
//

#include <iostream>
#include <vector>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

typedef long long LL;

#define LINESZ 1024

int main(int argc, const char * argv[])
{
    freopen("output.out","w", stdout);
    FILE* in = freopen("input.in","r", stdin);
    
    int test,cases;
    long Smax, N;
    char S[1024] ;
    
    char str[LINESZ] ;
    
    cases=0;
    scanf("%d",&test);
    fgets (str, LINESZ, in) ;
    while (test){
        test--;
        cases++;
        
        scanf("%lu", &Smax) ;
        scanf("%s", S) ;
        std::vector<int> vect ;
        int res = 0;
        N = 0;
        
        for (int i = 0; i <=Smax; i++) {
            vect.push_back(S[i]-'0');
            N += S[i] - '0' ;
        }
        
        for (long x = Smax; x>=0; x--) {
            N = N - vect.at(x);
            if( N < x ){
                res += x-N ;
                N += x-N ;
            }
        }

        cout<<"Case #"<<cases<<": "<< res <<endl;
    }
    return 0;
}

