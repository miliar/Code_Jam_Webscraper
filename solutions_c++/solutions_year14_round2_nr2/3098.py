//
//  main.cpp
//  CodeJam - New Lottery Game
//
//  Created by Administrator on 5/3/14.
//  Copyright (c) 2014 Ryan. All rights reserved.
//

#include <iostream>

using namespace std;

int main(int argc, const char * argv[])
{

    int numCases;
    cin >> numCases;
    int numResults = 0;
    
    int A;
    int B;
    int K;
    
    for (int i = 1; i <= numCases; i++) {
        
        cin >> A >> B >> K;
        
        
        for (int j = 0; j < A; j++) {
            for (int x = 0; x < B; x++) {
                if ( (j & x) < K ) {
                    numResults++;
                }
            }
        }
        
        
        
        
        
        
        cout << "Case #" << i << ": " << numResults << endl;
        numResults = 0;
    }
    
    return 0;
}

