#include"stdio.h"
main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("smal0.out","w",stdout);
    int k;
    scanf("%d",&k);
    int r,t;
    int sum=0,c=0;

    for(int j=1;j<=k;j++)
    {
    scanf("%d %d",&r,&t);
    sum=0;
    c=0;
    while(1)
    {
        sum+=2*r+1;
        if(sum>t)
            break;
        r+=2;
        c++;
    }
    printf("Case #%d: %d\n",j,c);
    }

}
