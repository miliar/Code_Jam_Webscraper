//
//  main.cpp
//  Google Code Jam
//
//  Created by Vivek Vichare on 4/9/16.
//  Copyright © 2016 Vivandro. All rights reserved.
//

#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <fstream>
#include <sstream>
#include <iomanip>

using namespace std;
typedef vector <int> vi;
typedef vector<vi> vvi;
typedef unsigned long long ull;

string process_testcase_A()
{
    long long N;
    cin >> N;

    if (N == 0) {
        return "INSOMNIA";
    }
    
    ull flags[] = {
        1ULL << 0,
        1ULL << 1,
        1ULL << 2,
        1ULL << 3,
        1ULL << 4,
        1ULL << 5,
        1ULL << 6,
        1ULL << 7,
        1ULL << 8,
        1ULL << 9,
    };
    
    auto digitsFound = [&](ull n)->ull {
        ull found = 0;
        do {
            ull q = n / 10;
            ull r = n % 10;
            found |= flags[r];
            n = q;
        } while (n);
        return found;
    };
    
    // We have counted enough sheep when seen == target
    ull seen = 0;
    ull target = 0x3FF;

    // First get rid of all the zeros on the right hand side
    ull quot = 0;
    ull powOfTen = 0;
    while ((quot = N/10) * 10 == N) {
        seen |= flags[0];
        N = quot;
        ++powOfTen;
    }
    
    if (N == 0) {
        return "INSOMNIA";
    }
    
    ull lastNum = N;
    for (ull multiple = 1; (seen != target); ++multiple) {
        lastNum = multiple * N;
        seen |= digitsFound(lastNum);
    }

    lastNum *= pow(10, powOfTen);
    char numC_str[1000];
    sprintf(numC_str, "%llu", lastNum);
    return string(numC_str);
}

ull process_testcase_B()
{
    string pancakes;
    cin >> pancakes;
    
    ull flips = 0;
    char prev = '+';
    auto rend = pancakes.rend();
    for (auto i = pancakes.rbegin(); i != rend; ++i) {
        if (*i != prev) {
            prev = *i;
            ++flips;
        }
    }
    return flips;
}

int main(int argc, char*argv[]) {
    int tc = 0;
    if(argc == 1) {
        freopen("/Users/vivandro/Downloads/inp.txt", "r", stdin);
        //freopen("outp.txt", "w", stdout);
    }
    else {
        freopen(argv[1], "r", stdin);
        //freopen("outp.txt", "w", stdout);
    }
    freopen("/Users/vivandro/Downloads/outp.txt", "w", stdout);
    
    // find total number of testcases
    cin >> tc;
    
    // for every testcase
    for(int i = 1; i <= tc; i++)
    {
        printf("Case #%d: ",i);
        cout << process_testcase_A();
        cout << endl;
    }
    
    return 0;
}
