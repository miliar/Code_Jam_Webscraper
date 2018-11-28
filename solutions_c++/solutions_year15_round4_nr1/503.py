#include <bits/stdc++.h>

using namespace std;
const int N = 105;
int cnt[N][N], mustSwitch[N][N];
char board[N][N];
int n, m;
void testCase() {
    scanf("%d %d", &n, &m);
    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= m; j++) {
            cnt[i][j] = mustSwitch[i][j] = 0;
        }
    }
    for(int i = 1; i <= n; i++) {
        scanf("%s", &board[i][1]);
    }
    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= m; j++) {
            if(board[i][j] != '.') {
                cnt[i][j]++;
                if(board[i][j] == '<') {
                    mustSwitch[i][j] = true;
                }
                break;
            }
        }
        for(int j = m; j >= 1; j--) {
            if(board[i][j] != '.') {
                cnt[i][j]++;
                if(board[i][j] == '>') {
                    mustSwitch[i][j] = true;
                }
                break;
            }
        }
    }
    
    
    for(int j = 1; j <= m; j++) {
        for(int i = 1; i <= n; i++) {
            if(board[i][j] != '.') {
                cnt[i][j]++;
                if(board[i][j] == '^') {
                    mustSwitch[i][j] = true;
                }
                break;
            }
        }
        for(int i = n; i >= 1; i--) {
            if(board[i][j] != '.') {
                cnt[i][j]++;
                if(board[i][j] == 'v') {
                    mustSwitch[i][j] = true;
                }
                break;
            }
        }
    }
    int ans = 0;
    for(int i = 1; i <= n; i++) {
        for(int j = 1; j <= m; j++) {
            if(cnt[i][j] == 4) {
                printf("IMPOSSIBLE\n");
                return;
            } else if(mustSwitch[i][j]) {
                ans++;
            }
        }
    }
    printf("%d\n", ans);
}

int main() {
    int t;
    scanf("%d" ,&t);
    for(int test = 1; test <= t; test++) {
        printf("Case #%d: ", test);
        testCase();
    }
    return 0;
}