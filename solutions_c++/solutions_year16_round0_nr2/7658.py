#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>
#include <iostream>
#include <map>
#include <queue>
using namespace std;
int n, last;
map<string, int> dis;
bool check(string &s)
{
    for (int i = 0; i < n; i++)
        if (s[i] == '-')
            return false;
    return true;
}
void work(string &s, int x)
{
    for (int i = 0; i <= x; i++)
    {
        if (i > x / 2) break;
        int temp = s[i];
        s[i] = s[x - i] == '+' ? '-' : '+';
        s[x - i] = temp == '+' ? '-' : '+';
    }
}
int bfs(string &s)
{
    queue<string> q;
    dis.clear();
    q.push(s);
    dis[s] = 0;
    while (!q.empty())
    {
        string now = q.front();
        int d = dis[now];
        for (int i = n - 1; i >= 0; i--)
        {
            work(now, i);
            if (dis.find(now) == dis.end())
            {
                dis[now] = d + 1;
                q.push(now);
                if (check(now))
                    return (d + 1);
            }
            work(now, i);
        }
        q.pop();
    }
    return -1;
}
int main()
{
    freopen("B-small-attempt1.in", "r", stdin);
    freopen("B-small-attempt1.out", "w", stdout);
    int t, Case = 0;
    cin>>t;
    while (t--)
    {
        
        string s;
        cin>>s;
        n = (int)s.length();
        if (check(s))
        {
            printf("Case #%d: 0\n", ++Case);
            continue;
        }
        printf("Case #%d: %d\n", ++Case, bfs(s));
    }
    
}