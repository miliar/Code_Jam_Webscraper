#include <cstdio>
#include <algorithm>
using namespace std;

const int MAX_N = 105;

int R, C;
char grid[MAX_N][MAX_N];

int row[MAX_N];
int col[MAX_N];

int dr[] = {0, 0, 1, -1};
int dc[] = {1, -1, 0, 0};

int m(char c) {
    if(c == '^') {
        return 3;
    } else if(c == 'v') {
        return 2;
    } else if(c == '>') {
        return 0;
    } else if(c == '<') {
        return 1;
    } else {
        return -1;
    }
}

int main() {
    int T;
    scanf("%d",&T);

    for(int z=1;z<=T;z++) {
        for(int i=0;i<MAX_N;i++) {
            row[i] = 0;
            col[i] = 0;
        }

        scanf("%d %d",&R,&C);

        int numOff = 0;
        for(int i=0;i<R;i++) {
            scanf(" %s ",grid[i]);

            for(int j=0;j<C;j++) {
                int d = m(grid[i][j]);
                if(d != -1) {
                    row[i]++;
                    col[j]++;
                }
            }
        }

        bool impossible = false;
        for(int i=0;i<R;i++) {
            for(int j=0;j<C;j++) {
                int d = m(grid[i][j]);
                if(d != -1) {
                    if(row[i] == 1 && col[j] == 1) {
                        impossible = true;
                    } else {
                        int nr = i;
                        int nc = j;

                        for(int k=0;k<max(R,C)+3;k++) {
                            nr += dr[d];
                            nc += dc[d];

                            if(nr >= 0 && nc >= 0 && nr < R && nc < C) {
                                if(m(grid[nr][nc]) != -1) {
                                    break;
                                }
                            } else {
                                numOff++;
                                break;
                            }
                        }
                    }
                }
            }
        }

        printf("Case #%d: ",z);
        if(impossible) {
            printf("IMPOSSIBLE\n");
        } else {
            printf("%d\n",numOff);
        }
    }

    return 0;
}
