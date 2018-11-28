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

string getlastNum(long long n) {
    if (n == 0) {
        return "INSOMNIA";
    }
    unordered_set<int> digits;
    long long sum = n;
    int len = log10(n) + 1;
    while (digits.size() < 10) {
        for (int i = 0; i < len + 1; ++i) {
            long long tmp = sum / (long)pow(10, i);
            if (tmp == 0) {
                break;
            }
            digits.insert(tmp % 10);
        }
        if (digits.size() < 10) {
            sum += n;
        }
    }
    return to_string(sum);
}

string bruteforce(long long n) {
    if (n == 0) {
        return "INSOMNIA";
    }
    unordered_set<int> digits;
    long long sum = n;
    while (digits.size() < 10) {
        long long tmp = sum;
        while (tmp > 0) {
            digits.insert(tmp % 10);
            tmp /= 10;
        }
        if (digits.size() < 10) {
            sum += n;
        }
    }
    return to_string(sum);
}

int main(){
    int times = 0, k = 1;
    long long n;
    cin >> times;
    while (times--) {
        cin >> n;
        cout << "Case #" << k++ << ": " << getlastNum(n) << endl;
    }
}