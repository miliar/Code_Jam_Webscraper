//
//  ProblemA.cpp
//  codejam2015
//
//  Created by sambaiz on 2015/04/11.
//  Copyright (c) 2015年 sambaiz. All rights reserved.
//

#include <iostream>

const int MAX_S = 1000 + 1;

// char(0~9) -> int
int ctoi(char c) {
    return c - 48; // エラー処理(0~9以外)は省略
}

int main() {
    // case数
    int c_n = 0;
    // s_max, 各shynessのaudienceの人数, 暫定立っている人数の累計, inviteしないといけない人数(output)
    int s, sum, invite;
    char a[MAX_S];
    // 標準入力より入力
    scanf("%d", &c_n);
    for(int n = 0; n < c_n; n++){
        sum = 0, invite = 0;
        scanf("%d %s", &s, a);
        for(int i = 0; i < s + 1; i++){
            if(i > sum && ctoi(a[i]) != 0){ //立つ条件を満たしていない
                invite += i - sum;
                sum = i;
            }
            sum += ctoi(a[i]);
        }
        
        // 標準出力へ出力
        printf("Case #%d: %d\n", n + 1, invite);
    }
}