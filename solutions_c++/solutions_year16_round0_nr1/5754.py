//
//  main.cpp
//  CountingSheep
//
//  Created by Yunfei Lu on 4/9/16.
//  Copyright © 2016 googleCodeJam. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <unordered_map>
using namespace std;
int main() {
    ifstream file("A-small-attempt0.in");
    vector<int> aVector;
    int value = 0;
    if (file.fail() == false) {
        file >> value;
        aVector.resize(value);
        for (int i = 0; i < aVector.size(); i++) {
            file >> value;
            aVector[i] = value;
        }
    }
    
    int N = 0;
    int temp;
    int digit;
    int base;
    bool stop = false;
    unordered_map<int, int> contains;
    
    for(int i = 0; i < aVector.size();i++) {
        N = aVector[i];
        base = N;
        temp = N;
        int k = 2;
        contains.clear();
        
        while (true) {
            if (N == 0) {
                cout << "Case #" <<i+1 <<": " << "INSOMNIA" << endl;
                break;
            }
            while( temp > 0) {
                digit = temp % 10;
                temp /= 10;
                if (contains.find(digit) == contains.end()) {
                    contains[digit] = 1;
                }
            }
            if (contains.size() == 10) {
                cout << "Case #" <<i+1 <<": " << N << endl;
                break;
            }
            N = base * k;
            temp = N;
            k++;
        }
        
    }
    return 0;
}
