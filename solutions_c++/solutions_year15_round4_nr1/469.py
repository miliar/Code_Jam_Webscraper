//tonynater

#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

const int MAXR = 110;

int R, C;
int A[MAXR][MAXR]; //. = 0, ^ = 1, > = 2, v = 3, < = 4

bool find(int x, int y) {
    for(int i = 0; i < R; i++) {
        if(i != x && A[i][y] > 0) {
            return true;
        }
    }
    for(int i = 0; i < C; i++) {
        if(i != y && A[x][i]) {
            return true;
        }
    }
    return false;
}

int orient(int x, int y) { // -1 = failure, ret = num_changes
    if(A[x][y] == 0) {
        return 0;
    }else if(A[x][y] == 1) {
        for(int i = x-1; i >= 0; i--) {
            if(A[i][y] > 0) {
                return 0;
            }
        }
    }else if(A[x][y] == 2) {
        for(int i = y+1; i < C; i++) {
            if(A[x][i] > 0) {
                return 0;
            }
        }
    }else if(A[x][y] == 3) {
        for(int i = x+1; i < R; i++) {
            if(A[i][y] > 0) {
                return 0;
            }
        }
    }else if(A[x][y] == 4) {
        for(int i = y-1; i >= 0; i--) {
            if(A[x][i] > 0) {
                return 0;
            }
        }
    }
    
    if(find(x,y)) {
        return 1;
    }else {
        return -1;
    }
}

int main() {
    freopen("/Users/tonynater/Downloads/A-large.in", "r", stdin);
    freopen("/Users/tonynater/Store/Computer/Xcode_repos/Miscellaneous/GCJ_2015/R2_A/r2_a_large.out", "w", stdout);
    
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    
    int T;
    cin >> T;
    for(int t = 0; t < T; t++) {
        cin >> R >> C;
        
        memset(A,0,sizeof(A));
        for(int i = 0; i < R; i++) {
            string line;
            cin >> line;
            for(int j = 0; j < C; j++) {
                if(line[j] == '^') {
                    A[i][j] = 1;
                }else if(line[j] == '>') {
                    A[i][j] = 2;
                }else if(line[j] == 'v') {
                    A[i][j] = 3;
                }else if(line[j] == '<') {
                    A[i][j] = 4;
                }
            }
        }
        
        int res = 0;
        for(int i = 0; i < R; i++) {
            for(int j = 0; j < C; j++) {
                int cur = orient(i,j);
                if(cur == -1) {
                    res = -1;
                    break;
                }else {
                    res += cur;
                }
            }
        }
        
        cout << "Case #" << t+1 << ": ";
        if(res >= 0) {
            cout << res << '\n';
        }else {
            cout << "IMPOSSIBLE\n";
        }
    }
    
    return 0;
}