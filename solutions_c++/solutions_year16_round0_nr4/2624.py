#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    scanf("%d",&T);
    for (int tt=1;tt<=T;tt++)
    {
        int k,c,s;
        scanf("%d%d%d",&k,&c,&s);
        printf("Case #%d:",tt);
        if (c==1)
        {
            for (int i=1;i<=k;i++)
                printf(" %d",i);
        }
        else
        {
            for (int i=1;i<=k;i++)
                printf(" %d",(i-1)*k+i);
        }
        printf("\n");
    }
    return 0;
}
