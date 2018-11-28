//
//  main.cpp
//  LastWord
//
//  Created by 손 정훈 on 2016. 4. 16..
//  Copyright (c) 2016년 손 정훈. All rights reserved.
//

#include <iostream>
#include <string>
#include <algorithm>

#define MAX_S 1000*3

using namespace std;
int main() {
    int T;
    cin >> T;
    char ans[100][1002];
    memset(ans, 0, 100*1002);
    for(int t = 0; t < T; t++){
        string s;
        cin >> s;
        int len = s.length();
        int start = 1500;
        int end = 1500;

        char new_s[MAX_S];
        memset(new_s, 0, MAX_S);
        for(int i = 0; i < len; i++){
                if(s[i] >= new_s[start]){
                    new_s[--start] = s[i];
                }
                else{
                    new_s[end++] = s[i];
                }
        }
        memcpy(ans[t], new_s+start, end-start);
    }
    
    for(int t = 0; t < T; t++){
        printf("Case #%d: %s\n", t+1, ans[t]);
    }
    return 0;
}
