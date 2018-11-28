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
    int num_case;
    cin >> num_case;
    string pan_cakes;
    getline(cin, pan_cakes);
    
    int i = 1;
    while (i <= num_case) {
        
        getline(cin, pan_cakes);
        
        int result = 0;
        if (pan_cakes.length() == 1) {
            result = (pan_cakes == "+") ? 0:1;
        }
        else {
            int first = 1, second = 0;
            while (first < pan_cakes.length()) {
                if (pan_cakes[second] != pan_cakes[first]) {
                    result ++;
                }
                
                first++;
                second++;
            }
            if (pan_cakes[first - 1] == '-') result++;
        }
        
        
        cout << "Case #" << i << ": " << result << endl;
        i++;
    }
    return 0;
}
