#include<iostream>
#include<string.h>
#include<stdio.h>
#include<math.h>
#include<stdlib.h>

using namespace std;

int main()
{
    freopen("0in.txt","r",stdin);
    freopen("0out.txt","w",stdout);

    int k,c,s,t,i;
    scanf("%d",&t);

    for(int kk1=1;kk1<=t;kk1++)
    {
        scanf("%d%d%d",&k,&c,&s);
        printf("Case #%d: ",kk1);
        for(i=1;i<=k;i++)
        {
            printf("%d ",i);
        }
        printf("\n");


    }

}
