#include<stdio.h>
int main()
{
    int a[5]={1,4,9,121,484};
    int T,s,l,x,y,i;
    scanf("%d",&T);
    for( i=1;i<=T;i++)
    {
         s=0;l=4;
         scanf("%d%d",&x,&y);
         while(a[s]<x)
               s++;
         while(a[l]>y)
                      l--;
         printf("Case #%d: %d\n",i,l-s+1);
    }
}
