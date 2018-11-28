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

typedef long long ll;
typedef vector <ll> vll;
typedef vector<vll> vvll;

typedef unsigned long long ull;
typedef vector <ull> vull;
typedef vector<vull> vvull;

typedef vector <string> vs;
typedef vector<vs> vvs;

void process_testcase_A()
{
    string S;
    cin >> S;
    
    int count[27] = {0};
    for (int i = 0; i < S.length(); ++i) {
        count[S[i]-'A']++;
    }
    map<char, int>firstPass;
    firstPass['Z'] = 0;
    firstPass['W'] = 2;
    firstPass['U'] = 4;
    firstPass['X'] = 6;
    firstPass['G'] = 8;
    map<char, int>secondPass;
    secondPass['O'] = 1;
    secondPass['T'] = 3;
    secondPass['F'] = 5;
    secondPass['S'] = 7;
    
    map<int, string>numToStr;
    numToStr[0] = "ZERO";
    numToStr[1] = "ONE";
    numToStr[2] = "TWO";
    numToStr[3] = "THREE";
    numToStr[4] = "FOUR";
    numToStr[5] = "FIVE";
    numToStr[6] = "SIX";
    numToStr[7] = "SEVEN";
    numToStr[8] = "EIGHT";
    numToStr[9] = "NINE";
    

    vector<int>number;
    auto pass = [&](map<char, int>&mapping){
        for (int i = 0; i < 26; i++) {
            if (count[i] == 0) {
                continue;
            }
            char ch = 'A'+i;
            if (mapping.find(ch) != mapping.end()) {
                int digit = mapping[ch];
                int occurrences = count[i];
                for (int k = 0; k < occurrences; k++) {
                    number.push_back(digit);
                }
                string strRepresentation = numToStr[digit];
                for (size_t j = 0; j < strRepresentation.length(); j++) {
                    int chIndex = strRepresentation[j] - 'A';
                    count[chIndex] -= occurrences;
                }
            }
        }
        
    };
    pass(firstPass);
    pass(secondPass);
    int numNines = count['N' - 'A']/2;
    
    for (int i = 0; i < numNines; i++) {
        number.push_back(9);
    }
    sort(begin(number), end(number));
    for (int i = 0; i < number.size(); i++) {
        cout << number[i];
    }
}

int main(int argc, char*argv[]) {
    int tc = 0;
    if(argc == 1) {
        freopen("/Users/vivandro/Downloads/inp.txt", "r", stdin);
    }
    else {
        freopen(argv[1], "r", stdin);
    }
    freopen("/Users/vivandro/Downloads/outp.txt", "w", stdout);
    
    // find total number of testcases
    cin >> tc;
    
    // for every testcase
    for(int i = 1; i <= tc; i++)
    {
        printf("Case #%d: ",i);
        process_testcase_A();
        cout << endl;
    }
    
    return 0;
}
