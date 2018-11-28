#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <map>
#include <cstring>
#define MAX 100000   

using namespace std;   

vector <int> tree[MAX+5];
int c[MAX+5];
int con[MAX+5];
map <int, int> cc[MAX+5];

void findfa(int x, int fx)
{
//    cout<<x<<endl;
//    int cnt = 0;
    for (int i=0;i<tree[x].size();++i)
    {
        if (tree[x][i] == fx) continue;
        con[ tree[x][i] ] = x;
        findfa(tree[x][i], x);
//        cnt ++;
    }
//    if (cnt!=tree[x].size() - 1) printf("!! %d\n", x);
}

void solve(int cases)
{
    int n,q;
    printf("Case #%d:\n", cases);
    int ans = 1;
    scanf("%d", &n);
    for (int i=1;i<=n;++i)
    {
        tree[i].clear();
        cc[i].clear();
    }
    int x,y;
    for (int i=1;i<n;++i)
    {
        scanf("%d%d",&x, &y);
        tree[x].push_back(y);
        tree[y].push_back(x);
    }

    for (int i=1;i<=n;++i)
    {
        if (i == 1)
        {
            cc[1][0] = tree[i].size();
            continue;
        }
        cc[i][0] = tree[i].size()-1;
    }

    findfa(1, 0);
    con[1] = 0;

    scanf("%d", &q);
    memset(c, 0, sizeof(c));

    int ins;
    for (int i=0;i<q;++i)
    {
        scanf("%d", &ins);
//            cout<<"~~"<<ins<<endl;
        if (ins==1)
        {
            printf("%d\n", ans);
        }
        else if(ins == 2)
        {
            scanf("%d%d", &x, &y);

            int oric = c[x];
            int cnt_oric = cc[x][oric], cnt_y = cc[x][y];
            if (con[x]!=0)
            {
                if (c[con[x]] == oric) cnt_oric ++;
                if (c[con[x]] == y) cnt_y ++;
                cc[con[x]][oric] --;
                cc[con[x]][y] ++;
            }

            ans = ans + cnt_oric - cnt_y;

            c[x] = y;
        }
    }
}

int main()
{
    freopen("in.txt", "r", stdin);

    int t;
    scanf("%d",&t);
    for (int cases = 1; cases <= t; ++cases)
    {
        solve(cases);
    }

    return 0;
}
