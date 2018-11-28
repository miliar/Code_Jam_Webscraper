#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <assert.h>

#include <iostream>
#include <algorithm>
#include <string>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <queue>

#include <thread>
#include <chrono>

#include <memory>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>
#include <signal.h>
#include <sys/stat.h>

using namespace std;

char a[110][110];
char f[4][2] = {{0,1},{0,-1},{1,0},{-1,0}};
int r, c;

int change;
int impos;

bool check(int x, int y, int k, int l) {
    int x0 = x + k, y0 = y + l;
    while (x0 >= 0 and y0 >= 0 and x0 < r and y0 < c) {
        if (a[x0][y0] != '.') {
            return true;
        }
        x0 += k;
        y0 += l;
    }
    
    return false;
}


int main() {
    freopen("/Users/lujcmss/Downloads/A-large.in.txt", "r", stdin);
    freopen("/Users/lujcmss/Downloads/a.out", "w", stdout);
    
    int T;
    scanf("%d", &T);
    
    for (int kase = 0; kase < T; kase++) {
        cin >> r >> c;
        
        for (int i = 0; i < r; i++) {
            string s;
            cin >> s;
            for (int j = 0; j < c; j++) {
                a[i][j] = s[j];
            }
        }
        
        change = 0;
        impos = 0;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                int ind = 0;
                if (a[i][j] == '.') {
                    continue;
                } else if (a[i][j] == '^') {
                    ind = 3;
                } else if (a[i][j] == '<') {
                    ind = 1;
                } else if (a[i][j] == '>') {
                    ind = 0;
                } else {
                    ind = 2;
                }
                
                if (check(i, j, f[ind][0], f[ind][1])) {
                    continue;
                }
                
                int flag = false;
                for (int k = 0; k < 4; k++) {
                    if (k != ind) {
                        if (check(i, j, f[k][0], f[k][1])) {
                            flag = true;
                            break;
                        }
                    }
                }
                
                if (flag) {
                    change++;
                } else {
                    impos++;
                }
            }
        }
        
        printf("Case #%d: ", kase+1);
        if (impos) printf("IMPOSSIBLE\n");
        else printf("%d\n", change);
    }
    
    return 0;
}