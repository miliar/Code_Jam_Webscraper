//
//  main.cpp
//  Coin Jam
//
//  Created by Yunfei Lu on 4/9/16.
//  Copyright © 2016 googleCodeJam. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <bitset>
using namespace std;

int main(int argc, const char * argv[]) {
    ifstream file("B-small-attempt1.in");
    int caseNumber = 0;
    file >> caseNumber;
    int N;
    int J;
    long long sum;
    bool isNotPrime = false;
    bool isjamcoin = true;
    bool middleIsFull = true;
    int middleValue = 0;
    string middleString;
    int temp;
    file >> N;
    file >> J;
    string jamcoin;
    for (int i = 0; i < N; i++) {
        jamcoin += "0";
    }
    jamcoin[0] = '1';
    jamcoin[N - 1] = '1';
    vector<long long> divisors;
    divisors.resize(9);
    cout << "Case #1:" << endl;

    while (J > 0) {
        isjamcoin = true;
        //cout << "hello" << endl;
        for (int base =  2; base <= 10; base++) {
            sum = 0;
            isNotPrime = false;
            middleIsFull = true;
            for (int i = N - 1,digit = 0; i >= 0;i--,digit++) {
                if (jamcoin[i] == '1') {
                    sum += pow(base, digit);
                }
            }

            for (long long l = 2; l * l < sum; l++) {
                if (sum % l == 0) {
                    isNotPrime = true;
                    divisors[base - 2] = l;
                    break;
                }
            }
            if (isNotPrime) {
                continue;
            } else {isjamcoin = false;break;}
        }
        
        if (isjamcoin) {
            cout << jamcoin <<" ";
            J--;
            for ( auto &i: divisors) {
                cout << i << " ";
            }
            cout << endl;
        }
        middleString = bitset<14>(middleValue).to_string();
//        for (int i = middleString.size() - 1; i >= middleString.size() - N + 2 ; i--) {
//            if (middleString[i] == '0') {
//                middleIsFull = false;
//                break;
//            }
//        }
        if (middleString == "11111111111111") {
            break;
        }

        
        middleValue++;
        middleString = bitset<14>(middleValue).to_string();
//        for (int i = middleString.size() - 1, j = N - 2; i >= middleString.size() - N + 2 ; i--,j--) {
//            jamcoin[j] = middleString[i];
//        }
        jamcoin = '1' + middleString + '1';
        //cout << jamcoin << endl;
        
        
    }
    //string middleString = bitset<16>()

    return 0;
}
