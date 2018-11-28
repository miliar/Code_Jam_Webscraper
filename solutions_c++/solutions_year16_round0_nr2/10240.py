//
//  Solution.cpp
//  GoogleJam
//
//  Created by LIU YUJIE on 3/25/15.
//  Copyright (c) 2015 刘予杰. All rights reserved.
//

#include "Solution.h"
#include <string>
#include <unordered_map>

int docase1(int R,int C, int N)
{
    int maxUnhappy = (C-1) * R + (R - 1) * C;
    int t = R * C - N;
    if (N <= (R * C + 1) / 2) {
        return 0;
    }
    else if(R == 1)
    {
        if (C % 2 == 1) {
            return t * 2;
            
        }
        else{
            return 1 + (t - 1) / 2;
        }
    }else if(R == 2){
        int num = (C - 1)/2 + (C-2)/2;
        if (t < num) {
            maxUnhappy -= 3 * t;
            t = 0;
        }
        maxUnhappy -= 2 * t;
    }
    else if(R == 3){
        if (C == 3) {
            if (t == 1) {
                maxUnhappy -= 4;
            }
            else{
                maxUnhappy -= 3 * t;
            }
        }
        else if(C == 4){
            if (t == 1) {
                maxUnhappy -= 4;
            }
            else if(t <= 4){
                maxUnhappy -= 1 + t * 3;
            }
            else{
                maxUnhappy -= 13 + (t - 4) * 2;
            }
        }
        else if(C == 5){
            if (t <= 2) {
                maxUnhappy -= 4 * t;
            }
            else if(t <= 4){
                maxUnhappy -= 8 + (t - 2) * 3;
            }
            else if(t <= 7){
                maxUnhappy -= 4 + (t - 1) * 3;
            }
        }
    }
    else if(R== 4){
        if (t <= 2) {
            maxUnhappy -= 4 * t;
        }
        else if(t <= 6){
            maxUnhappy -= 8 + (t - 2) * 3;
        }
        else {
            maxUnhappy -= 20 + (t - 6) * 2;
        }
    }
    
    return maxUnhappy;
}

void doCase(ifstream& file,int index, string &s)
{
    string ans;
    string flag;
    file >> flag;
    
    int sum = 0;
    for (int i = 0; i < flag.length(); ++i) {
        char c = flag[i];
        if (c == '-') {
            if (i == 0) {
                sum = 1;
            } else if (flag[i-1] == '+') {
                sum += 2;
            }
        }
    }
    ans = to_string(sum);
    cout << "Case #" + to_string(index) + ": " + ans + "\n";
    s += "Case #" + to_string(index) + ": " + ans + "\n";
}

