#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

int main()
{
    freopen("D.in","r",stdin);
    freopen("D.out","w",stdout);
    int T,k,c,s,i,j;
    scanf("%d",&T);
    for (i=1; i<=T; i++)
    {
        scanf("%d%d%d",&k,&c,&s);
        printf("Case #%D:",i);
        for (j=1; j<=s; j++)
            printf(" %d",j);
        printf("\n");
    }
    return 0;
}
