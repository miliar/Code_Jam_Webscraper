//
//  main.cpp
//  PalindromeSq
//
//  Created by Stephen Zhu on 4/13/13.
//  Copyright 2013 University of Michigan. All rights reserved.
//

#include <iostream>
#include <math.h>
#include <fstream>

using namespace std;

bool isPal(int x){
    int temp = x;
    int reverse = 0;
    while ( temp ){
        reverse = 10 * reverse + temp%10;
        temp /= 10;
    }
    
    if (reverse == x){
        return true;
    }
    
    else 
        return false;
    
}

int main ()
{

    int T;
    ifstream in("test.txt");
    ofstream out("palin.txt");
    
    int round = 1; 
    in >> T;
    while (round <= T){
        int A, B;
        in >> A >> B;
        int count = 0;
        int low = ceil(sqrt(A));
        int high = floor(sqrt(B));
        for (int i = low; i <= high; i++){
            if (isPal (i) && isPal(i*i)){
                count++;
            }
        }
        out << "Case #" << round << ": " << count << endl;
        
        round++;
    }
    
    
    return 0;
}

