//
//  main.cpp
//  2
//
//  Created by David on 14-4-12.
//  Copyright (c) 2014年 David. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
using namespace std;

const string CASE = "Case #";
const string BAD = "Bad magician!";
const string CHEATED = "Volunteer cheated!";

const int BAD_ANSWER = -1;
const int CHEATED_ANSWER = -2;


int guess(int case_num) {
    int first_answer;
    int second_answer;
    int first_arrange[16];
    int second_arrange[16];
    cin >> first_answer;
    for (int i = 0; i < 16; i++) {
        cin >> first_arrange[i];
    }
    
    cin >> second_answer;
    for (int i = 0; i < 16; i++) {
        cin >> second_arrange[i];
    }
    
    int found[4] = {0};
    int num[4] = {0};
    
    for (int i = 0; i < 4; i++) {
        int cardNum = first_arrange[4*(first_answer-1) + i];
        for (int j = 0; j < 16; j++) {
            if (cardNum == second_arrange[j]) {
                found[j/4]++;
                num[j/4] = cardNum;
            }
        }
    }
    
    if (found[second_answer-1] == 0) {
        return CHEATED_ANSWER;
    }
    if (found[second_answer-1] > 1) {
        return BAD_ANSWER;
    }
    return num[second_answer-1];
    
    
}
int main() {
    
    freopen("/Users/david/Documents/x-code/google code jam/A-small-attempt4.in", "r", stdin);
    freopen("/Users/david/Documents/x-code/google code jam/A-small-attempt0.out", "w", stdout);
    int T;
    cin >> T;
    
    for (int i = 0; i < T; i++) {
        int a = guess(i+1);
        switch(a) {
            case BAD_ANSWER:
                cout << CASE << (i+1) << ": " << BAD << endl;
                break;
            case CHEATED_ANSWER:
                cout << CASE << (i+1) << ": " << CHEATED << endl;
                break;
            default:
                cout << CASE << (i+1) << ": " << a << endl;
                break;
        }
    }
}

