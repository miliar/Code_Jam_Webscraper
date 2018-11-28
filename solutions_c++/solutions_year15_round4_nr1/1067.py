#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

int t, T, R, C, ans;
char m[105][105];
int rc[105], cc[105];

bool valid ( int x , int y ) {
    return ( x >= 0 && x < R && y >= 0 && y < C );
}



char change( char c ) {
    if ( c == '^' ) return 0;
    if ( c == '>' ) return 1;
    if ( c == 'v' ) return 2;
    if ( c == '<' ) return 3;
    return -1;
}
int dir[4][2] = {{-1,0},{0,1},{1,0},{0,-1}};

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i, j;
    char str[105];
    scanf("%d",&T);
    for ( t = 1 ; t <= T ; t ++ ) {
        memset(rc,0,sizeof(rc));
        memset(cc,0,sizeof(cc));
        scanf("%d %d",&R,&C);
        for ( i = 0 ; i < R ; i ++ ) {
            scanf("%s",m[i]);
        }

        for ( i = 0 ; i < R ; i ++ ) {
            for ( j = 0 ; j < C ; j ++ ) {
                if ( m[i][j] != '.' ) {
                    rc[i]++;
                    cc[j]++;
                }
            }
        }

        ans = 0;
        bool noans = false;
        for ( i = 0 ; i < R && noans == false ; i ++ ) {
            for ( j = 0 ; j < C && noans == false ; j ++ ) {
                if ( m[i][j] != '.' ) {
                    int d = change(m[i][j]);
                    int x = i+dir[d][0], y = j+dir[d][1];
                    bool flag = false;
                    while ( valid(x,y) ) {
                        if ( m[x][y] != '.' ) {
                            flag = true;
                            break;
                        }
                        x += dir[d][0];
                        y += dir[d][1];
                    }
                    if ( flag == false ) {
                        if ( rc[i] < 2 && cc[j] < 2 ) {
                            noans = true;
                        }
                        else ans ++;
                    }
                }
            }
        }

        printf("Case #%d: ",t);

        if ( noans == true ) printf("IMPOSSIBLE\n");
        else printf("%d\n",ans);


    }
    return 0;
}
