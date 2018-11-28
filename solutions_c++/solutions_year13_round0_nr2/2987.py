#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <sstream>
#include <cmath>
#include <algorithm>

using namespace std;
int n,m;
int lawn[105][105];
bool solve()
{
    scanf("%d%d",&n,&m);
    for (int i=0;i<n;++i)
    {
        for (int j=0;j<m;++j)
        {
            scanf("%d",&lawn[i][j]);
        }
    }
    for (int i=0;i<n;i++)
    {
        for (int j=0;j<m;++j)
        {
            int k;
            bool flag = false;
            for (k=0;k<n;++k)
            {
                if (lawn[i][j]<lawn[k][j]) break;
            }
            if (k==n) flag = true;
            for (k=0;k<m;++k)
            {
                if (lawn[i][j]<lawn[i][k]) break;
            }
            if (k==m) flag = true;
            if (!flag)
            {
                return false;
            }
        }
    }
    return true;
}

int main()
{
//    freopen("B-large.in","r",stdin);
//    freopen("B-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for (int cases=1;cases<=t;++cases)
    {
        printf("Case #%d: ",cases);
        if (solve()) puts("YES");
        else puts("NO");
    }
    return 0;
}
