//
//  main.cpp
//  GoogleJam1
//
//  Created by Raghu Raman on 11/04/15.
//  Copyright (c) 2015 Raghu Raman. All rights reserved.
//

#include <iostream>
#include <stdio.h>
using namespace std;
int no;

void solve(){
    char level[1000002];
    long temp, friends = 0 , already_stood;
    long length;
    scanf("%ld", &length);
    scanf("%s", level);
    already_stood = level[0] - '0';
    for (long current_level = 1; current_level < (length + 1); current_level++){
        if (already_stood < current_level){
            temp = current_level - already_stood;
            friends += temp;
            already_stood += temp;
        }
        already_stood += level[current_level] - '0';
    }
    printf("Case #%d: %ld\n", ++no, friends);
}

int main(int argc, const char * argv[]) {
    int testcase;
    cin >> testcase;
    while (testcase --> 0)
        solve();
    return 0;
}
