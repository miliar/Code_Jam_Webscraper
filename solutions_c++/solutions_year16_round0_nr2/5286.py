//
//  main.cpp
//  Google Practice 1
//
//  Created by Ruowen Tan on 4/7/16.
//  Copyright (c) 2016 Ruowen Tan. All rights reserved.
//

#include <iostream>
#include <cassert>
#include <vector>
#include <cstdlib>
#include <string>

using namespace std;


int main(int argc, const char * argv[]) {
    
    
    FILE *fin = freopen("B-large.in", "r", stdin);
    assert( fin!=NULL );
    FILE *fout = freopen("B-large.out", "w", stdout);
    int times;
    int result = 0;
    int index = 1;
    string head_tail;
    char current;
    cin >> times;
    for (size_t i = 0; i < times; ++i) {
        cin >> head_tail;
        current = head_tail[0];
        
        if (head_tail.size() == 1) {
            if (current == '+') {
                result = 0;
            } else {
                result = 1;
            }
        } else {
            while (index < head_tail.size()) {
                if (current != head_tail[index]) {
                    result++;
                    current = head_tail[index];
                }
                index++;
            }
            if (current == '-') {
                result++;
            }
        }
        
        cout << "Case #" << (i + 1) << ": " << result;
        cout << "\n";
        
        result = 0;
        index = 1;
        

    }
    
    exit(0);
}
