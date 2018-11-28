#include <cstdio>

int main() {
    int T;
    scanf("%d", &T);
    for ( int tc = 1; tc <= T; tc++ ) {
        char map[7][7];
        for ( int j = 0; j < 4; j++ ) {
            scanf("%s", map[j]);
        }

        int dir[4][2] = { {1,0}, {1,1}, {0,1}, {1,-1} };
        int result = -1;//draw
        for ( int x = 0; x < 4; x++ ) {
            for ( int y = 0; y < 4; y++ ) {
                for ( int i = 0; i < 4; i++ ) {//dir
                    char cur = map[x][y];
                    if ( cur == '.' ) {
                        if ( result == -1 ) {
                            result = -2;
                        }
                        continue;
                    }
                    int cnt = 0;
                    int tcnt = 0;
                    for ( int j = 0; j < 4; j++ ) {
                        int nx = x + dir[i][0]*j;
                        int ny = y + dir[i][1]*j;
                        if ( 0 <= nx && nx < 4 && 0 <= ny && ny < 4 ) {
                            if ( cur == map[nx][ny] ) {
                                cnt++;
                            } else if ( map[nx][ny] == 'T' ) {
                                tcnt++;
                            }
                        }
                    }
                    if ( cnt == 4 || (cnt == 3 && tcnt == 1) ) {
                        if ( cur == 'O' ) {
                            result = 0;
                        } else if ( cur == 'X' ) {
                            result = 1;
                        }
                    }
                }

            }
        }
        switch ( result ) {
            case -1: printf("Case #%d: Draw\n", tc); break;
            case -2: printf("Case #%d: Game has not completed\n", tc); break;
            case 0: printf("Case #%d: O won\n", tc);break;
            case 1: printf("Case #%d: X won\n", tc);break;
        }
    }
    return 0;
}
