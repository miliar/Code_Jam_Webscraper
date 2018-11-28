#include <iostream>
#include <string.h>
#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;
const int Maxn = 100;
int T;
int tar[Maxn], b[Maxn];
int C,R;
int a[Maxn][Maxn];
int tC[Maxn], rR[Maxn], dC[Maxn], lR[Maxn];
const int sp[4][2] ={{1,0},{0,1},{0,-1},{-1,0}};
int path(int x, int y, int dir){
    if (x == 0) return tC[y];
    if (x == R + 1) return dC[y];
    if (y == 0) return lR[x];
    if (y == C + 1) return rR[x];
    if (a[x][y]){
        if (dir <= 1) dir = 1 - dir;
        else dir = 5 - dir;
    }
    else {
        if (dir % 2) dir = 4 - dir;
        else dir = 2 - dir;
    }
    return path(x + sp[dir][0], y + sp[dir][1], dir);
}
int check(){
    for (int i = 1; i <= C; i++){
        if (tar[tC[i]] != path(1, i, 0)) 
            return 0;
    }
    for (int i = 1; i <= R; i++) {
        if (tar[rR[i]] != path(i, C, 2))
            return 0;
    }
    for (int i = 1; i <= C; i++) {        
        if (tar[dC[i]] != path(R, i, 3)) 
            return 0;
    }
    for (int i = 1; i <= R; i++) {
        if (tar[lR[i]] != path(i, 1, 1)) 
            return 0;
    }
    return 1;
}
int dfs(int x, int y){
    if (x == R + 1)
        return check();   
    if (y == C + 1)
        return dfs(x + 1, 1);        
    a[x][y] = 0;
    if (dfs(x, y + 1)) return 1;
    a[x][y] = 1;
    if (dfs(x, y + 1)) return 1;
    return 0;
}
int main()
{
    cin >> T;
    for (int cs = 1; cs <= T; cs ++){
        printf("Case #%d:\n",cs);
        cin >> R >> C;
        for (int i = 1; i <= C; i++) tC[i] = i;
        for (int i = 1; i <= R; i++) rR[i] = C + i;
        for (int i = 1; i <= C; i++) dC[i] = 2 * C + R - i + 1;
        for (int i = 1; i <= R; i++) lR[i] = 2 * C + 2 * R - i + 1;
        for (int i=1;i <= 2 * (R + C); i++){
            cin >> b[i];
        }
        for (int i=0;i < (R + C); i++){
            tar[b[i * 2 + 1]] = b[i * 2 + 2];
            tar[b[i * 2 + 2]] = b[i * 2 + 1];
        }
        // for (int i = 1; i <= C; i++) cout << tC[i] <<" "; cout << endl;
        // for (int i=1; i <= 2 *(R + C);i++) cout << tar[i] << " "; cout<< endl;
        if (dfs(1 , 1)){
            for (int i = 1; i<= R; i++){
                for (int j = 1; j <= C; j++)
                    cout << (a[i][j]?'\\':'/');
                cout << endl;
            }
        }        
        else puts("IMPOSSIBLE");
    }
    
    return 0;
}