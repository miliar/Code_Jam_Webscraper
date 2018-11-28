/*
 * Author: WHHeV
 * Created Time:  2013/4/13 13:55:44
 * File Name: b.cpp
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;
#define out(v) cerr << #v << ": " << (v) << endl
#define SZ(v) ((int)(v).size())
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}

struct coor {
    int x, y;
};
vector<coor> coo[101];
int map[110][110];
int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        for(int i = 0; i < 101; ++i)
            coo[i].clear();
        int n, m;
        scanf("%d%d", &n, &m);
        memset(map, 0, sizeof(map));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                scanf("%d", &map[i][j]);
                coor tc;
                tc.x = i, tc.y = j;
                coo[map[i][j]].push_back(tc);
            }
        }
        bool flag = true;
        for (int i = 0; i < 101; ++i) {
            if (coo[i].size() == 0)
                continue;
            bool flag1 = true;
            for (vector<coor>::iterator it = coo[i].begin(); it != coo[i].end(); ++it) {
                //printf("[%d %d %d]\n", i, (*it).x, (*it).y);
                bool flag2 = true, flag3 = true;
                for (int j = 0; j < m; ++j) {
                    if (map[(*it).x][j] > i) {
                        flag2 = false;
                    }
                }
                for (int j = 0; j < n; ++j) {
                    if (map[j][(*it).y] > i) {
                        flag3 = false;
                        break;
                    }
                }
                if (!flag2 && !flag3) {
                    flag1 = false;
                    break;
                }
            }
            if (!flag1) {
                flag = false;
                break;
            }
        }
        if (flag) {
            printf("Case #%d: YES\n", t);
        } else {
            printf("Case #%d: NO\n", t);
        }
    }
    return 0;
}

