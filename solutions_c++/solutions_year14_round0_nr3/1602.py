#include <iostream>
#include <cstring>
#include <cmath>
#include <queue>
#include <fstream>
using namespace std;
int r,t,m,c;
int ans=0,num=0;
int flag[105]={},vis[105]={};
ifstream fin("C-small-attempt8.in");
ofstream fout("C-small-attempt8.out");
typedef pair<int, int> P;
int dir[8][2] = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};
void bfs(int x, int y)
{
    queue<P> que;
    que.push(P(x, y));
    vis[x*c+y]=1;
    ans = 1;
    while(que.size())
    {
        P p=que.front();
        que.pop();
        int mark=1;
        for(int i=0; i<8; ++i)
        {
            int nx = p.first + dir[i][0], ny = p.second + dir[i][1];
            if(nx >= 0 && nx < r && ny >= 0 && ny < c)
                if(flag[nx*c+ny] == 1) mark = 0;
        }
        if(mark)
            for(int i=0; i<8; ++i)
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

int dfs()
{
    int comb = (1 << m) - 1;
    memset(flag, 0, sizeof(flag));
    int i=1,j=0;
    while(true)
    {
        if(i & comb)
            flag[j] = 1;
        j++;
        i=i*2;
        if(j >= r*c) break;
    }

    int res = r * c - m;

    for(int x = 0; x < r; ++x)
        for(int y = 0; y < c; ++y)
            if(flag[x*c+y] == 0)
            {
                ans=0;
                memset(vis, 0, sizeof(vis));
                bfs(x, y);
                if(ans == res)
                {
                    fout << "Case #" << num << ": " << endl;
                    for(int l = 0; l < r; ++l)
                    {
                        for(int g = 0; g < c; ++g)
                            if(l == x && g == y) fout << "c";
                            else if(flag[l*c+g] == 1) fout << "*";
                            else fout << ".";
                        fout << endl;
                    }
                    return 1;
                }
            }
    while(comb < 1 << r*c)
    {
        int p1 = comb & -comb, p2 = comb + p1;
        comb = ((comb & ~p2) / p1 >> 1) | p2;
        memset(flag, 0, sizeof(flag));
        int i=1,j=0,ans1=0;
        while(true)
        {
            if(i & comb)
            {
                flag[j] = 1;
                ans1++;
            }
            j++;
            i=i*2;
            if(j >= r*c) break;
        }

        for(int x = 0; x < r; ++x)
            for(int y = 0; y < c; ++y)
                if(flag[x*c+y] == 0)
                {
                    ans = 0;
                    memset(vis, 0, sizeof(vis));
                    bfs(x, y);
                    if(ans == res)
                    {
                        fout << "Case #" << num << ": " << endl;
                        for(int l = 0; l < r; ++l)
                        {
                            for(int g = 0; g < c; ++g)
                                if(l == x && g == y) fout << "c";
                                else if(flag[l*c+g] == 1) fout << "*";
                                else fout << ".";
                            fout << endl;
                        }
                        return 1;
                    }
                }
    }
    return 0;
}

void answer()
{
    memset(flag, 0, sizeof(flag));
    if(dfs() == 0)
        fout << "Case #" << num << ": " << endl << "Impossible" << endl;
}

int main()
{
    ios::sync_with_stdio(0);
    fin>>t;
    int tFirst = t;
    while(t--)
    {
        fin>>r>>c>>m;
        num=tFirst-t;
        answer();
    }
    return 0;
}
