#include <iostream>
#include <vector>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;
char num[3][100][2000];
char nt[3] = {'R', 'S', 'P'};
char ans[3][2000], res[2000];
int vis[20][3];
int st[10000];
char ch[3];
int main() {
    num[0][0][0] = 'R';
    num[1][0][0] = 'P';
    num[2][0][0] = 'S';
    for (int i = 1; i <= 12; i++) {
        if (strcmp(num[0][i - 1], num[1][i - 1]) < 0) {
            int len = strlen(num[0][i - 1]);
            for (int j = 0; j < len; j++) num[0][i][j] = num[0][i - 1][j];
            for (int j = 0; j < len; j++) num[0][i][len + j] = num[1][i - 1][j];
        } else {
            int len = strlen(num[0][i - 1]);
            for (int j = 0; j < len; j++) num[0][i][j] = num[1][i - 1][j];
            for (int j = 0; j < len; j++) num[0][i][len + j] = num[0][i - 1][j];
        }
        if (strcmp(num[1][i - 1], num[2][i - 1]) < 0) {
            int len = strlen(num[1][i - 1]);
            for (int j = 0; j < len; j++) num[1][i][j] = num[1][i - 1][j];
            for (int j = 0; j < len; j++) num[1][i][len + j] = num[2][i - 1][j];
        } else {
            int len = strlen(num[0][i - 1]);
            for (int j = 0; j < len; j++) num[1][i][j] = num[2][i - 1][j];
            for (int j = 0; j < len; j++) num[1][i][len + j] = num[1][i - 1][j];
        }
        if (strcmp(num[2][i - 1], num[0][i - 1]) < 0) {
            int len = strlen(num[2][i - 1]);
            for (int j = 0; j < len; j++) num[2][i][j] = num[2][i - 1][j];
            for (int j = 0; j < len; j++) num[2][i][len + j] = num[0][i - 1][j];
        } else {
            int len = strlen(num[2][i - 1]);
            for (int j = 0; j < len; j++) num[2][i][j] = num[0][i - 1][j];
            for (int j = 0; j < len; j++) num[2][i][len + j] = num[2][i - 1][j];
        }
    }
    int t;
    scanf("%d", &t);
    int cas = 1;
    while (t--) {
        int n, r, p, s;
        scanf("%d%d%d%d", &n, &r, &p, &s);
        printf("Case #%d: ", cas++);
        res[0] = 0;
        for (int i = 0; i < 3; i++) {
            int len = strlen(num[i][n]);
            int sr = 0, sp = 0, ss = 0;
            for (int j = 0; j < len; j++) {
                if (num[i][n][j] == 'S') ss++;
                if (num[i][n][j] == 'R') sr++;
                if (num[i][n][j] == 'P') sp++;
            }
            if (ss == s && sp == p && sr == r) {
                if (res[0] == 0 || strcmp(res, num[i][n]) < 0) strcpy(res, num[i][n]);
            } 
        }
        if (res[0] == 0) printf("IMPOSSIBLE\n");
        else printf("%s\n", res);
    }
    return 0;
}
