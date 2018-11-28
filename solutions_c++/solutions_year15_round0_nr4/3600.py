//
//  main.cpp
//  ominoes
//
//  Created by Sebastian Corobado on 11/04/15.
//  Copyright (c) 2015 Sebastian Corobado. All rights reserved.
//

#include <iostream>
#include <stdio.h>

using namespace std;


int main(int argc, const char * argv[]) {
    int testCases;
    int x,r,c;
    bool b;
    cin >> testCases;
    
    for( int i = 0 ; i < testCases ; ++i ){
        cin >> x >> r >> c;
        
        int availableCells = r * c;
        
        if(x == 4 && r == 4 && c == 4){
            b=1;
        }
        else if( (x == 4 && r == 4 && c == 2) || (x == 4 && r == 2 && c == 4) ){
            b=0;
        }
        else if(availableCells < x){
            b=0;
        }
        else if(availableCells == x){
            if( availableCells == 1 &&  r == 1 &&  c == 1 ){
                b=1;
            }
            else if (availableCells == 2){
                b=1;
            }
            else{
                b=0;
            }
        }
        else if( availableCells % x == 0 ){
            b=1;
        }
        else{
            b=0;
        }
        printf("Case #%i: %s\n", i+1, b == 0 ? "RICHARD":"GABRIEL" );
    }
    
    return 0;
}

