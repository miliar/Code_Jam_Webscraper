//
//  main.cpp
//  Bullseye
//
//  Created by jiusi on 4/27/13.
//  Copyright (c) 2013 jiusi. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, const char * argv[])
{
    ifstream cin("/Users/jiusi/Downloads/A-small-attempt01.in");
    
    int count = 0;
    cin >> count;
    
    for(int c = 0; c < count; c++) {
        long long r;
        long long t;
        cin >> r >> t;
        long long cnt = 0;
        long long outr = 1 + r;
        long long inr = r;
        while(true) {
            long long cost = outr* outr - inr*inr;
            if(cost <= t) {
                t-=cost;
                cnt++;
            } else {
                break;
            }
            
            outr = cnt*2+1 + r;
            inr = cnt*2 + r;
        }
        
        
        cout << "Case #" << c+1 << ": " << cnt << endl;
        
    }
    
}

