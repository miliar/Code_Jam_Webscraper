#include <iostream>
#include <stdio.h>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out","w",stdout);
    int o, cas=0;
    int a[20],b[20];
    scanf("%d",&o);
    while (o--)
    {
        int p1,p2,x;
        scanf("%d",&p1);
        for (int i=1; i<=4; i++)
            for (int j=1; j<=4; j++)
            {
                scanf("%d",&x);
                a[x]=i;
            }
        scanf("%d",&p2);
        for (int i=1; i<=4; i++)
            for (int j=1; j<=4; j++)
            {
                scanf("%d",&x);
                b[x]=i;
            }
        int ans=0,cnt=0;
        for (int i=1; i<=16; i++)
            if (a[i]==p1 && b[i]==p2) {cnt++; ans=i;}
        printf("Case #%d: ",++cas);
        if (cnt==1) printf("%d\n",ans);
        else if (cnt==0) printf("Volunteer cheated!\n");
        else printf("Bad magician!\n");
    }
    return 0;
}