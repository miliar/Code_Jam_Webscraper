#include <cstdio>
#include <string>
#include <iostream>
using namespace std;


int r, c, m;
string board[10];
bool check, vis[5][5];
int cx[8] = {0, 0, 1, 1, 1, -1, -1, -1};
int cy[8] = {-1, 1, -1, 0, 1, -1, 0, 1};

int dfs(int x, int y)
{
    int ret = 1;
    vis[x][y] = true;
    bool check = false;
    for(int i = 0; i < 8; i++) {
        if(x + cx[i] < 0 || x + cx[i] >= r) continue;
        if(y + cy[i] < 0 || y + cy[i] >= c) continue;
        if(board[x + cx[i]][y + cy[i]] == '*') check = true;
    }
    if(check == false)
        for(int i = 0; i < 8; i++){
            if(x + cx[i] < 0 || x + cx[i] >= r) continue;
            if(y + cy[i] < 0 || y + cy[i] >= c) continue;
            if(vis[x + cx[i]][y + cy[i]] == false)
                ret += dfs(x + cx[i], y + cy[i]);
        }
    return ret;
}

int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int t = 1; t <= T; t++)
    {
        scanf("%d%d%d",&r,&c,&m);
        check = false;
        for(int i = 0; i < r; i++)
        {
            board[i] = "";
            for(int j = 0; j < c; j++)
                board[i] += '.';
        }
        for(int i = (1 << (r * c)) - 1; i >= 0 ; i--)
        {
            int cnt = 0;
            for(int j = 0; j < r * c; j++) if(i & (1 << j)) cnt++;
            if(cnt != m) continue;

            for(int j = 0; j < r * c; j++)
                if(i & (1 << j)) board[j / c][j % c] = '*';
                else board[j / c][j % c] = '.';
            /*
            for(int k = 0; k < r; k++)
                printf("%s\n",board[k].c_str());
            */
            for(int x = 0; x < r; x++)
                for(int y = 0; y < c; y++){
                    if(board[x][y] == '*') continue;
                    memset(vis, 0, sizeof(vis));
                    if(check != true && dfs(x, y) == r * c - m){
                        board[x][y] = 'c';
                        check = true;
                    }
                }
            if(check == true) break;
        }

        printf("Case #%d:\n", t);
        if(check == false)
            printf("Impossible\n");
        else
            for(int i = 0; i < r; i++)
                printf("%s\n",board[i].c_str());
    }
    return 0;
}
