#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>

#define MAXN 105

using namespace std;

int t,n,m;
int a[MAXN][MAXN];

bool check()
{
    for (int i=0;i<n;++i)
    {
        for (int j=0;j<m;++j)
        {
            int flag = 0;
            for (int k=0;k<n;++k)
            {
                if (a[i][j]<a[k][j]) flag = true;
            }
            for (int k=0;k<m;++k)
            {
                if (a[i][j]<a[i][k]) if (flag) return false;
            }
        }
    }
    return true;
}

int main()
{
//    freopen("B-large.in","r",stdin);
//    freopen("B-large.out","w",stdout);
    scanf("%d",&t);
    for (int cases=1;cases<=t;++cases)
    {
        scanf("%d%d",&n,&m);
        for (int i=0;i<n;++i)
        {
            for (int j=0;j<m;++j)
            {
                scanf("%d",&a[i][j]);
            }
        }

        if(check()) printf("Case #%d: YES\n",cases);
        else printf("Case #%d: NO\n",cases);
    }
    return 0;
}
