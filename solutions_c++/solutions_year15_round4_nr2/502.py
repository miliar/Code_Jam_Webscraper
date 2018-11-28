//
//  main.cpp
//  p2
//
//  Created by 默默 on 15-4-2.
//  Copyright (c) 2015年 默默. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <iostream>
#include <map>
#include <vector>
#include <stack>
#include <set>
#include <cstring>
#include <queue>
using namespace std;
#define MA 100005
char num[MA];
int K;
int main(){
    //freopen("a.in", "r", stdin);
    //freopen("/Users/momo/Desktop/xcode_data/in.txt", "r", stdin);
    int cas;
    scanf("%d", &cas);
    while (cas--){
        scanf("%s %d",num, &K);
        stack<char> st;
        int len = strlen(num);
        int i = 0;
        for (; i < len; ++i){
            while (!st.empty() && K != 0 && st.top() < num[i]){
                st.pop();
                --K;
            }
            st.push(num[i]);
            if (K == 0){
                break;
            }
        }
        ++i;
        while (K != 0 && !st.empty()){
            st.pop();
            --K;
        }
        
        string temp;
        while (!st.empty()){
            temp = st.top() + temp;
            st.pop();
        }
        printf("%s", temp.c_str());
        if (i < len){
            printf("%s", num+i);
        }
        puts("");
        
    }
    return 0;
}






