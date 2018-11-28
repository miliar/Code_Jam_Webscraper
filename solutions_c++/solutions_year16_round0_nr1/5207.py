//
//  main.cpp
//  codejam2016A
//
//  Created by Daniel Pompe on 09.04.16.
//  Copyright © 2016 DP. All rights reserved.
//

#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    FILE *fin = freopen("test.in", "r", stdin);
    FILE *fout = freopen("test.out", "w", stdout);
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        cout << "Case #" << t << ": ";
        uint64_t n;
        cin >> n;
        if(n == 0)
        {
            cout << "INSOMNIA" << endl;
            continue;
        }
        bool digits[10] = {};
        int named = 0;
        bool valid = true;
        while(!digits[0]
              || !digits[1]
              || !digits[2]
              || !digits[3]
              || !digits[4]
              || !digits[5]
              || !digits[6]
              || !digits[7]
              || !digits[8]
              || !digits[9])
        {
            named += n;
            uint64_t tmp = named;
            while(tmp)
            {
                digits[tmp % 10] = true;
                tmp /= 10;
            }
            if(named > numeric_limits<uint64_t>::max() - n)
            {
                valid = false;
                break;
            }
        }
        if(valid)
            cout << named << endl;
        else
            cout << "INSOMNIA" << endl;
    }
    exit(0);
}
