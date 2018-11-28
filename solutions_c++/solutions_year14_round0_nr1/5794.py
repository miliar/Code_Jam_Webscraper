#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
using namespace std;

int a[5][5], b[5][5];

int main() {
    freopen("/Users/L/Downloads/A-small-attempt0.in.txt", "r", stdin);
    freopen("/Users/L/Downloads/A-small-attempt0.out.txt", "w", stdout);
    
    int T;
    scanf("%d", &T);
    
    for (int kase = 1; kase <= T; kase++) {
        int x, y;
        scanf("%d", &x);
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                scanf("%d", &a[i][j]);
            }
        }
        scanf("%d", &y);
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                scanf("%d", &b[i][j]);
            }
        }
        
        int match = 0, re;
        for (int j = 0; j < 4; j++) {
            for (int k = 0; k < 4; k++) {
                if (a[x-1][j] == b[y-1][k]) {
                    match++;
                    re = a[x-1][j];
                }
            }
        }
        printf("Case #%d: ", kase);
        if (match == 1) {
            printf("%d\n", re);
        } else if (match) {
            printf("Bad magician!\n");
        } else {
            printf("Volunteer cheated!\n");
        }
    }
    return 0;
}
