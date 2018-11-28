//
//  main.cpp
//  b.cpp
//
//  Created by Duo Donald Zhao on 4/12/14.
//  Copyright (c) 2014 Duo Donald Zhao. All rights reserved.
//

#include <iostream>
#include <iomanip>
#include <cmath>
#include <set>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;

int main(int argc, const char * argv[])
{
    int N;
    cin >> N;
    for (int i = 0; i < N; i++) {
        int rounds;
        cin >> rounds;
        vector<double> Naomi(rounds);
        vector<double>  Ken (rounds);
        vector<int> played (rounds);
        for (int j = 0; j < rounds; j++) {
            cin >> Naomi[j];
        }
        for (int j = 0; j < rounds; j++) {
            cin >> Ken[j];
        }
        sort(Naomi.begin(), Naomi.end());
        sort(Ken.begin(), Ken.end());
        int score = 0;
        for (int j = 0; j < rounds; j++) {
            double challenge = Naomi[j];
            bool win = true;
            for (int k = 0; k < rounds; k++) {
                if (Ken[k] > challenge && played[k] == 0) {
                    played[k] = 1;
                    win = false;
                    break;
                }
            }
            if (win == true) {
                for (int tmp = 0; tmp < rounds; tmp++) {
                    if (played[tmp] == 0) {
                        played[tmp] = 1;
                        break;
                    }
                }
                score++;
            }
        }
        int cheat_score = 0;
        for (int j = 0; j < rounds; j++) {
            bool win_rest = true;
            for (int k = j; k < rounds; k++) {
                if (Naomi[k] < Ken[k - j]) {
                    win_rest = false;
                    break;
                }
            }
            if (win_rest) {
                cheat_score = rounds - j;
                break;
            }
        }
        printf("Case #%d: %d %d\n", i+1, cheat_score, score);
    }
    return 0;
}

