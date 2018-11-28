//
//  main.cpp
//  Google Code Jam
//
//  Created by Bryan Gonzales Vega on 4/11/15.
//  Copyright (c) 2015 Renovatio Technologies. All rights reserved.
//

#include <iostream>
#include <stdio.h>

using namespace std;

/// 0 -> richard
/// 1 -> gabriel

bool winningFormula(int x, int r , int c){
    int availableCells = r * c;

    if(x == 4 && r == 4 && c == 4){
        return 1;
    }
    if( (x == 4 && r == 4 && c == 2) || (x == 4 && r == 2 && c == 4) ){
        return 0;
    }
    else if(availableCells < x){ /// Not enough space
        return 0; /// Richard
    }
    else if(availableCells == x){ /// Its a straight line or perfect shape
        if( availableCells == 1 &&  r == 1 &&  c == 1 ){
            return 1;
        }
        else if (availableCells == 2){
            return 1;
        }
        else{
            return 0; /// Richard
        }
    }
    else if( availableCells % x == 0 ){ /// Even
        return 1; /// Gabriel
    }
    else{ /// Odd
        return 0; // Richard
    }
}


int main(int argc, const char * argv[]) {
    int testCases;
    int x,r,c;
    
    cin >> testCases;

    for( int i = 0 ; i < testCases ; ++i ){
        cin >> x >> r >> c;
        
//        printf("%i %i %i Case #%i: %s\n",x,r,c, i+1, winningFormula(x, r, c) == 0 ? "RICHARD":"GABRIEL" );
        printf("Case #%i: %s\n", i+1, winningFormula(x, r, c) == 0 ? "RICHARD":"GABRIEL" );
    }
    
    return 0;
}
