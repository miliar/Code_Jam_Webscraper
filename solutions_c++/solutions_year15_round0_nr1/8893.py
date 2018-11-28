#include<iostream>
#include<stdio.h>
int main()
{
    int t,ti;
    scanf("%d",&t);
    for(ti=1;ti<=t;ti++)
    {
        char str[1001];
        int smax,i,abc,ans=0,tot=0;
        scanf("%d",&smax);
        scanf("%s",str);
        for(i=0;i<=smax;i++)
        {
            //scanf("%d",&abc);
            abc=str[i]-48;
            if(tot<i)
            {
                //printf("tot<i\n");
                ans+=i-tot;
                tot=i;
            }
            //else
                //printf("tot>=i\n");
            tot+=abc;
        }
        printf("Case #%d: %d\n",ti,ans);
    }
}
