#include<stdio.h>

int main()
{
    int t;
    scanf("%d",&t);
    int i,j,k,l;
    for(i=1;i<=t;i++)
    {
        l=0;
        scanf("%d%d",&j,&k);
        if(j<=1&&k>=1)l++;
        if(j<=4&&k>=4)l++;
        if(j<=9&&k>=9)l++;
        if(j<=121&&k>=121)l++;
        if(j<=484&&k>=484)l++;
        //if(j<=676&&k>=676)l++;
        printf("Case #%d: %d\n",i,l);
    }
    
    return 0;
}
