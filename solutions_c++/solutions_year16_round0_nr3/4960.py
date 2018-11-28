//
//  main.cpp
//  test
//
//  Created by Haoliang on 7/27/15.
//  Copyright (c) 2015 Haoliang. All rights reserved.
//

#include <iostream>
#include <cmath>
#include <vector>
#include <mutex>
#include <sstream>
#include <algorithm>
#include <string>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <map>
#include <set>
#include <sstream>
#include <cstdlib>
#include <ctime>
#include <chrono>
#include <thread>
#include <bitset>
#include <cmath>
#include <fstream>
#include <iterator>

#include "test.h"

using namespace std;

long long getnum(long long num, int base){
    long long res = 0;
    int k = 0;
    while (num > 0) {
        if ((num & 1) == 1) {
            res += pow(base, k);
        }
        num >>= 1;
        k++;
    }
    return res;
}

long long getfactor(long long num) {
    for (long long i = 2; i < sqrt(num); ++i) {
        if (num % i == 0) {
            return i;
        }
    }
    return 1;
}

string getbinary(long long n) {
    string res;
    while (n > 0) {
        if ((n & 1) == 1) {
            res.push_back('1');
        }else {
            res.push_back('0');
        }
        n >>= 1;
    }
    reverse(res.begin(), res.end());
    return res;
}

int main(){
    int n = 16, j = 50;
    unordered_set<string> res;
    cout << "Case #1:" << endl;
    long long num = pow(2, 15) + 1;
    int k = 0;
    while (k < j) {
        vector<long long> factors;
        bool f = false;
        for (int base = 2; base <= 10; base++) {
            long long cur = getnum(num, base);
            long long x = getfactor(cur);
            if (x == 1) {
                f = true;
                break;
            }
            factors.push_back(x);
        }
        if (f) {
            num += 2;
            continue;
        }
        cout << getbinary(num);
        for (int i = 0; i < factors.size(); ++i) {
            cout << " " << factors[i];
        }
        cout << endl;
        k++;
        num += 2;
    }
}