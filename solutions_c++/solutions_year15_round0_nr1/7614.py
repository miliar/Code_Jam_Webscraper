/* 
 * File:   standing_ovation.cc
 * Author: vivek
 *
 * Created on April 11, 2015, 11:54 AM
 */

#include <cstdlib>
#include <algorithm>
#include <iostream>

using namespace std;

#define Int   int
#define UInt unsigned  Int 


/*
 * 
 */
int main(int argc, char** argv) {
    UInt t;
    cin >> t;
    for(UInt i=1;i<=t;i++){
        UInt s;
        cin>> s;
        UInt required = 0;
        UInt totalCapacity= 0;
        string capacityString;
        cin >> capacityString;
        for(UInt j=0; j<=s ;j++){
            UInt capacity  = capacityString.at(j) - '0';                        
            UInt currentRequired = max(0,int(min(j,j*capacity) - totalCapacity));
            required += currentRequired;   
            totalCapacity += capacity + currentRequired;
        }
        cout << "Case #" << i <<": " << required << endl;
    }
    return 0;
}

