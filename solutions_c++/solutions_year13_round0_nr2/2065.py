#include <stdio.h>
#include <iostream>
#include <string.h>
#include <stdlib.h>

#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)

using namespace std;

int main () {
    int t, testcase = 1, n, m, i, j, lawn[100][100], rowMax[100], colMax[100];
    scanf("%d", &t);
    while (testcase <= t) {
        scanf("%d%d", &n, &m);
        rep(i, n) {
            rowMax[i] = 0;
            rep(j, m) {
                scanf("%d", &lawn[i][j]);
                if (lawn[i][j] > rowMax[i]) {
                    rowMax[i] = lawn[i][j];
                }
            }
        }
        rep(j, m) {
            colMax[j] = 0;
            rep(i, n) {
                if (lawn[i][j] > colMax[j]) {
                    colMax[j] = lawn[i][j];
                }
            }
        }
        printf("Case #%d: ", testcase++);
        bool isPossible = true;
        rep(j, m) {
            rep(i, n) {
                if (lawn[i][j] < rowMax[i] && lawn[i][j] < colMax[j]) {
                    isPossible = false;
                }
            }
        }
        if (isPossible) {
            printf("YES\n");
        } else {
            printf("NO\n");
        }
    }
    return 0;
}
