#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;
int a[110][110];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int ii=1;ii<=T;ii++)
    {
        int n,m;
        scanf("%d%d",&n,&m);
        for (int i=0;i<n;i++)
            for (int j=0;j<m;j++)
                scanf("%d",&a[i][j]);
        bool ok=true;
        for (int i=0;i<n;i++)
            for (int j=0;j<m;j++)
            {
                int maxc=0,maxr=0;
                for (int k=0;k<m;k++)
                    maxc=max(maxc,a[i][k]);
                for (int k=0;k<n;k++)
                    maxr=max(maxr,a[k][j]);
                if (a[i][j]!=maxc&&a[i][j]!=maxr) ok=false;
            }
        printf("Case #%d: %s\n",ii,ok?"YES":"NO");
    }
    return 0;
}

