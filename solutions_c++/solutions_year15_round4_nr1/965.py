#include <stdio.h>
#include <string.h>

int T, R, C;
char map[110][110];

//0 = blank
//1 = up
//2 = right
//3 = down
//4 = left
char get_arrow() 
{
    char tmp = getchar();
    while(true) {
        if (tmp == '.') {
            return 0;
        } else if (tmp == '^') {
            return '^';
        } else if (tmp == '>') {
            return '>';
        } else if (tmp == 'v') {
            return 'v';
        } else if (tmp == '<') {
            return '<';
        }
        tmp = getchar();
    }
}

int slove() 
{
    int ans = 0;
    int count_r[110];
    int count_c[110];
    memset(count_r, 0, sizeof(count_r));
    memset(count_c, 0, sizeof(count_c));
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (map[i][j]) {
                count_r[i]++;
                count_c[j]++;
            }
        }
    }
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (map[i][j]) {
                if (count_r[i] == 1 && count_c[j] == 1) {
                    return -1;
                }
            }
        }
    }

    for (int i = 0; i < R; i++) {
        int start = 0;
        int end = 0;
        for (int j = 0; j < C; j++) {
            if (map[i][j]) {
                if(!start) {
                    start = 1;
                    if (map[i][j] == '<') {
                        ans ++;
                    }
                }
                if(map[i][j] == '>') {
                    end = 1;
                } else {
                    end = 0;
                }
            }
        }
        if (end) {
            ans++;
        }
    }
    for (int j = 0; j < C; j++) {
        int start = 0;
        int end = 0;
        for (int i = 0; i < R; i++) {
            if (map[i][j]) {
                if(!start) {
                    start = 1;
                    if (map[i][j] == '^') {
                        ans ++;
                    }
                }
                if(map[i][j] == 'v') {
                    end = 1;
                } else {
                    end = 0;
                }
            }
        }
        if (end) {
            ans++;
        }
    }

    return ans;
}

int main()
{
    scanf("%d", &T);
    for (int z = 1; z <= T; z++) {
        scanf("%d%d", &R, &C);
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                map[i][j] = get_arrow();
            }
        }

        int ans = slove();
        if (ans == -1) {
            printf("Case #%d: IMPOSSIBLE\n", z);
        } else {
            printf("Case #%d: %d\n", z, ans);
        }
    }

    return 0;
}

