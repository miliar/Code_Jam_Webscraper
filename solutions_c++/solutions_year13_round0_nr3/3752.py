//
//  main.cpp
//  FS
//
//  Created by jiusi on 4/13/13.
//  Copyright (c) 2013 jiusi. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int main(int argc, const char * argv[])
{
    ifstream cin("/Users/jiusi/Downloads/C-small-attempt0.in");
    int n;
    cin >> n;
    
    int casenum = 0;
    for(int i = 0; i<n; i++) {
        long long s;
        long long e;
        cin >> s >> e;
        
        long long check = s;
        long long seed = sqrt(check);
        if(seed * seed < check){
            check = (++seed)*(seed);
        } else if(seed * seed > check) {
            check  = seed * seed;
        }
        long count = 0;
        while(check <= e) {
            string s_check = to_string(check);
            string s_seed = to_string(seed);
            if(s_check == string(s_check.rbegin(), s_check.rend()) &&
                s_seed == string(s_seed.rbegin(), s_seed.rend())) {
                count++;
            }
            seed++;
            check = seed * seed;
        }
        
        cout << "Case #" << ++casenum << ": " << count << endl;
    }
    
    return 0;
}

