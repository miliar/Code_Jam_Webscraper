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

using namespace std;


int main(int argc, const char * argv[]) {
    
    
    FILE *fin = freopen("A-large.in", "r", stdin);
    assert( fin!=NULL );
    FILE *fout = freopen("A-large.out", "w", stdout);
    int times;
    string number;
    int digit;
    int num;
    int num2;
    string cast_back;
    vector<int> data;
    string result;
    cin >> times;
    for (size_t i = 0; i < times; ++i) {
        cin >> number;
        
        if (number.size() == 1 && number[0] == '0') {
            result = "INSOMNIA";
        } else {
            num = atoi(number.c_str());
            num2 = num;
            cast_back = to_string(num);
            while (data.size() != 10) {
                for (size_t l = 0; l < cast_back.size(); ++l) {
                    bool found = false;
                    for (size_t m = 0; m < data.size(); ++m) {
                        if (data[m] == (cast_back[l] - '0')) {
                            found = true;
                        }
                    }
                    if (found == false) {
                        digit = cast_back[l] - '0';
                        //cout << "  " << digit << " " << data.size() << endl;
                        data.push_back(digit);
                    }
                }
                num = num + num2;
                cast_back = to_string(num);
                //cout <<  "num:" << num << endl;
                
            }
            result = to_string(num - num2);
        }
        data.clear();
        cout << "Case #" << (i + 1) << ": " << result;
        cout << "\n";
        
        
        
        data.clear();
    }
    
    exit(0);
}
