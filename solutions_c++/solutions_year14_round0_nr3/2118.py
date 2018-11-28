#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <algorithm>
#include <string.h>
using namespace std;
int dx[8] = {-1, -1, -1, 0, 1, 1, 1, 0};
int dy[8] = {-1, 0, 1, 1, 1, 0, -1, -1};
int r, c, m;
char ans[20][20];
char a[20][20];
bool v[20][20];
int b[20][20];
int cnt;
bool flag;

void calc(int x, int y){
    if (x < 1 || x > r) return;
    if (y < 1 || y > c) return;
    if (v[x][y]) return ;
    v[x][y] = 1;
    cnt++;
    if (b[x][y] == 0)
        for (int i = 0; i < 8; ++i)
            if (a[x + dx[i]][y + dy[i]] == '.')
                calc(x + dx[i], y + dy[i]);
}

bool check(){
/*
    for (int i = 1; i <= r; ++i){
        for (int j = 1; j <= c; ++j)
            putchar(a[i][j]);
        puts("");
    }
*/
    memset(b, 0, sizeof(b));
    memset(v, 0, sizeof(v));
    for (int i = 1; i <= r; ++i)
        for (int j = 1; j <= c; ++j){
            for (int k = 0; k < 8; ++k)
                b[i][j] += (a[i + dx[k]][j + dy[k]] == '*');
        }
    for (int i = 1; i <= r; ++i)
        for (int j = 1; j <= c; ++j){
            if (a[i][j] == '.'){
                cnt = 0;
                calc(i, j);
                if (cnt == r * c - m){
                    flag =1;
                    return 1;
                }else{
                    return 0;
                }
            }
        }
}

void Dfs(int x, int y, int tot){
    if (flag) return;
    if (y > c) y = 1, x++;
    //cout <<x << " "<< y <<endl;
    if (x > r){
        if (tot < m) return;
        flag |= check();
        //cout << "!" << endl;
        if (flag){
            for (int i = 1; i <= r; ++i)
                for (int j = 1; j <= c; ++j)
                    ans[i][j] = a[i][j];
        }
        return;
    }
    if (tot > m) return;
    if (r * c - (x - 1) * c + tot < m) return;
    a[x][y] = '.';
    Dfs(x, y + 1, tot);
    a[x][y] = '*';
    Dfs(x, y + 1, tot + 1);
}

void output(){
    for (int i = 1; i <= r; ++i)
        for (int j = 1; j <= c; ++j){
            if (ans[i][j] == '.'){
                ans[i][j] = 'c';
                for (int x = 1; x <= r; ++x){
                    for (int y = 1; y <= c; ++y){
                        putchar(ans[x][y]);
                    }
                    puts("");
                }
                return;
            }
        }
}
void solve(){
    scanf("%d%d%d", &r, &c, &m);
    flag = 0;
    Dfs(1, 1, 0);
    //cout << "!" << endl;
    if (flag)
        output();
    else
        puts("Impossible");
}

int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int _;
    scanf("%d", &_);
    for (int __ = 1; __ <= _; ++__){
        memset(a, '.', sizeof(a));
        printf("Case #%d:\n", __);
        solve();
    }
    return 0;
}
