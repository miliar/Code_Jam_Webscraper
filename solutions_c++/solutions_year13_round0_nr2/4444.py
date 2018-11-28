#include <stdio.h>
#include <iostream>
using namespace std;

int t,n,m;
int a[200][200];

bool check(int x,int y)
{
    bool flag = true;

    for (int i = 0;i < n;++i)
        if (a[i][y] > a[x][y])
        {
            flag = false;
            break;
        }
    if (flag) return true;
    flag = true;
    for (int i = 0;i < m;++i)
        if (a[x][i] > a[x][y])
        {
            flag = false;
            break;
        }
    if (flag) return true;
    else return false;
}

int main()
{
    freopen("B1.in","r",stdin);
    freopen("B1.out","w",stdout);
    scanf("%d",&t);
    for (int w = 1;w <= t;++w)
    {
        cin >> n >> m;
        for (int i = 0;i < n;++i)
            for (int j = 0;j < m;++j)
                scanf("%d",&a[i][j]);
        bool flag = true;
        for (int i = 0;i < n;++i)
        {
            for (int j  = 0;j < m;++j)
                if (!check(i,j))
                {
                    flag = false;
                    break;
                }
            if (!flag) break;
        }
        printf("Case #%d: ",w);
        if (flag) printf("YES\n");
        else printf("NO\n");
    }

    return 0;
}
