#include<iostream>
#include<stdio.h>

using namespace std;

int main()
{
    int t,v=1,c,s,i,k;
    scanf("%d",&t);
    while(v<=t)
    {
        scanf("%d%d%d",&k,&c,&s);
        printf("Case #%d: ",v);
        for(i=1 ; i<=k ; i++)
        {
            printf("%d ",i);
        }
        printf("\n");
        v++;
    }
    return 0;
}
