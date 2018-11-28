#include <iostream>
#include <algorithm>
#include <string>
#include <stdio.h>
#include <cstring>
#include <vector>
using namespace std;
typedef long long LL;
#define S 205
int n,t,txt,r,c;
int grid[S][S],row[S],col[S];
int main()
{
    freopen("1.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int i,j,k;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d",&r,&c);
        memset(row, 0, sizeof row);
        memset(col, 0, sizeof col);
        for(int i = 0; i < r; ++i)for(int j = 0; j < c; ++j)
        {
            scanf("%d",&grid[i][j]);
            row[i] = max(row[i],grid[i][j]);
            col[j] = max(col[j],grid[i][j]);
        }
        bool ok = true;
        for(int i = 0; i < r; ++i)for(int j = 0; j < c; ++j)
        {
            if(grid[i][j] < row[i] && grid[i][j] < col[j])ok = false;
        }
        string ans = "NO";
        if(ok)ans = "YES";
        cout << "Case #" << ++txt <<": "<< ans << endl;
    }
    return 0;
}
