/*
 * Author: tender
 * Created Time:  2013/4/13 20:01:20
 * File Name: b.cpp
 */
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <map>
#include <queue>
#include <string>
#include <vector>
#include <set>

using namespace std;
const double pi = acos(-1.0);
const int maxn = 100;
int a[maxn + 2][maxn + 2];
bool vis[maxn + 2][maxn + 2];
int main() {
    int cas;
    freopen("B-large.in", "r", stdin);
    freopen("2.txt", "w", stdout);
    scanf("%d", &cas);
    for (int ii = 1; ii <= cas; ii++) {
        printf("Case #%d: ", ii);
        int n, m;
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++) {
                scanf("%d", &a[i][j]);
                vis[i][j] = false;
            }
        int left = n * m;
        int tmp = 0;
        while(left > 0) {
            tmp++;
            int _min = 0x7fffffff, ki, kj;
            for (int i = 0; i < n; i++)
                for (int j = 0; j < m; j++)
                    if (vis[i][j] == false && _min > a[i][j]) {
                        _min = a[i][j];
                        ki = i; kj = j;
                    }
            bool flag = true;
            for (int j = 0; j < m; j++)
                if (vis[ki][j] == false && a[ki][j] != _min) {
                    flag = false;
                    break;
                }
            if (flag) {
                for (int j = 0; j < m; j++)
                    if (vis[ki][j] == false) {
                        vis[ki][j] = true;
                        left--;
                    }
                continue;
            }
            flag = true;
            for (int i = 0; i < n; i++)
                if (vis[i][kj] == false && a[i][kj] != _min) {
                    flag = false;
                    break;
                }
            if (flag) {
                for (int i = 0; i < n; i++)
                    if (vis[i][kj] == false) {
                        vis[i][kj] = true;
                        left--;
                    }
            }
            else break;
        }
        if (left == 0) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
