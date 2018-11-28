#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<algorithm>
using namespace std;
char g[105][55],b[55];
int main()
{
    freopen("D-small-attempt1.in","r",stdin);
    freopen("D.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int ca=1;ca<=T;ca++)
    {
        int n,L;
        scanf("%d%d",&n,&L);
        for(int i=0;i<n;i++)
            scanf("%s",g[i]);
        scanf("%s",b);
        bool flag=1;
        for(int i=0;i<n;i++)
        {
            bool isok=0;
            for(int j=0;j<L;j++)
                isok|=g[i][j]=='0';
            flag&=isok;
        }
        printf("Case #%d: ",ca);
        if(!flag)printf("IMPOSSIBLE\n");
        else
        {
            if(L>1)for(int i=0;i<L-1;i++)
                printf("?");
            else printf("0");
            printf(" ");
            for(int i=0;i<25;i++)
                printf("10");
            printf("?");
            for(int i=0;i<25;i++)
                printf("10");
            printf("\n");
        }
    }
    return 0;
}
