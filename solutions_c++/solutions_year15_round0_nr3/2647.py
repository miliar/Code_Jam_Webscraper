//
//  main.cpp
//  round3
//
//  Created by wangdongfang on 15/4/11.
//  Copyright (c) 2015年 _. All rights reserved.
//

#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int map[26][26];

char input [10005];

int L;
int X;

int ans [4];

void find(int round) {
    int current_num = 1;
    int check_num = 0;
    int check_index = 0;
    int ans_index = 0;
    char current_check_char;
    while (check_num < L * X) {
        int first_idx;
        if (current_num != 1 && current_num != -1) {
            first_idx = current_num;
        }
        else if (current_num == 1) {
            first_idx = 1;
        }
        else if (current_num == -1) {
            first_idx = -1;
        }
            
        current_check_char = input[check_index];
        int second_idx = current_check_char - 'a';
        
        int negation = 1;
        if (first_idx < 0) {
            first_idx *= -1;
            negation *= -1;
        }
        if (second_idx < 0) {
            second_idx *= -1;
            negation *= -1;
        }

        current_num = map[first_idx][second_idx];
        current_num *= negation;
            
        if (current_num == ans[ans_index]) {
            ans_index++;
            current_num = 1;
            if (ans_index > 3) {
                ans_index = 3;
            }
        }
        check_num++;
        check_index++;
        if (check_index >= L) {
            check_index %= L;
        }
      

    }
    if (ans_index == 3 && current_num == 1) {
        cout << "Case #" << round <<": "<< "YES" << endl;
    }
    else {
        cout << "Case #" << round <<": "<< "NO" << endl;

    }
    
}

int main() {
   
    int T;
 //   freopen("/Users/wangdongfang/Myprogram/codejam2015/round3/round3/round3/smalldata.txt", "r",stdin);
    
    cin >> T;
   
    ans [0] = 'i' - 'a';
    ans [1] = 'j' - 'a';
    ans [2] = 'k' - 'a';
    ans [3] = 1;
    
    map [1][1] = 1;
    map [1]['i' - 'a'] = 'i' - 'a';
    map [1]['j' - 'a'] = 'j' - 'a';
    map [1]['k' - 'a'] = 'k' - 'a';
    
    map ['i' - 'a'][1] = 'i' - 'a';
    map ['i' - 'a']['i' - 'a'] = -1;
    map ['i' - 'a']['j' - 'a'] = 'k' - 'a';
    map ['i' - 'a']['k' - 'a'] = -1 * ('j'- 'a');
    
    map ['j' - 'a'][1] = 'j'- 'a';
    map ['j' - 'a']['i' - 'a'] = -1 *('k'- 'a');
    map ['j' - 'a']['j' - 'a'] = -1;
    map ['j' - 'a']['k' - 'a'] = 'i'- 'a';
    
    map ['k' - 'a'][1] = 'k'- 'a';
    map ['k' - 'a']['i' - 'a'] = 'j'- 'a';
    map ['k' - 'a']['j' - 'a'] = -1 * ('i'- 'a');
    map ['k' - 'a']['k' - 'a'] = -1;
    
   
    for (int i = 0; i < T; i++) {
        cin >> L >> X;
            for (int j = 0; j < L; j++) {
            char character;
            cin >> character;
            input[j] = character;
        }
        find(i+1);
        
    }
    return 0;
}
