//
//  main.cpp
//  qr
//
//  Created by 文灏洋 on 08/04/2017.
//  Copyright © 2017 文灏洋. All rights reserved.
//

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <iostream>
using namespace std;
int T, K, n;
char s[1010];
int main() {
	//	freopen("a.txt", "r", stdin);
	//	freopen("a.out", "w", stdout);
    scanf("%d\n",&T);
    for (int tt = 1; tt <= T; tt++){
        scanf("%s %d\n", s, &K);
        n = (int)strlen(s);
        int ans = 0;
        for (int i = 0; i < n; i++){
            if (i + K - 1 >= n) break;
            if (s[i] == '-'){
                ans++;
                for (int j = 0; j < K; j++)
                    s[i + j] = s[i+j] == '-' ? '+' : '-';
            }
        }
        int flag = 0;
        for (int i = 0; i < n; i++)
            if (s[i] == '-'){
                flag = 1;
                break;
            }
        printf("Case #%d: ", tt);
        if (flag)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n", ans);
    }
    return 0;
}
