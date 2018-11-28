#include <stdio.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <algorithm>

using namespace std;

int t,n,m,s,ans;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    bool flag;
    scanf("%d",&t);
    for(int cas=1;cas<=t;++cas)
    {
        scanf("%d%d%d",&n,&m,&s);
        printf("Case #%d:",cas);
        if(s>=n)
            for(int i=1;i<=n;i++)
                printf(" %d",i);
        else
            printf(" IMPOSSIBLE");
        printf("\n");
    }
    return 0;
}
