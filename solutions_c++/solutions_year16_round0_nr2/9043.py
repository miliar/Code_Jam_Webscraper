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
    FILE *fin = freopen("/Users/rayhwang/Projects/CodeJam/2016/Qual-B/B-large.in", "r", stdin);
    assert( fin!=NULL );
    freopen("/Users/rayhwang/Projects/CodeJam/2016/Qual-B/B-large.out", "w", stdout);
    
    int T;
    cin >> T;
    
    for(int t = 1; t <= T; t++){
        
        string stack;
        cin >> stack;
        
        int len = (int)stack.length();

        fprintf(stderr, "Case: %d\t%s\n", t, stack.c_str());

        int numOfFlips = 0;
        
        // Check if already complete
        bool done = true;
        
        for(int i=0; i<len; i++) {
            if (stack[i] != '+') {
                done = false;
                break;
            }
        }
        
        while (!done) {
            if (t == 8) {
                
            }
            char topSign = stack[0];
            int pointer = 0;
            
            while (topSign == stack[pointer]) {
                pointer++;
            }
            
            for (int i=0; i<pointer; i++) {
                stack[i] = stack[i] == '-' ? '+' : '-';
            }
            
            for (int i=0; i<pointer / 2; i++) {
                char temp = stack[i];
                stack[i] = stack[pointer - 1 - i];
                stack[pointer - i] = temp;
            }
            numOfFlips++;
          
            if (stack[0] == '-') {
                done = true;
                for(int i=0; i<len; i++) {
                    if (stack[i] != '-') {
                        done = false;
                        break;
                    }
                }
                if (done) {
                    numOfFlips++;
                }
            } else {
                done = true;
                for(int i=0; i<len; i++) {
                    if (stack[i] != '+') {
                        done = false;
                        break;
                    }
                }
            }
        }
        

        
        cout << "Case #" << t << ": ";
        cout << numOfFlips << endl;

        fprintf(stderr, "Case #%d: %d", t, numOfFlips);
        fprintf(stderr, "\n\n");
    }
    exit(0);
}
