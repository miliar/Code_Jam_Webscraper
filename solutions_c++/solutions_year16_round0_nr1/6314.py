//
//  main.cpp
//  hihi
//
//  Created by Ge Bian on 4/8/16.
//  Copyright (c) 2016 Ge Bian. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace  std;

int main(int argc, const char * argv[]) {
    unsigned long long num, n;
    cin >> num;
    
    vector<bool> got(10, false);
    unsigned long long i = 1;
    while (i <= num) {
        cin >> n;
        if (n == 0) {
            cout << "Case #" << i << ": INSOMNIA" << endl;
            i++;
            continue;
        }
        
        unsigned long long t = 1, count = 0;
        unsigned long long result = 0;
        got  = vector<bool>(10, false);
        while (true) {
            long long nt = n * t;
            result = nt;
            while (nt > 0) {
                unsigned long long digit = nt % 10;
                nt /= 10;
                if (!got[digit]) {
                    got[digit] = true;
                    count++;
                    if (count == 10) break;
                }
            }
            if (count == 10) break;
            t++;
        }
        cout << "Case #" << i << ": " << result << endl;
        
        i++;
    }
    return 0;
}
