#include <bits/stdc++.h>
#define foreach(IT,C) for(typeof(C.begin())IT=C.begin();IT!=C.end();IT++)

using namespace std;

int Y,X;
string M[109];

//          ^  v  < >
int mx[] = {0 ,0,-1,1};
int my[] = {-1,1,0 ,0};

int dir(char c){
    if (c == '^')return 0;
    if (c == 'v')return 1;
    if (c == '<')return 2;
    if (c == '>')return 3;
    assert(false);
}

bool point_wall(int y,int x,char c) {
    int d = dir(c);

    while (true) {
        y += my[d];
        x += mx[d];

        if(x<0 or x>=X or y<0 or y>=Y)return true;
        if (M[y][x] != '.')return false;
    }
}

int solve() {
    cin >> Y >> X;

    for(int i=0;i<Y;i++) {
        cin >> M[i];
    }

    int ans = 0;
    for(int i=0;i<Y;i++) {
        for(int j=0;j<X;j++) {
            if (M[i][j] != '.' and point_wall(i,j,M[i][j]) == true) {

                if (point_wall(i,j,'v') and point_wall(i,j,'<') and point_wall(i,j,'>') and point_wall(i,j,'^')) {
                    return -1;
                }
                ans++;
            }
        }
    }
    return ans;
}

int main() {
    int NC;cin >> NC;
    for (int i = 1; i <= NC; i++) {
        int ans = solve();
        printf("Case #%d: ", i);
        if (ans >= 0) {
            printf("%d\n", ans);
        } else {
            printf("IMPOSSIBLE\n");
        }
    }
}