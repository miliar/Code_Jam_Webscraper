/***************************************************************************
 *
 * Copyright (c) 2014 Baidu.com, Inc. All Rights Reserved
 *
 **************************************************************************/



/**
 * @file a.cpp
 * @author wangyaoxuan(com@baidu.com)
 * @date 2014/04/12 11:00:31
 * @brief
 *
 **/

#include <iostream>
#include <stdio.h>



const int N=5;
int a[N][N], b[N][N];


int main() {
    //freopen("A-small-attempt4.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int t, tt, n, m;
    scanf("%d", &t);
    tt = t;

    while(tt--) {
        scanf("%d", &n);
        n--;
        for(int i = 0; i < 4; ++i) {
            for(int j = 0; j < 4; ++j) {
                scanf("%d", &a[i][j]);
            }
        }

        scanf("%d", &m);
        m--;
        for(int i = 0; i < 4; ++i) {
            for(int j = 0; j < 4; ++j) {
                scanf("%d", &b[i][j]);
            }
        }
        int cnt = 0, ans;
        if((n >= 0 && n < 4) && (m >= 0 && m < 4)) {
            for(int i = 0; i < 4; ++i) {
                for(int j = 0; j < 4; ++j) {
                    if(a[n][i] == b[m][j]) {
                        ++cnt;
                        ans = a[n][i];
                    }
                }
            }
        } else {
            printf("Case #%d: Volunteer cheated!\n", t - tt);
            cnt = -1;
        }
        if(cnt == 0) {
            printf("Case #%d: Volunteer cheated!\n", t - tt);
        } else if(cnt > 1) {
            printf("Case #%d: Bad magician!\n", t - tt);
        } else if(cnt == 1) {
            printf("Case #%d: %d\n", t - tt, ans);
        }
    }
    //fclose(stdin);
    //fclose(stdout);

    return 0;
}
