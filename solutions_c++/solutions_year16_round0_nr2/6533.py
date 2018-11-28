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

int minflip(string str) {
    int ops = 0;
    char last = str[0];
    for (int i = 1; i < str.size(); ++i) {
        if (str[i] == str[i - 1]) {
            continue;
        }
        ops++;
        last = str[i];
    }
    if (last == '-') {
        ops++;
    }
    return ops;
}

int main(){
    int times = 0, k = 1;
    string str;
    cin >> times;
    while (times--) {
        cin >> str;
        cout << "Case #" << k++ << ": " << minflip(str) << endl;
    }
}