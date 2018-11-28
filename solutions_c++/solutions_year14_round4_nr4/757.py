#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<string>
#include<vector>

using namespace std;

int m, n, ansn, ansx;

struct Trie
{
    int next[30];
    void init()
    {
        for(int i = 0 ; i < 30 ; i++)next[i] = -1;
    }
}R[10000];

vector<string> st[5];

int work()
{
    for(int i = 0 ; i < n ; i++)
        if(st[i].size() == 0)return -1;

//    cout<<st[0].size()<<" "<<st[1].size()<<endl;

    int res = 0;
    for(int i = 0 ; i < n ; i++)
    {
        res += 1;
        R[0].init();
        int tot = 1;
        for(int j = 0 ; j < st[i].size() ; j++)
        {
            string str = st[i][j];
            int now = 0;
            for(int k = 0 ; k < str.size() ; k++)
            {
                if(R[now].next[str[k] - 'A'] == -1)
                {
                    res++;
                    R[now].next[str[k] - 'A'] = tot;
                    R[tot].init();
                    now = tot;
                    tot++;
                }
                else
                {
                    now = R[now].next[str[k] - 'A'];
                }
            }
        }
    }
    return res;
}

char str[10][20];

void dfs(int x)
{
    if(x >= m)
    {
        int tmp = work();
        if(ansx == tmp)ansn = (ansn + 1) % 1000000007;
        if(ansx < tmp){ansx = tmp; ansn = 1;}
        return;
    }
    for(int i = 0 ; i < n ; i++)
    {
        string s1(str[x]);
        st[i].push_back(s1);
        dfs(x + 1);
        st[i].pop_back();
    }
}

int main()
{
    freopen("x.in", "r", stdin);
    freopen("x.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1 ; cas <= T ; cas++)
    {
        scanf("%d%d", &m, &n);
        for(int i = 0 ; i < m ; i++)
        {
            scanf(" %s", str[i]);
        }
        ansx = 0;
        ansn = 0;
        dfs(0);

        printf("Case #%d: %d %d\n", cas, ansx, ansn);
    }
    return 0;
}
