//
//  main.cpp
//  GCJ-Standing Ovation
//
//  Created by Akhil Verghese on 4/11/15.
//  Copyright (c) 2015 Akhil Verghese. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>

using namespace std;

int getInt (char c) {
    return (int)c - '0';
}

int main(int argc, const char * argv[]) {
    int t, x = 0;
    cin>>t;
    int ans, sMax, standingUp;
    string in;
    while (t--) {
        x++;
        ans = 0;
        standingUp = 0;
        cin>>sMax>>in;
        for (int i = 0; i < sMax + 1; i++) {
            if (standingUp < i) {
                ans+= (i - standingUp);
                standingUp = i;
            }
            standingUp += getInt(in[i]);
        }
        cout<<"Case #"<<x<<": "<<ans<<endl;
    }
    
    return 0;
}
