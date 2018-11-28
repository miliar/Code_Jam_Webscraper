//
//  main.cpp
//  test
//
//  Created by 商占仝 on 2017/3/22.
//  Copyright © 2017年 bytedance. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

const int maxn = 1005;

char str[maxn];
int k, len;

int main(){
   // freopen("A-large.in", "r", stdin);
   // freopen("out.txt", "w", stdout);
    int T, cases = 0;
    scanf("%d", &T);
    while(T--){
        scanf("%s%d", str, &k);
        len = (int)strlen(str);
        int ans = 0;
        for(int i = 0; i < len; ++i){
            if(i > len - k){
                if(str[i] == '-'){
                    ans = -1;
                    break;
                }
            }
            else if(str[i] == '-'){
                ++ans;
                for(int j = 0; j < k; ++j){
                    str[i + j] = str[i + j] == '+' ? '-' : '+';
                }
            }
        }
        printf("Case #%d: ", ++cases);
        if(ans == -1) printf("IMPOSSIBLE\n");
        else printf("%d\n", ans);
    }
    return 0;
}
