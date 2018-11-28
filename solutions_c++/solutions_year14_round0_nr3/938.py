#include<stdio.h>

char mine[60][60];
int main() {
    int tc,t, r,c,m, i,j;

    scanf("%d",&t);
    for(tc=1; tc<=t; ++tc) {
        printf("Case #%d:\n", tc); 
        scanf("%d %d %d",&r,&c,&m);
        int max = r*c;

        if(m != max) {
            if(r==1 || c==1) {
                for(i=1; i<=r; ++i)
                for(j=1; j<=c; ++j) {
                    if(m)   mine[i][j] = '*', --m;
                    else    mine[i][j] = '.';
                }
                mine[r][c] = 'c';
            }
            else {
                bool special = (m == max-1);
                for(i=1; i<(r-1); ++i)
                for(j=1; j<(c-1); ++j) {
                    if(m)   mine[i][j] = '*', --m;
                    else    mine[i][j] = '.';
                }
                if(!special && (m&1) && (r>=3 && c>=3)) {
                    ++ m;
                    mine[r-2][c-2] = '.';
                }
                for(i=1; i<(r-1); ++i) {
                    if(m>0) mine[i][c-1] = '*', --m,
                            mine[i][c  ] = '*', --m;
                    else    mine[i][c-1] = '.',
                            mine[i][c  ] = '.';
                }
                if(mine[r-2][c-2] == '.' &&
                   mine[r-2][c-1] == '*') {
                    m+= 2;
                    mine[r-2][c-1] = '.';
                    mine[r-2][c  ] = '.';
                }
                for(j=1; j<(c-1); ++j) {
                    if(m>0) mine[r-1][j] = '*', --m,
                            mine[r  ][j] = '*', --m;
                    else    mine[r-1][j] = '.',
                            mine[r  ][j] = '.';
                }
                if(mine[r-2][c-2] == '.' &&
                   mine[r-1][c-2] == '*') {
                    m+= 2;
                    mine[r-1][c-2] = '.';
                    mine[r  ][c-2] = '.';
                }

                if(m==0 || m==3)
                for(i=r-1; i<=r; ++i)
                for(j=c-1; j<=c; ++j) {
                    if(m>0) mine[i][j] = '*', --m;
                    else    mine[i][j] = '.';
                }
                
                mine[r][c] = 'c';
            }
        }

        if(m) printf("Impossible\n");
        else {
            for(i=1; i<=r; ++i) {
            for(j=1; j<=c; ++j) {
                printf("%c", mine[i][j]);
            }
                printf("\n");
            }
        }
    }
    return 0;
}
