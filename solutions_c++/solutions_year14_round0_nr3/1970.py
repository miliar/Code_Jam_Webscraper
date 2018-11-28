#include <iostream>  
#include <cstdlib>  
#include <cstdio>  
#include <memory.h>  
#include <cstring>  
#include <cmath>  
#include <ctime>  
#include <algorithm>  
#include <set>  
#include <vector>  
#include <set>  
#include <map>  
#include <queue>  
#include <stack>  
#include <bitset>  
  
using namespace std;  
  

int ans = 0;  
int num = 1;  
int flag[105] = {0};  
int vis[105] = {0};  
  
typedef pair<int, int> P;  
int dir[8][2] = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};  
  
void bfs(int x, int y,int r,int c,int m)  
{  
    queue<P> que;  
  
    que.push(P(x, y));  
    vis[x*c+y] = 1;  
    ans = 1;  
  
    while(que.size())  
    {  
        P p = que.front();  
        que.pop();  
  
        int mark = 1;  
        for(int i = 0; i < 8; ++i)  
        {  
            int nx = p.first + dir[i][0], ny = p.second + dir[i][1];  
            if(nx >= 0 && nx < r && ny >= 0 && ny < c)  
            {  
                if(flag[nx*c+ny] == 1) mark = 0;  
            }  
        }  
        if(mark)  
        {  
            for(int i = 0; i < 8; ++i)  
            {  
                int nx = p.first + dir[i][0], ny = p.second + dir[i][1];  
                if(nx >= 0 && nx < r && ny >= 0 && ny < c && vis[nx*c+ny] == 0)  
                {  
                    vis[nx*c+ny] = 1;  
                    ans++;  
                    que.push(P(nx, ny));  
                }  
            }  
        }  
    }  
}  
  
int dfs(int r,int c,int m)  
{  
    int comb = (1 << m) - 1;  
    memset(flag, 0, sizeof(flag));  
    int i = 1;  
    int j = 0;  
    while(true)  
    {  
        if(i & comb)  
        {  
            flag[j] = 1;  
        }  
        ++j;  
        i*=2;  
        if(j >= r*c) break;  
    }  
  
    int res = r * c - m;  
  
    for(int x = 0; x < r; ++x)  
    {  
        for(int y = 0; y < c; ++y)  
        {  
            if(flag[x*c+y] == 0)  
            {  
                ans = 0;  
                memset(vis, 0, sizeof(vis));  
                bfs(x, y,r,c,m);  
                if(ans == res)  
                {  
                    cout << "Case #" << num << ": " << endl;  
                    for(int l = 0; l < r; ++l)  
                    {  
                        for(int g = 0; g < c; ++g)  
                        {  
                            if(l == x && g == y) cout << "c";  
                            else if(flag[l*c+g] == 1) cout << "*";  
                            else cout << ".";  
                        }  
                        cout << endl;  
                    }  
                    return 1;  
                }  
            }  
        }  
    }  
  
    while(comb < 1 << r*c)  
    {  
        int p1 = comb & -comb, p2 = comb + p1;  
        comb = ((comb & ~p2) / p1 >> 1) | p2;  
  
        memset(flag, 0, sizeof(flag));  
        int i = 1;  
        int j = 0;  
        int ans1 = 0;  
        while(true)  
        {  
            if(i & comb)  
            {  
                flag[j] = 1;  
                ++ans1;  
            }  
            ++j;  
            i*=2;  
            if(j >= r*c) break;  
        }  
  
        for(int x = 0; x < r; ++x)  
        {  
            for(int y = 0; y < c; ++y)  
            {  
                if(flag[x*c+y] == 0)  
                {  
                    ans = 0;  
                    memset(vis, 0, sizeof(vis));  
                    bfs(x, y,r,c,m);  
                    if(ans == res)  
                    {  
                        cout << "Case #" << num << ": " << endl;  
                        for(int l = 0; l < r; ++l)  
                        {  
                            for(int g = 0; g < c; ++g)  
                            {  
                                if(l == x && g == y) cout << "c";  
                                else if(flag[l*c+g] == 1) cout << "*";  
                                else cout << ".";  
                            }  
                            cout << endl;  
                        }  
                        return 1;  
                    }  
                }  
            }  
        }  
    }  
    return 0;  
}  
  
void Solve(int r,int c,int m)  
{  
    memset(flag, 0, sizeof(flag));  
    if(dfs(r,c,m) == 0)  
    {  
        cout << "Case #" << num << ": " << endl << "Impossible" << endl;  
    }  
	num++;
}  
  
int main()  
{  
    int t,r,c,m,num;
  
    cin >> t;  
    int tF = t;  
    while(t--)  
    {  
        cin >> r >> c >> m;  
        //cout<<r<<"  "<<c;
        num = tF - t;  
        Solve(r,c,m);  
    }  
    return 0;  
}  
