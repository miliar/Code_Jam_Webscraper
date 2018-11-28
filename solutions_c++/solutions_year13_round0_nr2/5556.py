#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

char s[11][11];
int a[111][111];

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int ca,t=0;
    for(scanf("%d",&ca);ca--;)
    {
        printf("Case #%d: ",++t);
        int n,m;
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                scanf("%d",&a[i][j]);
        int r[111]={},c[111]={};
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                r[i]=max(r[i],a[i][j]);
        for(int i=0;i<m;i++)
            for(int j=0;j<n;j++)
                c[i]=max(c[i],a[j][i]);
        bool f=1;
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                if(a[i][j]<min(r[i],c[j])) f=0;
        if(f) printf("YES\n");
        else puts("NO");
    }
    return 0;
}
