//
//  main.cpp
//  Oversized Pancake Flipper
//
//  Created by Rugen Heidbuchel on 08/04/2017.
//  Copyright © 2017 Rugen Heidbuchel. All rights reserved.
//

#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>

// Shortcuts for "common" data types in contests
typedef long long ll;
typedef std::vector<int> vi;
typedef std::pair<int, int> ii;
typedef std::vector<ii> vii;
typedef std::set<int> si;
typedef std::map<std::string, int> msi;

// To simplify repetitions/loops, Note: define your loop style and stick with it!
#define REP(i, a, b) \
for (int i = int(a); i <= int(b); i++) // a to b, and variable i is local!
#define TRvi(c, it) \
for (vi::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvii(c, it) \
for (vii::iterator it = (c).begin(); it != (c).end(); it++)
#define TRmsi(c, it) \
for (msi::iterator it = (c).begin(); it != (c).end(); it++)
#define INF 2000000000 // 2 billion

// If you need to recall how to use memset:
#define MEMSET_INF 127 // about 2B
#define MEMSET_HALF_INF 63 // about 1B
//memset(dist, MEMSET_INF, sizeof dist); // useful to initialize shortest path distances
//memset(dp_memo, -1, sizeof dp_memo); // useful to initialize DP memoization table
//memset(arr, 0, sizeof arr); // useful to clear array of integers


#pragma mark - MAIN

size_t T;
int K, flips;
std::string S;

char inverse(char c) {
    return c == '+' ? '-' : '+';
}

int main(int argc, const char * argv[]) {

    #ifdef USE_INPUT_FILE
    freopen("example_input.txt", "r", stdin);
    #endif
    
    std::cin >> T;
    for (size_t caseNumber = 0; caseNumber < T; caseNumber++) {
        
        std::cout << "Case #" << caseNumber + 1 << ": ";
        
        std::cin >> S >> K;
        flips = 0;
        
        int i = 0;
        while (i <= S.size() - K) {
            
            if (S[i] == '-') {
                ++flips;
                for (size_t j = 0; j < K; j++) {
                    S[i+j] = inverse(S[i+j]);
                }
            }
            
            ++i;
        }
        
        bool worked = true;
        for (size_t i = S.size() - K + 1; i < S.size(); i++) {
            if (S[i] == '-') {
                worked = false;
                break;
            }
        }
        
        if (worked) {
            std::cout << flips;
        } else {
            std::cout << "IMPOSSIBLE";
        }
        
        std::cout << "\n";
    }
    
    return 0;
}
