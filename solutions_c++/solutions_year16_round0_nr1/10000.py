//
//  main.cpp
//
//
//  Created by Aaron Ruel on 3/11/16.
//  Copyright (c) 2016 AAR. All rights reserved.
//

#include <iostream>
#include <cstring>
#include <vector>

#define ASCII_OFFSET 48

bool truthArray(bool (&arr)[10]);

void setArray(bool (&arr)[10], int set);

int main(int nargs, char** argv)
{
    int getCount;
    std::cin >> getCount;
    
    for(int i = 0; i < getCount; ++i){
        bool arr[10] = {false};
        
        std::string eval;
        std::cin >> eval;
        
        unsigned long long n = atoi(eval.c_str());
        
        if(eval != "0"){
            unsigned long long store = 0;
            int TC = 1;
            while(!truthArray(arr)){
                for(int j = 0; j < eval.length(); ++j){
                    arr[(int)eval[j] - ASCII_OFFSET] = true;
                }
                ++TC;
                if(truthArray(arr)) std::cout << "Case #" << i+1 << ": " << store << '\n';
                store = n * TC;
                eval = std::to_string(store);
            }
        }
        else {
            std::cout << "Case #" << i+1 << ": " << "INSOMNIA\n";
        }
    }
}

bool truthArray(bool (&arr)[10]){
    bool flag = true;
    for(int i = 0; i < 10; ++i) if(arr[i] == false) flag = false;
    return flag;
}

void setArray(bool (&arr)[10], int set){
    
}