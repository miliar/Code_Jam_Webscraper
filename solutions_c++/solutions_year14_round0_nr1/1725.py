#include <iostream>
#include <cstdio>
#include <cstring>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <functional>
#include <queue>
#include <vector>
#include <cstdlib>
#include <string>
#include <set>
using namespace std;

const int N = 1000100;
const int INF = 1000000000;
const double eps = 1e-8;

int a[10][10], b[10][10];
vector<int> v;
bool vis[10];

void solve()
{
        v.clear();
        int k;
        scanf("%d", &k);
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                int x;
                scanf("%d", &x);
                if(i==k)v.push_back(x);
            }
        }
        scanf("%d", &k);
        memset(vis, 0, sizeof(vis));
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                int x;
                scanf("%d", &x);
                if(i==k)
                {
                    for(int ii=0;ii<4;ii++)
                        if(v[ii]==x)
                            vis[ii]=true;
                }
            }
        }
        int cnt=0, x;
        for(int i=0;i<4;i++)
            if(vis[i])
            {
                cnt++;x=v[i];
            }
        if(cnt==1)printf("%d\n", x);
        else if(cnt==0)puts("Volunteer cheated!");
        else puts("Bad magician!");
}

int main()
{
    freopen("in_.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d", &t);
    for(int i=1;i<=t;i++)
    {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
