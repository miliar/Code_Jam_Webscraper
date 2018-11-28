/*
    Just For You 97116:)
*/

#include <iostream>
#include <stdio.h>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("dsmalloutput.txt","w",stdout);
    //freopen("dlargeoutput.txt","w",stdout);
    int t,k,c,s,i,j;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        scanf("%d%d%d",&k,&c,&s);
        printf("Case #%d: ",i);
        for(j=1;j<=s;j++)
            printf("%d ",j);
        printf("\n");
    }
    return 0;
}