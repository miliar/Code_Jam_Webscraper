#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    int t,k,c,s,i,j;
    scanf("%d",&t);
    i=1;
    while(t--)
    {
        scanf("%d%d%d",&k,&c,&s);
        printf("Case #%d: ",i++);
        for(j=1;j<=k;j++)
            printf("%d ",j);
        printf("\n");
    }
    return 0;
}
