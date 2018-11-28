#include <cstdio>
#include <iostream>
#include <map>
#include <vector>
#include <set>
#include <string>
#include <cstring>
#define TASK "B"
using namespace std;

int T, G[100][100];
int N, M;

int MaxR[100], MaxC[100];

bool possible() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (G[i][j] < MaxR[i] && G[i][j] < MaxC[j]) {
                return false;
            }
        }
    }
    return true;
}

int main() {
    freopen(TASK ".in", "r", stdin);
    freopen(TASK ".out", "w", stdout);
    
    scanf("%d", &T);
    for (int test = 1; test <= T; test++) {
        memset(MaxR, 0, sizeof(MaxR));
        memset(MaxC, 0, sizeof(MaxC));
        scanf("%d %d", &N, &M);
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                scanf("%d", &G[i][j]);
                MaxR[i] = max(MaxR[i], G[i][j]);
                MaxC[j] = max(MaxC[j], G[i][j]);
            }
        }
        
        printf("Case #%d: ", test);
        printf(possible() ? "YES\n" : "NO\n");
    }
    
    return 0;
}
