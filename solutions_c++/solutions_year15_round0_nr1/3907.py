//
//  main.cpp
//  GCJ
//
//  Created by feliciafay on 4/10/15.
//  Copyright (c) 2015 feliciafay. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <cmath>
#include <sstream>
#include <algorithm>
using namespace std;

/*
 4
 4 11111
 1 09
 5 110011
 0 1
 Case #1: 0
 Case #2: 1
 Case #3: 2
 Case #4: 0
 */

int solve(int field_one, string field_two) {
    if (field_one == 0) return 0;
    int needed_friends = 0;
    int currrent_needed_friends = 0;
    int current_friends = field_two[0] - '0';
    for(int i = 1; i < field_one + 1; ++i) {
        int level_friends = field_two[i] - '0';
//        // 5 110011
        if (current_friends < i) {
            currrent_needed_friends = i - current_friends;
            needed_friends += currrent_needed_friends;
            current_friends = i + level_friends;
        } else {
            current_friends += level_friends;
        }
    }
    return needed_friends;
}

int main()
{
        freopen("/Users/feliciafay/Downloads/A-small-attempt1.in","r",stdin);  
    int test_number = 0;
    cin>>test_number;
    int field_one;
    string field_two;
    int min_friend;
    int count = 1;
    while (cin>>field_one>>field_two) {
        min_friend = solve(field_one, field_two);
        printf("Case #%d: %d\n", count, min_friend);
        ++count;
    }
    return 0;
}

