#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    int t,i,j,k,c,s;
    scanf("%d",&t);
    for(j=1;j<=t;++j)
    {
        scanf("%d%d%d",&k,&c,&s);
        printf("Case #%d: ",j);
        for(i=1;i<=s;++i)
            printf("%d ",i);
        printf("\n");
    }
}