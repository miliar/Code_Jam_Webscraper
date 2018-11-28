
#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

int lawn[100][101];
int n, m;

bool gt_in_x (int value, int x) {
    for (int i = 0; i < m; i++) {
        if (lawn[x][i] > value) return true;
    }
    return false;
}

bool gt_in_y (int value, int y) {
    for (int i = 0; i < n; i++) {
        if (lawn[i][y] > value) return true;
    }
    return false;
}

int main (void) {
    int t;
    bool possible;
    
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    
    scanf("%d", &t);
    
    for (int z = 1; z <= t; z++) {
        scanf("%d %d", &n, &m);
        possible = true;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                scanf("%d", &lawn[i][j]);
            }
        }
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (gt_in_x(lawn[i][j], i) && gt_in_y(lawn[i][j], j)) {
                    possible = false;
                    goto solution;
                }
            }
        }
        
        solution:
        
        if (possible) {
            printf("Case #%d: YES\n", z);
        } else {
            printf("Case #%d: NO\n", z);
        }
    }
    
    return 0;
}
