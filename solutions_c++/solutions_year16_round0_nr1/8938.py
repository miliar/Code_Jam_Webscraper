//
//  main.cpp
//  CodeJam2016
//
//  Created by Ray Hwang on 4/9/16.
//  Copyright © 2016 Original Function. All rights reserved.
//

#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>

using namespace std;

int main()
{
    FILE *fin = freopen("/Users/rayhwang/Projects/CodeJam/2016/Qual-A/A-small-attempt0.in", "r", stdin);
    assert( fin!=NULL );
    freopen("/Users/rayhwang/Projects/CodeJam/2016/Qual-A/A-small-attempt0.out", "w", stdout);
    
    int T;
    cin >> T;
    
    for(int t = 1; t <= T; t++){
        
        int n;
        cin >> n;
        
        int curr = n;
        
        bool digits[10] = { 0 };
        
        if (curr == 0) {
            cout << "Case #" << t << ": INSOMNIA" << endl;
        } else {
            
            bool done = false;
            
            while (!done) {
                int copy = curr;
                while (copy > 0) {
                    int digit = copy % 10;
                    digits[digit] = true;
                    copy /= 10;
                }
                
                bool check = true;
                for (int i=0; i<10; i++) {
                    if (digits[i] == false) {
                        check = false;
                        break;
                    }
                }
                
                if (check == true) {
                    done = true;
                } else {
                    curr += n;
                }
            }
            
            cout << "Case #" << t << ": ";
            cout << curr << endl;
        }
    }
    exit(0);
}