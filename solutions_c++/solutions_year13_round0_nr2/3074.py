#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>

using namespace std;

int T;
int N, M;
int grid[101][101];
int maxrow[101];
int maxcol[101];

int main() {
    char name[50];
    char aName[50], bName[50];
    scanf("%s", name);
    strcpy(aName, name);   strcpy(bName, name);
    strcat(aName, ".in");  strcat(bName, ".out");
    FILE *in=fopen(aName, "r"), *out=fopen(bName,"w");

    fscanf(in, "%d", &T);

    int r, c;
    bool nope;
    for(int i=1; i<=T; i++) {
        memset(grid, 0, sizeof(grid));
        memset(maxrow, 0, sizeof(maxrow));
        memset(maxcol, 0, sizeof(maxcol));

        fscanf(in, "%d %d", &N, &M);
        nope = false;

        for(r=1; r<=N; r++) {
            for(c=1; c<=M; c++) {
                fscanf(in, "%d", &grid[r][c]);
            }
        }

        int x;
        for(r=1; r<=N; r++) {
            x = -1;
            for(c=1; c<=M; c++) {
                if(grid[r][c] > x) x = grid[r][c];
            }
            maxrow[r] = x;
        }
        for(c=1; c<=M; c++) {
            x = -1;
            for(r=1; r<=N; r++) {
                if(grid[r][c] > x) x = grid[r][c];
            }
            maxcol[c] = x;
        }


        for(r=1; r<=N; r++) {
            for(c=1; c<=M; c++) {
                if(grid[r][c]<maxrow[r] && grid[r][c]<maxcol[c]) {
//                    cout << r << " " << c << endl;
                    nope = true;
                    break;
                }
            }
            if(nope) break;
        }

        fprintf(out, "Case #%d: %s\n", i, !nope ? "YES" : "NO");

    }
    return 0;
}
