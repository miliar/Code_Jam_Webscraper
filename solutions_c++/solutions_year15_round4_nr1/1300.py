#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <vector>
#include <string>
#include <queue>
#include <iostream>
using namespace std;

bool fless(double a,double b){ return b-a>1e-6; }
bool fequal(double a,double b){ return fabs(b-a)<=1e-6; }


int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

int get_dir(int v) {
    if (v == 'v')return 0;
    if (v == '>')return 1;
    if (v == '^')return 2;
    if (v == '<')return 3;
    return 0;
}


int main(){
    int tt; scanf("%d",&tt);
    for (int ti=1;ti<=tt;ti++){
        int n, m; scanf("%d%d", &n, &m);
        char a[n][m+1];
        for (int i=0;i<n;i++) {
            scanf("%s", a[i]);
        }

        bool impossible = false;
        int ans = 0;

        for (int i=0;i<n;i++) {
            for (int j=0;j<m;j++) {
                if (a[i][j] == '.') {
                    continue;
                }
                // walk that dir to see if it go stragiht out
                int dir = get_dir(a[i][j]);
                int cx = i, cy = j;
                bool ok = true;
                while (true) {
                    cx += dx[dir];
                    cy += dy[dir];
                    if (cx < 0 || cx >= n || cy < 0 || cy >= m) {
                        // a[i][j] needs to change
                        ok = false;
                    }
                    if (a[cx][cy] != '.') {
                        break;
                    }
                }
                //printf("(%d %d) %d\n", i, j, ok);
                if (!ok) {
                    // try turn to other direction
                    bool ok2 = false;
                    for (int k=0;k<4;k++) {
                        cx = i; cy=j;
                        while (true) {
                            cx += dx[k]; cy += dy[k];
                            if (cx < 0 || cx >= n || cy < 0 || cy >= m) {
                                break;
                            } else {
                                if (a[cx][cy] != '.') ok2 = true;
                            }
                        }
                    }
                    if (ok2) {
                        ans ++;
                    } else {
                        impossible = true;
                    }
                    //printf("- ok2: %d\n", ok2);
                }

            }
        }

        if (impossible) {
            printf("Case #%d: IMPOSSIBLE\n",ti);
        } else {
            printf("Case #%d: %d\n",ti,ans);

        }
    }
    return 0;
}
