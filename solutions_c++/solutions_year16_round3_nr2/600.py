#include<iostream>
#include<stdio.h>
#include<string.h>
#include<string>
#include<algorithm>
using namespace std;
int grid[51][51];
int main(){
    freopen("inputB.in", "r", stdin);
    freopen("outputB.in", "w", stdout);
    int T;
    cin>>T;
    for(int t = 1; t <= T; t++){
        memset(grid, 0, sizeof grid);
        int n;
        long long m;
        cin>>n>>m;
        n--;
        printf("Case #%d: ", t);
        if((1LL << (n - 1)) < m){
            puts("IMPOSSIBLE");
            continue;
        }
        puts("POSSIBLE");
        for(int i = 1; i < n; i++)
            for(int j = 0; j < i; j++)
                grid[j][i] = 1;
        for(int i = 1; i < n; i++) if(((1LL << (i - 1)) & m) || m == (1LL << (n - 1)))
            grid[i][n] = 1;
        if(m == (1LL << (n - 1)))
            grid[0][n] = 1;
        for(int i = 0; i <= n; i++){
            for(int j = 0; j <= n; j++)
                printf("%d", grid[i][j]);
            puts("");
        }
    }
    return 0;
}

