#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <string>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cmath>
#include <vector>
#include <cstring>
#include <list>
#include <ctime>
#include <sstream>
#include <ctime>
#define mod 1000000007
#define INF 10000
using namespace std;

int a[110][110];

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T,cas=0,i,j,n,m,k;
    scanf("%d",&T);
    while(T--)
    {
        int flag,can=1;
        scanf("%d%d",&n,&m);
        for(i=1;i<=n;i++)
            for(j=1;j<=m;j++)
                scanf("%d",&a[i][j]);
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=m;j++)
            {
                flag=0;
                for(k=1;k<=n;k++)
                {
                    if(a[k][j]>a[i][j])
                    {
                        flag=1;
                        break;
                    }
                }
                if(flag==0)
                    continue;
                flag=0;
                for(k=1;k<=m;k++)
                {
                    if(a[i][k]>a[i][j])
                    {
                        flag=1;
                        break;
                    }
                }
                if(flag==1)
                {
                    can=0;
                    break;
                }
            }
            if(can==0)
                break;
        }
        if(can==1)
            printf("Case #%d: YES\n",++cas);
        else
            printf("Case #%d: NO\n",++cas);
    }
    return 0;
}
