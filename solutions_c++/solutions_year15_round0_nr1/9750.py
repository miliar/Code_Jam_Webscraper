//
//  main.cpp
//  Ovation
//
//  Created by Christian Kisczio on 11.04.15.
//  Copyright (c) 2015 Christian Kisczio. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

#define ADR "***"

using namespace std;



int main(int argc, const char * argv[]) {
    freopen("" ADR "input.in", "rt", stdin);
    freopen("" ADR "output.in", "w", stdout);
    
    int T = 0;
    int SMax;
    int O[1010];
    int num;
    int standing;
    int needed;
    
    cin >> T;
    
    for(int i =1; i<=T; i++){
        standing = 0;
        needed =0;
        for (int loop=0; loop < 1010; loop++){
            O[loop] = 0;
        }
        cin >> SMax;
        cin >> num;
        for(int f = 0; f<=SMax; f++){
            O[SMax - f] = num % 10;
            num = (num - (num%10))/10;
        }
        for(int g=0; g<=SMax; g++){
            
            while(g>standing){
                needed++;
                standing++;
            }
            standing = standing + O[g];
        }
        cout << "Case #" << i << ": " << needed << endl;
    }
    
}
