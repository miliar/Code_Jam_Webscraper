//
//  T2.cpp
//  GCJ.2013.1
//
//  Created by Orpine on 13-4-13.
//  Copyright (c) 2013年 Orpine. All rights reserved.
//
#include <iostream>
#include <cstdio>
using namespace std;

int T,n,m;
int map[108][108],row[108],col[108];
bool v[108][108];
void Work()
{
    scanf("%d%d",&n,&m);
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            scanf("%d", &map[i][j]);
        }
    }
    bool flag = true;
    for (int w = 2; flag && w > 0; w--) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (map[i][j] <= w) {
                    v[i][j] = true;
                }
                else v[i][j] = false;
            }
        }
        memset(row, 0, sizeof row);
        memset(col, 0, sizeof col);
        for (int i = 1; i <= n; i++) {
            bool f = true;
            for (int j = 1; f && j <= m; j++) {
                if (!v[i][j]) {
                    f = false;
                }
            }
            row[i] = f;
        }
        for (int i = 1; i <= m; i++) {
            bool f = true;
            for (int j = 1; f && j <= n; j++) {
                if (!v[j][i]) {
                    f = false;
                }
            }
            col[i] = f;
        }
        for (int i = 1; flag && i <= n; i++) {
            for (int j = 1; flag && j<= m; j++) {
                if (v[i][j] && !row[i] && !col[j]) {
                    flag = false;
                }
                if (!v[i][j] && (row[i] || col[j])) {
                    flag =false;
                }
            }
        }
    }
    puts(flag ? "YES" : "NO");
}
int main(int argc, const char * argv[])
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for (int i = 1; i <= T; i++) {
        cout << "Case #" << i << ": ";
        Work();
        cout << endl;
    }
}