#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <cmath>
#include <algorithm>
#include <map>

using namespace std;


int n,m;
int a[110][110];
int row[110];
int col[110];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++)
    {
        scanf("%d%d",&n,&m);
        for (int i=0;i<n;i++)
            for (int j=0;j<m;j++)
            {
                scanf("%d",&a[i][j]);
            }
        for (int i=0;i<n;i++)
        {
            row[i]=a[i][0];
            for (int j=1;j<m;j++)
                row[i]=max(row[i],a[i][j]);
        }
        for (int j=0;j<m;j++)
        {
            col[j]=a[0][j];
            for (int i=1;i<n;i++)
                col[j]=max(col[j],a[i][j]);
        }
        bool can=true;
        for (int i=0;i<n;i++)
            for (int j=0;j<m;j++)
            {
                if (a[i][j]!=min(col[j],row[i])) can=false;
            }
        if (can) printf("Case #%d: YES\n",cas);
        else printf("Case #%d: NO\n",cas);
    }


}
