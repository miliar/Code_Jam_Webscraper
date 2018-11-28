#include <cstdio>
using namespace std;

char s[100][101];

int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
char ch[4] = {'v', '>', '^', '<'};

int solve(int r, int c) {
    int ans = 0;
    for(int i = 0; i < r; i++) {
        for(int j = 0; j < c; j++) {
            if(s[i][j] == '.') continue;
            bool found = false;
            for(int d = 0; d < 4; d++)
                for(int x = i + dx[d], y = j + dy[d]; x >= 0 && x < r && y >= 0 && y < c; x += dx[d], y += dy[d])
                    if(s[x][y] != '.') {
                        if(s[i][j] == ch[d])
                            goto no_change;
                        else
                            found = true;
                    }
            if(found)
                ans++;
            else
                return -1;
            no_change:;
        }
    }
    return ans;
}

int main() {
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++) {
        int r, c;
        scanf("%d %d", &r, &c);
        for(int j = 0; j < r; j++)
            scanf("%s", s[j]);

        int ans = solve(r, c);
        if(ans >= 0)
            printf("Case #%d: %d\n", i, ans);
        else
            printf("Case #%d: IMPOSSIBLE\n", i);
    }
}
